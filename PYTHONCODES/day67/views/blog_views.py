from flask import Blueprint, render_template, redirect, url_for, flash
from extensions import db
from models import BlogPost
from forms import BlogPostForm
from datetime import date

blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/")
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    all_posts = result.scalars().all()
    return render_template("index.html", all_posts=all_posts)


@blog_bp.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == post_id)
    ).scalar()
    return render_template("post.html", post=requested_post)


@blog_bp.route("/add/", methods=["GET", "POST"])
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


@blog_bp.route("/contact")
def contact():
    return render_template("contact.html")
