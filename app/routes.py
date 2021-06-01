#!/usr/bin/env python3
"""HTTP route definitions"""

from flask import request
from app import app # from the app package import the app variable
from app.database import(
    create,
    scan,
    update_user,
    delete_user
)

@app.route("/users", methods=["POST"]) # decorator
def create_user():                      # view functions
    user_data = request.json
    new_id = create(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    return{
    "ok": True,
    "message": "success",
    "new_id": new_id
    }


@app.route("/users", methods=["GET"])
def get_all_users():
    users = scan()
    return{
        "ok": True,
        "message": "Success",
        "users": users
    }



@app.route("/remove/<int:user>", methods=["POST"])
def delete(user):
    delete_user(user)
    return "%s was deleted." % user


@app.route("/update/<int:user>/<key>/<val>")
def update(val, key, user):
    update_user(val, key, user)
    return "The %s in %s was updated for %s" % val, key, user


@app.route('/square/<int:number>')
def square(number):
    return ("<h1>%s squared is %s</h1>"
            % (number, number**2))

        
@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent