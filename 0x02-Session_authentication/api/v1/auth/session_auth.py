#!/usr/bin/env python3
"""
Session Auth Module
"""
import base64
from .auth import Auth
from typing import TypeVar
from models.user import User


class SessionAuth(Auth):
    """
    session auth inherits authentication from the base Auth
    """
    pass
