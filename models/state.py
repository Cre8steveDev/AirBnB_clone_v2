#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if storage_type == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    if storage_type != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
