from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHMY_DATABASE_URL = "sqlite:///./cars.db"
engine = create_engine(
    SQLALCHMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def setup_database():
    Base.metadata.create_all(bind=engine)


def get_database():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
