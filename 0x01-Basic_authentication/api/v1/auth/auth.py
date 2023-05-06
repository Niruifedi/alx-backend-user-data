#!/usr/bin/env python3
"""
Authentication Module
"""
from flask import request
from typing import (
    List,
    TypeVar)


class Auth():
    """
    Class for Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        public method to get authentication
        returns false
        """
        if not excluded_paths:
            return True
        if not path:
            return True

        for i in excluded_paths:
            if i.startswith(path):
                return False
            if path.startswith(i):
                return False
            if i[-1] == "*":
                if path.startswith(i[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        public method for auth header
        """
        if request is None:
            return None

        if "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        public method for current user authenticated
        """
        return request
