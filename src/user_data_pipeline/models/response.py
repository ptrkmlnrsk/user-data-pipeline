from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    username: str
    email: str
    company: Company


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catch_phrase: str
    bs: str


class Geo(BaseModel):
    lat: str
    lon: str


# user = User.model_validate()
