from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database/sqlalchemy_example.db')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
