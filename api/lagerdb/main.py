"""main"""

from sqlalchemy.orm import sessionmaker

from .engine import engine
from .models.models import Base

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
