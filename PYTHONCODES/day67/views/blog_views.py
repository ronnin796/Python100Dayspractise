from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from extensions import db
from models import BlogPost, Comment
from forms import BlogPostForm, CommentForm
from datetime import date
from utils import admin_required, send_mail

blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/")
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    all_posts = result.scalars().all()
    return render_template("index.html", all_posts=all_posts)


@blog_bp.route("/post/<int:post_id>")
def show_post(post_id):
    form = CommentForm()
    requested_post = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == post_id)
    ).scalar()
    return render_template("post.html", post=requested_post, comment_form=form)


@blog_bp.route("/comment/<int:post_id>", methods=["POST"])
@login_required
def comment(post_id):
    form = CommentForm()
    post = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == post_id)
    ).scalar()
    if form.validate_on_submit():
        comment = Comment(
            text=form.text.data,
            author=current_user,
            post=post,
        )
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for("blog.show_post", post_id=post_id))


@blog_bp.route("/add/", methods=["GET", "POST"])
@admin_required
def add_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data,
            date=date.today().strftime("%B %d, %Y"),
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for("blog.get_all_posts"))

    return render_template("make-post.html", form=form)


@blog_bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
@admin_required
def edit_post(post_id):
    post = db.session.get(BlogPost, post_id)

    if not post:
        flash("Post not found.", "danger")
        return redirect(url_for("blog.get_all_posts"))

    form = BlogPostForm(
        title=post.title,
        subtitle=post.subtitle,
        body=post.body,
        author=post.author,
        img_url=post.img_url,
    )

    if form.validate_on_submit():

        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.body.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        post.date = date.today().strftime("%B %d, %Y")

        db.session.commit()

        flash("Post updated successfully!", "success")
        return redirect(url_for("blog.show_post", post_id=post.id))

    return render_template("make-post.html", form=form, is_edit=True)


@blog_bp.route("/delete/<int:id>")
@admin_required
def delete_post(id):
    post = db.session.get(BlogPost, id)

    if post is None:
        flash("Post not found.", "danger")
        return redirect(url_for("blog.get_all_posts"))

    db.session.delete(post)
    db.session.commit()

    flash(f"Post '{post.title}' deleted successfully!", "success")
    return redirect(url_for("blog.get_all_posts"))


@blog_bp.route("/about")
def about():
    return render_template("about.html")


@blog_bp.route("/contact", methods=["POST", "GET"])
@login_required
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        mail_text = f"""
        Name : {name}
        Email : {email}
        Phone : {phone}
        Message : {message}
        """
        send_mail("Blog contact request", mail_text)

        return render_template(
            "contact.html", message="Message Has been sent successfully"
        )
    return render_template("contact.html")
