from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

##### Schema: WS #####
class ScrapingResult(Base):
    __tablename__  = "scraping_result"
    __table_args__ = {"schema": "ws"}

    title = Column(String, primary_key=True)
    website = Column(String)
    channel = Column(String)
    category = Column(String)
    native_category = Column(String)
    url = Column(String)
    load_dt Column(DateTime)
