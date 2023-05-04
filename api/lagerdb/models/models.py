"""Models File"""
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

# from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# pylint:disable=too-few-public-methods
class Layout(Base):
    "DB Model for Layout File"
    __tablename__ = "layout"

    id = Column(Integer, primary_key=True)
    pdf_text = Column(String)


# pylint:disable=too-few-public-methods
class OfferFile(Base):
    """DB Model for Offer File"""

    __tablename__ = "offerfile"

    id = Column(Integer, primary_key=True)
    pdf_text = Column(String)


# pylint:disable=too-few-public-methods
class Offer(Base):
    """DB model for offer"""

    __tablename__ = "offer"

    id = Column(Integer, primary_key=True)
    customer = Column(Integer, ForeignKey("customer.id"), nullable=True)
    offer_file = Column(Integer, ForeignKey("offerfile.id"), nullable=True)
    layout = Column(Integer, ForeignKey("layout.id"), nullable=True)
    description = Column(String, nullable=True)
    hardwware = Column(Integer,ForeignKey("hardware.id"),nullable=True,index=True)


# pylint:disable=too-few-public-methods
class Hardware(Base):
    """DB Model for Hardware"""

    __tablename__ = "hardware"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    size = Column(String, nullable=True)
    weight = Column(Float, nullable=True)
    cable_length = Column(Float, nullable=True)
    power_consumption = Column(Float, nullable=True)
    workplace_ergonomics = Column(String, nullable=True)


# pylint:disable=too-few-public-methods
class Customer(Base):
    """Customer"""

    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    sirname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    company_name = Column(String, nullable=True)
