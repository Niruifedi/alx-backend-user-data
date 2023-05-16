#!/usr/bin/env python3
"""
Session Auth Module
"""
from .auth import Auth
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
        return str(self.user_id_by_session_id.get(session_id))

    def current_user(self, request=None):
        """
        retrieves and identify user with session id created
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user
    
    def destroy_session(self, request=None):
        """
        this method deletes a user session
        """
        if request is None:
            return False
        _my_session_id = self.session_cookie(request)
        if _my_session_id is None:
            return False
        user_id = self.user_id_for_session_id(_my_session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[_my_session_id]
        return True
