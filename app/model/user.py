from pydantic import BaseModel

class User(BaseModel):
    id : str = None
    name: str
    phone : str = None
    age : int
    mail : str = None

    def to_dict(self):
        return self.dict()

    def from_dict(spec:dict):
        return User.parse_obj(spec)