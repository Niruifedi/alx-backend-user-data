#!/usr/bin/env python3
"""
Session Auth Module
"""
import base64
from .auth import Auth
from typing import TypeVar
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """
    session auth inherits authentication from the base Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        method to create a session for a user id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        else:
            sess_id = uuid4()
            self.user_id_by_session_id[str(sess_id)] = user_id
            return str(sess_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        this method returns a user id based on session id
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
