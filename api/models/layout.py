"""Layout Model"""

# pylint:disable=no-name-in-module
from pydantic import BaseModel


# pylint:disable=too-few-public-methods
class Layout(BaseModel):
    """Layout Model"""

    pdf_text: str
