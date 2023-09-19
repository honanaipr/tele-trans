from pydantic import BaseModel, Field, ConfigDict

class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class User(Base):
    first_name: str
    last_name: str = ""
    id: int
    
