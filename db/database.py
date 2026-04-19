from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Connection string format: dialect+driver://username:password@host:port/database
# For SQLite: sqlite:///example.db
uri = "sqlite:///db/test.db"
engine = create_engine(
    uri,
    connect_args={"check_same_thread": False} # sqlite
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    except  Exception:
        session.rollback()
        raise
    finally:
        session.close()


