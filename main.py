# just testing
from database.database import engine, Base
from repositories.user_repo import UserRepo
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()
    repo = UserRepo(session=session)

    repo.register_user("xongs@gmail.com", "asdas#$32e", "xongs")
    print(repo.get_by_email("xongs@gmail.com"))  
