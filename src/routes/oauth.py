import time
import urllib
import requests

from flask import redirect, request

import util
import config
from app import app, db
from database import Student

oauth_state = {}

@app.route("/auth/redirect")
def get_redirect():
    state = util.random_string(16)
    epoch = time.time()
    oauth_state[state] = epoch
    print(oauth_state)

    redirect_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={config.client_id}&redirect_uri={urllib.parse.quote_plus(config.external_url)}/auth/complete&response_type=code&scope=profile&state={state}"
    return redirect(redirect_url)


@app.route("/auth/complete")
def get_complete():
    code = request.args.get("code")
    state = request.args.get("state")

    epoch = time.time()
    old_epoch = oauth_state[state]
    del oauth_state[state]

    if epoch - old_epoch > 60:
        return "State expired."

    resp = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "grant_type": "authorization_code",
            "client_secret": config.client_secret,
            "client_id": config.client_id,
            "code": code,
            "redirect_uri": f"{config.external_url}/auth/complete",
        },
    ).json()

    access_token = resp["access_token"]

    user_info = requests.get(
        "https://www.googleapis.com/oauth2/v1/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
    ).json()

    print(user_info)

    id = user_info["id"]
    name = user_info["name"]
    picture = user_info["picture"]

    student = Student.query.filter_by(id=id).first()

    if student:
        return "existing"


    # todo cookie

    db.session.add(Student(id, name, picture))
    db.session.commit()

    return "new"
    # return redirect('/me')
