import logging

from flask_dance.contrib.google import google
from settings import InfoMsgs
from db.mongo import store_in_db   
from flask import (
    redirect, 
    url_for
)


def check_if_auth():
    logging.basicConfig(format='%(asctime)s %(message)s')

    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get('/oauth2/v2/userinfo')
    if not resp.ok or not resp.text:
        logging.info(InfoMsgs.unsuccessful_login)
        return redirect(url_for("google.login"))

    data = resp.json()

    logging.info(InfoMsgs.authorized_user.format(name=data['name'], email=data['email']))

    store_in_db(data)

    return redirect("http://localhost:3000")