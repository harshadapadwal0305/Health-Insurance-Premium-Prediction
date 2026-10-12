# Health Insurance Premium Prediction

## About the Project

This project predicts health insurance charges based on personal and lifestyle factors using Machine Learning.

The application is built using Python, Scikit-learn, and Streamlit.

## Features

- Predicts insurance charges based on user inputs.
- Uses Linear Regression for prediction.
- Provides an interactive web interface.
- Includes a Jupyter Notebook for data analysis, model training, and evaluation.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Input Features

- Age
- Sex
- BMI
- Number of children
- Smoking status

## Project Files

- `app_HI.py` — Streamlit web application
- `health_insurance.ipynb` — Jupyter Notebook
- `Health_insurance.csv` — Dataset
- `HI_model.pkl` — Trained machine learning model

## How to Run

1. Install the required libraries:

   ```bash
   pip install streamlit pandas scikit-learn
   ```

2. Run the application:

   ```bash
   python -m streamlit run app_HI.py
   ```

## Model Evaluation

The model is evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² score.

## Disclaimer

This project is for educational purposes only. Predictions are estimates and should not be treated as actual insurance quotations.
