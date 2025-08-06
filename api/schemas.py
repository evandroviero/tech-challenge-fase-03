from typing import Optional
from pydantic import BaseModel

class HouseSchema(BaseModel):
    city: str
    area: int
    rooms: Optional[int] = 0
    bathroom: Optional[int] = 0
    parking_spaces: Optional[int] = 0
    floor: Optional[int] = 0
    animal: Optional[int] = 0
    furniture: Optional[int] = 0
    hoa: Optional[int] = 0
    rent_amount: Optional[int] = 0
    property_tax: Optional[int] = 0
    fire_insurance: Optional[int] = 0

class HousePublic(BaseModel):
    id: int
    city: str
    area: int
    rooms: int = 0
    bathroom: int = 0
    parking_spaces: int = 0
    floor: int = 0
    animal: int = 0
    furniture: int = 0
    hoa: int = 0
    rent_amount: int = 0
    property_tax: int = 0
    fire_insurance: int = 0

class HousePartialUpdate(BaseModel):
    city: Optional[str] = None
    area: Optional[int] = None
    rooms: Optional[int] = None
    bathroom: Optional[int] = None
    parking_spaces: Optional[int] = None
    floor: Optional[int] = None
    animal: Optional[int] = None
    furniture: Optional[int] = None
    hoa: Optional[int] = None
    rent_amount: Optional[int] = None
    property_tax: Optional[int] = None
    fire_insurance: Optional[int] = None

class HouseList(BaseModel):
    houses: list[HousePublic]

