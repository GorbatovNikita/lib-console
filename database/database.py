from database.connection import engine
from database.models import Base


def initialize_database():
    Base.metadata.create_all(engine)