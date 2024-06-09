import requests
import os
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 17000
AGE = 21

APP_ID = os.environ["NUTRITIONIX_APP_ID"]
API_KEY = os.environ["NUTRITIONIX_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()


SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

TOKEN = os.environ["TOKEN"]

# Bearer Token Authentication
bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
