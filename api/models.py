from sqlalchemy import Column, Integer, String

from api.database import Base


class House(Base):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    area = Column(Integer, nullable=False)
    rooms = Column(Integer, default=0)
    bathroom = Column(Integer, default=0)
    parking_spaces = Column(Integer, default=0)
    floor = Column(Integer, default=0)
    animal = Column(Integer, index=True, default=0)
    furniture = Column(Integer, index=True, default=0)
    hoa = Column(Integer, default=0)
    rent_amount = Column(Integer, default=0)
    property_tax = Column(Integer, default=0)
    fire_insurance = Column(Integer, default=0)
