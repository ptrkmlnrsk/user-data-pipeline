from pydantic import BaseModel, Field


class Geo(BaseModel):
    lat: float = Field(ge=-90, le=90)
    lng: float = Field(ge=-180, le=180)  # automatyczne konwertowanie na float


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class UserResponse(BaseModel):
    id: int = Field(strict=True)
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company
