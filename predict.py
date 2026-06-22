import pandas as pd
import joblib

model = joblib.load("placement_model.pkl")

city = input("Enter city: ")
cgpa = float(input("Enter CGPA: "))
iq = int(input("Enter IQ: "))

new_student = pd.DataFrame({
    "city": [city],
    "cgpa": [cgpa],
    "iq": [iq]
})

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Prediction: Student will be Placed")
else:
    print("Prediction: Student will not be Placed")