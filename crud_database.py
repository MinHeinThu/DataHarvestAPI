from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from fastapi import HTTPException

# Secure loading
load_dotenv() # # This line loads the .env file and sets the environment variables

# connect with psql 
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Check the database if not show database not found message 
if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("Error: Database misconfiguration")

# Create SQlAlchemy 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for model 
Base = declarative_base()