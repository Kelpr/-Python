from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    """ Модель заметки для бд.

    Атрибуты:
    id - идентификатор заметки
    title - заголовок заметки
    content - содержание заметки
    """
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text)

    def __repr__(self):
        return f"<Note(id='{self.id}', title='{self.title}', content='{self.content}')>"

