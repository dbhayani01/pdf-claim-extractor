from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# SQLite DB file
DATABASE_URL = "sqlite:///claims.db"
# SQLAlchemy setup
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Claim table schema
class Claim(Base):
   __tablename__ = "claims"
   id = Column(Integer, primary_key=True, index=True)
   client_name = Column(String, nullable=True)
   contact_name = Column(String, nullable=True)
   incident_details = Column(String, nullable=True)
   vehicle = Column(String, nullable=True)
   insured_name = Column(String, nullable=True)
   incident_description = Column(String, nullable=True)
   claim_type = Column(String, nullable=True)
# Create tables
Base.metadata.create_all(bind=engine)
