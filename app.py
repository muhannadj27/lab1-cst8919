from flask import Flask, render_template, session, redirect, url_for
from authlib.integrations.flask_client import OAuth
from functools import wraps
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=os.getenv("AUTH0_CLIENT_ID"),
    client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
    server_metadata_url=f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/openid-configuration',
    client_kwargs={
        "scope": "openid profile email",
    },
)

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated

@app.route("/")
def home():
    return render_template("home.html", user=session.get("user"))

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/callback")
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token["userinfo"]
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()

    return redirect(
        f"https://{os.getenv('AUTH0_DOMAIN')}/v2/logout"
        f"?returnTo=http://localhost:3000"
        f"&client_id={os.getenv('AUTH0_CLIENT_ID')}"
    )

@app.route("/protected")
@login_required
def protected():
    return render_template(
        "protected.html",
        user=session["user"]
    )

if __name__ == "__main__":
    app.run(port=3000, debug=True)