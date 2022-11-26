from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'postgresql://gdhwlficqahlpa:7260b7853dbf90d2e4e56834046cdbd6d402136cafc6fb25c0b53954372813ac@ec2-52-70-45-163.compute-1.amazonaws.com/d1cf63itopno05'


engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
         db.close()
