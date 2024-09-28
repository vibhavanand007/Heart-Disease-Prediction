# Heart Disease Prediction Project

## Project Overview

The Heart Disease Prediction project aims to utilize machine learning techniques to analyze patient data and predict the likelihood of heart disease. This project is designed to assist healthcare professionals in making informed decisions by providing a user-friendly interface for data input and result visualization.

## Key Features

- **Data Processing:** The model processes several patient features, including:
  - **Age**
  - **Sex**
  - **Chest Pain Type**
  - **Resting Blood Pressure*
  - **Cholesterol**
  - **Fasting Blood Sugar**
  - **Resting ECG Results**
  - **Maximum Heart Rate**
  - **Exercise Angina**
  - **Oldpeak**
  - **ST Slope**
  
- **Model Training:** The project employs a `StandardScaler` on the training dataset to normalize feature values, which enhances the model's performance.

- **User Interface:** A responsive web application is developed using Flask, HTML, and CSS. It allows users to easily input data and receive predictions. Each input feature includes notes with detailed descriptions to guide users in providing accurate information.

- **Target Variable:** The target column for prediction is **Heart Disease**, enabling the model to identify the likelihood of heart disease based on the provided input features.

## Conclusion

This project contributes to the early detection of heart disease, promoting proactive healthcare measures and improving patient outcomes. By utilizing advanced machine learning techniques, it aims to support healthcare professionals in delivering better patient care.
