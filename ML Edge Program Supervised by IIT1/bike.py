Ofrom pydantic import BaseModel


class UserInfo(BaseModel):
    userName: str
    userID: str


class Bike(BaseModel):
    VendorName: str
    cc: int
    price: float
    person_details: UserInfo
