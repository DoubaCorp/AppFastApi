from fastapi import FastAPI , Request, Form, Depends
from fastapi.templating import Jinja2Templates
#from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
from classe import Car
import pickle
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model = pickle.load(open('modelregress.pkl','rb'))

@app.get("/", response_class=HTMLResponse)

async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/predict')
async def predict(form_data: Car = Depends(Car.as_form), request: Request=None):
    Fuel_Type_Diesel = 0
    Present_Price = form_data.Present_Price
    Kms_Driven = form_data.Kms_Driven
    Kms_Driven2 = np.log(Kms_Driven)
    Owner = form_data.Owner
    Year = form_data.Year
    Fuel_Type_Petrol = form_data.Fuel_Type_Petrol
    if (Fuel_Type_Petrol == 'Petrol'):
        Fuel_Type_Petrol = 1
        Fuel_Type_Diesel = 0
    else:
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 1
    Year = 2020 - Year
    Seller_Type_Individual = form_data.Seller_Type_Individual
    if (Seller_Type_Individual == 'Individual'):
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0
    Transmission_Mannual = form_data.Transmission_Mannual
    if (Transmission_Mannual == 'Mannual'):
        Transmission_Mannual = 1
    else:
        Transmission_Mannual = 0

    prediction = model.predict([[Present_Price, Kms_Driven2, Owner, Year,Fuel_Type_Diesel,
                                 Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
    output = round(prediction[0], 2)
    prediction_texts = "Sorry you cannot sell this car !"
    prediction_text = "You Can Sell The Car at Rs. {} Lakhs".format(output)
    if output < 0:
        return templates.TemplateResponse('index.html', {"request": request, "prediction_text": prediction_texts})
    else:
        return templates.TemplateResponse('index.html', {"request": request, "prediction_text": prediction_text})


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)




