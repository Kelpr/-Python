from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Создание движка базы данных с использованием SQLite
engine = create_engine('sqlite:///notes.db')
Session = sessionmaker(bind=engine)

def init_db():
    """ Инициализация бд, создание таблиц. """
    Base.metadata.create_all(engine)
