import requests


def get_blog():
    url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(url)
    blogs = response.json()

    return blogs


posts = get_blog()
print(posts)
for post in posts:
    print(post["id"], " ", post["title"], " ", post["subtitle"])
