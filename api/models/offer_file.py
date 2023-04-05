"""offer-file"""

# pylint:disable=no-name-in-module
from pydantic import BaseModel


# pylint:disable=too-few-public-methods
class Offer(BaseModel):
    """Offer File"""

    pdf_string: str
