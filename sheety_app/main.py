import requests
from datetime import datetime
import os

# Your Personal Information
GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 168
AGE = 32

# Nutrition Environment Variables.
APP_ID = os.environ.get("ENV_NIX_APP_ID")
API_KEY = os.environ.get("ENV_NIX_API_KEY")

# Sheety Sheets Environment Variables.
SHEETY_TOKEN = os.environ.get("ENV_SHTY_TOKEN")

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

nutri_json = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutri_json, headers=headers)
response.raise_for_status()

exercises = response.json()["exercises"]

sheety_endpoint = "https://api.sheety.co/e212c0fbfcbbc2c92d49c6bd84d7293c/workoutTracking/workouts"
formatted_date = datetime.now().date()
formatted_time = datetime.now().time()

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
for exercise in exercises:
    sheety_payload = {
        "workout": {
            "date": f"{formatted_date.strftime('%d/%m/%Y')}",
            "time": f"{formatted_time.strftime('%H:%M:%S')}",
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_payload, headers=sheety_headers)
    print(sheety_response.json())
