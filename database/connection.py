from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///library.db"

engine = create_engine(
    DATABASE_URL,
    echo=False
)