import time
import urllib
import requests

from flask_jwt_extended import create_access_token
from flask import redirect, request

import util
import config
from app import app, db
from database import Student

AUTH_COOKIE = 'access_token_cookie'
COOKIE_DURATION = 60 * 60 * 24 * 30 # one month by default

oauth_state = {}

@app.route("/auth/redirect")
def get_redirect():
    state = util.random_string(16)
    epoch = time.time()
    oauth_state[state] = epoch

    redirect_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={config.client_id}&redirect_uri={urllib.parse.quote_plus(config.external_url)}/auth/complete&response_type=code&scope=profile&state={state}"
    return redirect(redirect_url)

@app.route("/auth/logout")
def get_logout():
    resp = redirect('/')
    resp.set_cookie(AUTH_COOKIE, '', expires=0)
    return resp

@app.route("/auth/complete")
def get_complete():
    # Get the oauth code and state from the query parameters
    code = request.args.get("code")
    state = request.args.get("state")

    # Ensure the state has not expired and remove it so it can't be used again
    epoch = time.time()
    old_epoch = oauth_state[state]
    del oauth_state[state]

    if epoch - old_epoch > 60:
        return "State expired."

    # Ask Google oauth services for a Google api access token
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

    # Get basic user information
    user_info = requests.get(
        "https://www.googleapis.com/oauth2/v1/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
    ).json()

    id = user_info["id"]
    name = user_info["name"]
    picture = user_info["picture"]

    # Insert / update the database with student name and picture
    session = create_access_token(identity=id)
    student = Student.query.filter_by(id=id).first()

    if student:
        student.name = name
        student.picture = picture
    else:
        db.session.add(Student(id, name, picture))
    
    db.session.commit()

    # Redirect to /me with the session token stored as a cookie
    response = redirect('/me')
    response.set_cookie(AUTH_COOKIE, session, max_age=COOKIE_DURATION)
    return response
