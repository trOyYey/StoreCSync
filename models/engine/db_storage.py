#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.company import Company
from models.catagory import Catagory
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"BaseModel": BaseModel, "Company": Company, "Catagory": Catagory}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        SCS_MYSQL_USER = getenv('SCS_MYSQL_USER')
        SCS_MYSQL_PWD = getenv('SCS_MYSQL_PWD')
        SCS_MYSQL_HOST = getenv('SCS_MYSQL_HOST')
        SCS_MYSQL_DB = getenv('SCS_MYSQL_DB')
        SCS_ENV = getenv('SCS_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(SCS_MYSQL_USER,
                                             SCS_MYSQL_PWD,
                                             SCS_MYSQL_HOST,
                                             SCS_MYSQL_DB))
        if SCS_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """return object by class name and id"""
        if cls and id:
            objs = self.all(cls)
            for a in objs:
                if objs[a].id == id:
                    return objs[a]
        return None

    def count(self, cls=None):
        """count method"""
        return (len(self.all(cls)))
