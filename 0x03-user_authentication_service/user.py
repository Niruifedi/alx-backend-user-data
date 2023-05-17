#!/usr/bin/env python3
"""
User Module
"""
from sqlalchemy import (
    Column,
    Integer,
    String)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    """
    class to create table and map columns
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)