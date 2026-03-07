from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Example decorator
def makebold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

@app.route('/')
def home():
  
    return render_template(
        "index.html",
        user_name="Nischal Chaudhary",
        user_title="AI/ML Enthusiast & Python Developer",
        current_year=datetime.now().year,
        twitter_link="https://twitter.com/existenchal_",
        instagram_link="https://instagram.com/existenchal_",
        facebook_link="#"  # replace with your Facebook link
    )

# Test decorator route
@app.route('/bold')
@makebold
def bold_text():
    return "This text is bolded using a decorator!"

if __name__ == "__main__":
    app.run(debug=True)