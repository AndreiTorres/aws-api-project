from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
db_name = os.getenv('db_name')
db_host = os.getenv('db_host')

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@{db_host}/{db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

MySQLCon = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()
