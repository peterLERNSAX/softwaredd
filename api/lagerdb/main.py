"""main"""

from .models.models import Base
from sqlalchemy.orm import sessionmaker
from .engine import engine


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()