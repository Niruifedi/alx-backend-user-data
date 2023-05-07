#!/usr/bin/env python3
"""
Class for Basic Authentication
"""
from .auth import Auth


class BasicAuth(Auth):
    """
    Basic Authentication Inherits from the Auth Module
    """
    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """
        this public method returns the base64 part of the Authorization header
        """

        if not authorization_header:
            return None

        if not isinstance(authorization_header, str):
            return None

        if authorization_header.startswith('Basic '):
            return authorization_header.split(' ')[1]
        else:
            return None
