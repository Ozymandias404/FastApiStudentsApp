from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_urls = {"prod": "postgresql+psycopg://postgres:mysecretpassword@localhost:5432/template1",
           "test": "postgresql+psycopg://postgres:mysecretpassword@localhost:5432/test"}

SQLALCHEMY_DATABASE_URL = db_urls["test"]

db_meta = MetaData()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()