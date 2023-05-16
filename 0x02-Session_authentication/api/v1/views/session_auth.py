#!/usr/bin/env python3
"""
Module for session Auth views
"""
from flask import jsonify, request
import os
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """
    method for session login
    """
    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({'error': 'email missing'}), 400
    pwd = request.form.get('password')
    if pwd is None or pwd == "":
        return jsonify({'error': 'password missing'}), 400

    users = User.search({"email": email})

    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(pwd):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            resp = jsonify(user.to_json())
            session_name = os.getenv('SESSION_NAME')
            resp.set_cookie(session_name, session_id)
            return resp
    return jsonify({"error": "wrong password"}), 401

@app_views.route('/api/v1/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """
    method for session Logout
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
