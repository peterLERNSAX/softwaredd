"""offer-file"""

from pydantic import BaseModel

class Offer(BaseModel):
    """Offer File"""
    pdf_string: str
    