from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import os

Base = declarative_base()

class TranslationRequest(Base):
    __tablename__ = "translation_requests"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    languages = Column(String, nullable=False)
    status = Column(String, default="in progress", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class TranslationResult(Base):
    __tablename__ = "translation_results"
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("translation_requests.id"), nullable=False)
    language = Column(String, nullable=False)
    translated_text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class IndividualTranslations(Base):
    __tablename__ = "individual_translations"
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("translation_requests.id"), nullable=False)
    translated_text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# to ensure tables are created in the database
engine_url = os.getenv("DATABASE_URL")
engine = create_engine(engine_url)
Base.metadata.create_all(engine)