from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model and the scaler
model = pickle.load(open('model/model_knn.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    try:
        age = int(request.form['Age'])
        sex = 1 if request.form['Sex'] == 'M' else 0  # Convert to numerical value
        chest_pain_type = request.form['ChestPainType']
        resting_bp = int(request.form['RestingBP'])
        cholesterol = int(request.form['Cholesterol'])
        fasting_bs = int(request.form['FastingBS'])
        resting_ecg = request.form['RestingECG']
        max_hr = int(request.form['MaxHR'])
        exercise_angina = 1 if request.form['ExerciseAngina'] == 'Y' else 0
        oldpeak = float(request.form['Oldpeak'])
        st_slope = request.form['ST_Slope']

        # Convert categorical variables to numerical
        chest_pain_type = {'TA': 0, 'ATA': 1, 'NAP': 2, 'ASY': 3}[chest_pain_type]
        resting_ecg = {'Normal': 0, 'ST': 1, 'LVH': 2}[resting_ecg]
        st_slope = {'Up': 0, 'Flat': 1, 'Down': 2}[st_slope]

        # Create feature array and scale it
        features = np.array([[age, sex, chest_pain_type, resting_bp, cholesterol,
                              fasting_bs, resting_ecg, max_hr, exercise_angina,
                              oldpeak, st_slope]])
        scaled_features = scaler.transform(features)

        # Make a prediction
        prediction = model.predict(scaled_features)

        # Interpret prediction
        result = 'Heart Disease Detected' if prediction[0] == 1 else 'No Heart Disease'

    except Exception as e:
        return render_template('result.html', result=f"Error: {str(e)}")

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)