from fastapi import APIRouter, Depends, HTTPException, status
import joblib
import pandas as pd
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.database import get_session
from api.models import House
from api.schemas import HouseList, HousePartialUpdate, HousePublic, HouseSchema, PredictSchema

router = APIRouter(
    prefix="/api/v1/houses",
    tags=["houses"],
)

RENT_MODEL = joblib.load("model/rent_model.pkl")

@router.post(
    path="register/",
    summary="Create a new house",
    response_description="The created house",  
    status_code=status.HTTP_201_CREATED,
    response_model=HousePublic,
)
def create_house(house: HouseSchema, 
                 session: Session = Depends(get_session)):
    house = House(**house.model_dump())
    session.add(house)
    session.commit()
    session.refresh(house)
    return house

@router.get(
    path="register/",
    summary="List all houses",
    response_description="A list of houses",
    response_model=HouseList,
    status_code=status.HTTP_200_OK,
)
def list_houses(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
    query = session.scalars(select(House).offset(offset).limit(limit))
    houses = query.all()
    return {"houses": houses}

@router.get(
    path="register/{house_id}",
    summary="List a house by ID",
    response_description="A house by ID",
    response_model=HousePublic,
    status_code=status.HTTP_200_OK,
)
def get_house(house_id: int, session: Session = Depends(get_session)):
    query = session.get(House, house_id)
    if not query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="House not found") 
    return query

@router.put(
    path="register/{house_id}",
    summary="Update a house by ID",
    response_description="The updated house",
    response_model=HousePublic,
    status_code=status.HTTP_201_CREATED,
)
def update_house(house_id: int, 
                 house: HouseSchema, 
                 session: Session = Depends(get_session)):
    query = session.get(House, house_id)
    if not query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="House not found")
    
    for field, value in house.model_dump().items():
        setattr(query, field, value)
    
    session.commit()
    session.refresh(query)
    return query

@router.patch(
    path="register/{house_id}",
    summary="Partially update a house by ID",
    response_description="The updated house",
    response_model=HousePublic,
    status_code=status.HTTP_201_CREATED,
)
def patch_house(house_id: int, 
                house: HousePartialUpdate, 
                session: Session = Depends(get_session)):
    query = session.get(House, house_id)
    if not query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="House not found")
    update_data = {k: v for k, v in house.model_dump(exclude_unset=True).items()}
    for field, value in update_data.items():
        setattr(query, field, value)
    
    session.commit()
    session.refresh(query)
    return query

@router.delete(
    path="register/{house_id}",
    summary="Delete a house by ID",
    response_description="A message confirming deletion",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_house(house_id: int, session: Session = Depends(get_session)):
    query = session.get(House, house_id)
    if not query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="House not found")
    session.delete(query)
    session.commit()


@router.post(
    path="predict/",
    summary="Predict rental cost based on property features",
    response_description="Predicted rental cost",  
    status_code=status.HTTP_200_OK,
)
def predict_rent(house: PredictSchema, session: Session = Depends(get_session)):
    input_data = pd.DataFrame([house.model_dump()])
    predicted_rent = float(RENT_MODEL.predict(input_data)[0])
    house_db = House(**house.model_dump(), rent_amount=predicted_rent)
    
    session.add(house_db)
    session.commit()
    session.refresh(house_db)
    return {"predicted_rent": predicted_rent}