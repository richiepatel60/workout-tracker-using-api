import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = 74
HEIGHT_CM = 177
AGE = 19

# For Nutrionx api
NUTRIONX_APP_ID = "9c198b0f"
NUTRIONX_API_KEY = "0ae90c0558311f1fac384f0f5888e8e2"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

nutrionx_headers = {
    "x-app-id": NUTRIONX_APP_ID,
    "x-app-key": NUTRIONX_API_KEY,
}
nutrionx_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=exercise_endpoint, json=nutrionx_parameters, headers=nutrionx_headers)
result = response.json()
# print(result)

# For Sheety api
sheety_api_url = "https://api.sheety.co/8b2da98489f46aa9f2340b47a5eadf4b/workoutTracking/workouts"
sheety_api_key = "Basic cmljaGllOnBhdGVsMTA="

sheety_api_headers = {
    "Authorization": sheety_api_key
}

for _ in range(len(result["exercises"])):
    today = datetime.now()
    new_row_data = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": (result["exercises"][_]["name"]).title(),
            "duration": result["exercises"][_]["duration_min"],
            "calories": result["exercises"][_]["nf_calories"],
        }
    }
    response2 = requests.post(url=sheety_api_url, headers=sheety_api_headers, json=new_row_data)
    # print(response2.text)




