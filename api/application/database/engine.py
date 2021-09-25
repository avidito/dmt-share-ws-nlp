from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def session_factory(username, password, hostname, port, database):
    db_uri = f"postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}"
    db_engine = create_engine(db_uri)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

    def get_db():
        db = Session()
        try:
            yield db
        finally:
            db.close()

    return get_db
