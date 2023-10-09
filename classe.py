from fastapi import Form
from pydantic import BaseModel

class Car(BaseModel):

    Present_Price: float
    Kms_Driven: int
    Owner:int
    Year:int
    Fuel_Type_Petrol:str
    Seller_Type_Individual:str
    Transmission_Mannual: str


    @classmethod
    def as_form(
            cls,
            Present_Price: float = Form(...),
            Kms_Driven: int = Form(...),
            Owner:int = Form(...),
            Year:int = Form(...),
            Fuel_Type_Petrol:str = Form(...),
            Seller_Type_Individual:str = Form(...),
            Transmission_Mannual: str = Form(...),
        ):
            return cls(
                Present_Price=Present_Price,
                Kms_Driven= Kms_Driven,
                Owner=Owner,
                Year=Year,
                Fuel_Type_Petrol=Fuel_Type_Petrol,
                Seller_Type_Individual=Seller_Type_Individual,
                Transmission_Mannual=Transmission_Mannual
            )