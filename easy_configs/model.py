from sqlmodel import Field, SQLModel,create_engine
from sqlmodel import Session
class ConfigMeta(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

    
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    return Session(engine)