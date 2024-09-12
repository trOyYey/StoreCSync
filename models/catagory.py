#!/usr/bin/python3
""" holds class catagory"""
import models
from models.base_model import BaseModel, Base
from models.company import Company
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Catagory(BaseModel, Base):
    """Representation of catagory """
    if models.storage_t == "db":
        __tablename__ = 'catagories'
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        companies = relationship("Company", backref="catagory")
    else:
        name = ""
        description = ""

    def __init__(self, *args, **kwargs):
        """initializes catagory"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def companies(self):
            """getter for list of company instances related to the catagory"""
            company_list = []
            all_companies = models.storage.all(Company)
            for company in all_companies.values():
                if company.catagory_id == self.id:
                    company_list.append(company)
            return company_list
