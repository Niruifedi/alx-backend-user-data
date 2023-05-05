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

        # deletes the trailing slash to compare strings
        path = path.rstrip('/')

        for ex_path in excluded_paths:
            if ex_path.rstrip("/") == path:
                return False
            else:
                return True

    def authorization_header(self, request=None) -> str:
        """
        public method for auth header
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """
        public method for current user authenticated
        """
        return request
