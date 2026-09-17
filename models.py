from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Robot(Base):
  __tablename__ = "robots"
  id = Column(Integer, primary_key=True)
  name = Column(String)
  x = Column(Float)
  y = Column(Float)
  battery_pct = Column(Float)
  status = Column(String)
  updated_at = Column(DateTime)

from sqlalchemy import create_engine
engine = create_engine("sqlite:///robots.db")

Base.metadata.create_all(engine)

from sqlalchemy import inspect

inspector = inspect(engine)
print(inspector.get_table_names())
