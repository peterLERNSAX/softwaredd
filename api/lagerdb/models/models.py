"""Models File"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
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
    __tablename__ = "offer"

    id = Column(Integer,primary_key=True)
    pdf_text = Column(String)


