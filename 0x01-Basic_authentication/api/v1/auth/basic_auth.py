#!/usr/bin/env python3
"""
Class for Basic Authentication
"""
from .auth import Auth
import base64
from typing import TypeVar
from models.user import User


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
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str)\
            -> (str, str):
        """
        method returns user email and password from base64 to decoded value
        """
        if not decoded_base64_authorization_header:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        else:
            email, password = decoded_base64_authorization_header.split(':')
            return email, password

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str)\
            -> TypeVar('User'):
        """
        This method returns theuserinstance basedon his emailand password
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": "user_email"})
            if not users or users == []:
                return None
            for i in users:
                if i.is_valid_password(user_pwd):
                    return i
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        THis method overloads the Auth and retrieves the user instance for a request
        """
        Auth_header = self.authorization_header(request)
        if Auth_header is not None:
            token = self.extract_base64_authorization_header(Auth_header)
            if token is not None:
                decode = self.decode_base64_authorization_header(token)
                if decode is not None:
                    email, pwd = self.extract_user_credentials(decode)
                    if email:
                        return self.user_object_from_credentials(email, pwd)
        return
