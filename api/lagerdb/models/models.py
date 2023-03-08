"""Models File"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from ..engine import engine
#from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Layout(Base):
    "DB Model for Layout File"
    __tablename__ = "layout"

    id = Column(Integer,primary_key=True)
    pdf_text = Column(String)

class OfferFile(Base):
    """DB Model for Offer File"""
    __tablename__ = "offerfile"

    id = Column(Integer,primary_key=True)
    pdf_text = Column(String)

class Offer(Base):
    """DB model for offer"""

    __tablename__ = "offer"

    id = Column(Integer,primary_key=True)
    customer = Column(Integer,ForeignKey("customer.id"), nullable=True)
    offer_file = Column(Integer, ForeignKey("offerfile.id"), nullable=True)
    layout = Column(Integer,ForeignKey("layout.id"),nullable=True)
    description = Column(String,nullable=True)


class Hardware(Base):
    """DB Model for Hardware"""

    __tablename__ = "hardware"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    descripption = Column(String,nullable=True)
    size = Column(String,nullable=True)
    weight = Column(Float,nullable=True)
    cable_length = Column(Float,nullable=True)
    power_consumption = Column(Float,nullable=True)
    workplace_ergonomics = Column(String,nullable=True)

class Customer(Base):
    """Customer"""

    __tablename__ = "customer"

    id = Column(Integer,primary_key=True)
    firstname = Column(String,nullable=False)
    sirname = Column(String,nullable=False)
    email = Column(String,nullable=False)
    compay_name = Column(String,nullable=True)


