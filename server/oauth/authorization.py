from flask_dance.contrib.google import google
from db.mongo import store_in_db   
from flask import (
    redirect, 
    url_for
)


def check_if_auth():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    data = resp.json()
    print(data)
    store_in_db(data)
    return redirect("http://localhost:3000")