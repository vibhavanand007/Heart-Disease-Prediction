# Heart Disease Prediction Project

## Project Overview

The Heart Disease Prediction project aims to utilize machine learning techniques to analyze patient data and predict the likelihood of heart disease. This project is designed to assist healthcare professionals in making informed decisions by providing a user-friendly interface for data input and result visualization.

## Key Features

- **Data Processing:** The model processes several patient features, including:
  - **Age**
  - **Sex**
  - **Chest Pain Type**
  - **Resting Blood Pressure**
  - **Cholesterol**
  - **Fasting Blood Sugar**
  - **Resting ECG Results**
  - **Maximum Heart Rate**
  - **Exercise Angina**
  - **Oldpeak**
  - **ST Slope**
  
- **Model Training:** 
  - The project employs a **StandardScaler** to normalize the feature values, ensuring that all input data is on a similar scale. This step is crucial for many machine learning algorithms to perform optimally, as it helps improve convergence speed during model training.
  - Various machine learning algorithms are explored, including:
    - **Logistic Regression**: For its simplicity and effectiveness in binary classification tasks.
    - **Decision Trees**: To capture non-linear relationships in the data.
    - **K-Nearest Neighbors (K-NN)**: Used for its instance-based learning approach.
    - **Gaussian Naive Bayes**: Applied for probabilistic classification based on Bayes' theorem.

    - **Support Vector Machines (SVM)**: To find the optimal hyperplane for classification.
  - Hyperparameter tuning is conducted using techniques such as **Grid Search** and **Cross-Validation** to identify the best model parameters. This ensures that the model is fine-tuned for maximum performance.
  - The final model is evaluated based on various metrics, including **accuracy**, **precision**, **recall**, and **F1-score**, to ensure it meets the necessary standards for clinical application.

- **User Interface:** A responsive web application is developed using Flask, HTML, and CSS. It allows users to easily input data and receive predictions. Each input feature includes notes with detailed descriptions to guide users in providing accurate information.

- **Target Variable:** The target column for prediction is **Heart Disease**, enabling the model to identify the likelihood of heart disease based on the provided input features.

## Live Demo

You can try the Heart Disease Prediction model by visiting the following link: [Try it](https://heart-disease-prediction-sglb.onrender.com)

## Conclusion

This project contributes to the early detection of heart disease, promoting proactive healthcare measures and improving patient outcomes. By utilizing advanced machine learning techniques, it aims to support healthcare professionals in delivering better patient care.
