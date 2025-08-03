#  Mental-Health-Prediction-MLApp

A machine learning-powered web application designed to **predict mental health risk levels** (Low, Medium, High) based on user inputs. This tool can be useful in **mental health screening**, awareness, and educational purposes, built using Python, Streamlit, and popular ML models like **RandomForest** and **XGBoost**.


## 📌 Project Overview

Mental health is a critical component of overall well-being. This app enables users to input basic health-related data and get a predicted **mental health risk level**. The model was trained on a dataset including factors like:

- Age  
- Sleep Hours  
- Stress Level  
- Anxiety Score  
- and more...

The app was built with the following goals:
- Early identification of mental health risks
- Simple and interactive UI for accessibility
- Demonstrate ML model training and deployment with real data



## 📂 Dataset

The dataset used for training includes the following features:
- `age`, `gender`, `employment_status`, `work_environment`
- `mental_health_history`, `seeks_treatment`, `stress_level`
- `sleep_hours`, `physical_activity_days`, `depression_score`
- `anxiety_score`, `social_support_score`, `productivity_score`

Target label: **`mental_health_risk`** (Low, Medium, High)

Dataset size: **10,000 rows × 14 columns**


##  Model & Training

The app uses a classification model trained using:

- Preprocessing with `StandardScaler`
- Label encoding for categorical data
- `RandomForestClassifier` (with option to switch to `XGBoostClassifier`)
- Accuracy ~59.6% (baseline, can be improved with more tuning or features)

Trained model is saved as: `model.pkl`  
Scaler object saved as: `scaler.pkl` (optional if used)

Training script: `train_model.py`  
Prediction logic: `app.py` and `mental_health.py`


## Streamlit App

The web app is powered by [Streamlit](https://streamlit.io/). It provides a slider-based input form for:

- Age (10–100)
- Stress Level (1–10)
- Sleep Hours (0–24)
- Anxiety Score (1–10)

Prediction is shown in real time after clicking the **"Predict"** button.


## Sample Screenshot

Prediction Result
<img width="1903" height="927" alt="image" src="https://github.com/user-attachments/assets/ab6381ff-2733-4915-b612-4639df2f6fbb" />

Train Model Accuracy
<img width="1112" height="515" alt="image" src="https://github.com/user-attachments/assets/e89cbf89-e375-4233-bd6d-75de6a67ef07" />



## ⚙️ Installation

```bash
# Clone this repository
git clone https://github.com/mahamudul-hasan-cse/Mental-Health-Prediction-MLApp.git
cd Mental-Health-Prediction-MLApp

# Optional: Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate       # For Windows

# Install all required libraries
pip install -r requirements.txt


# Project Structure
Mental-Health-Prediction-MLApp
├── app.py                     # Streamlit app
├── mental_health.py           # Prediction function
├── train_model.py             # Model training logic
├── model.pkl                  # Saved ML model
├── mental_health_dataset.csv  # Dataset
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation


# License

This project is licensed under the MIT License.
You are free to use, modify, and distribute with attribution.

#🙋‍♂️ Author

GitHub: @mahamudul-hasan-cse
