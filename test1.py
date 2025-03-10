from flask import Flask, request
import pickle  

app = Flask(__name__)

# Load the model
with open("random_forest.pkl", "rb") as model_file:
    clf = pickle.load(model_file)

@app.route("/ping", methods=["GET"])
def ping():
    return {"message": "Hi there, this is the ping API endpoint"}

@app.route("/predict", methods=["POST"])
def prediction():
    # Get JSON data
    loan_req = request.get_json()

    # Extract features safely
    Gender = 0 if loan_req.get('Gender') == "Male" else 1
    Married = 0 if loan_req.get('Married') == "Unmarried" else 1
    Credit_History = 0 if loan_req.get("Credit_History") == "Unclear Debts" else 1
    ApplicantIncome = loan_req.get("ApplicantIncome", 0)
    LoanAmount = loan_req.get("LoanAmount", 0)

    # Ensure proper input format for the model
    input_features = [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]]
    
    # Make prediction
    result = clf.predict(input_features)[0]  # Extracting first element

    pred = "Approved" if result == 1 else "Rejected"

    return {"Loan_approval_status": pred}

if __name__ == "__main__":
    app.run(debug=True)
