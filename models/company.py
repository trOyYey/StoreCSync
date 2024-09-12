#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Company(BaseModel, Base):
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'companies'
        catagory_id = Column(String(60), ForeignKey('catagories.id'), nullable=False)
        name = Column(String(128), nullable=False)
        href = Column(String(1024), nullable=True)
    else:
        catagory_id = ""
        name = ""
        href = ""

    def __init__(self, *args, **kwargs):
        """initializes company"""
        super().__init__(*args, **kwargs)
