#!/usr/bin/env python3
"""
Class for Basic Authentication
"""
from .auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """
        this method return the decode value of base64 string
        """
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except TypeError:
            return None
