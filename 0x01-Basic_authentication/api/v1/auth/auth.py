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
        return False

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
