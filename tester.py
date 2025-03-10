import requests

API_URL = "http://127.0.0.1:5000/predict" 

test_data = {
    "Gender": "Female",
    "Married": "Married",
    "ApplicantIncome": 60000,
    "LoanAmount": 200000,
    "Credit_History": 0.0
}

# Send  post request programatically

response = requests.post(API_URL, json = test_data)


print(response.status_code)

print(response.json())