

# 🎓 Student Performance Predictor

An interactive **Machine Learning + Streamlit** application that predicts a student's final performance grade (**A, B, C, D, F**) based on study habits, attendance, assignments, previous marks, and class participation.

---

## 🚀 Features
- Preprocessing pipeline with **StandardScaler**.
- Multiple ML models tested:
  - Linear Regression  
  - Decision Tree  
  - Random Forest  
  - Gradient Boosting  
  - Support Vector Regressor (SVR)  
  - KNN Regressor  
- Evaluation metrics: **R² Score** and **Mean Squared Error (MSE)**.
- Best model (**Linear Regression**) saved with `joblib`.
- Interactive **Streamlit UI** with sliders for input.
- Attractive **Plotly gauge chart** visualization for predicted grade.

---

## 📂 Project Structure
```
├── student_performance_data.xlsx   # Dataset
├── app.py                          # Training + Streamlit app
├── requirements.txt                # Dependencies
├── best_model_with_scaler.pkl      # Saved model + scaler
└── README.md                       # Documentation

```
---

## ⚙️ Installation & Setup

```bash
# 1️⃣ Clone the repository
git clone https://github.com/YourUsername/StudentPerformancePredictor.git
cd StudentPerformancePredictor

# 2️⃣ Create & activate environment
conda create -n student_ml python=3.11 -y
conda activate student_ml

# 3️⃣ Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Training & Model Evaluation

Run the script to train and evaluate models:

```bash
python app.py
```

This will:
- Load dataset (`student_performance_data.xlsx`).
- Preprocess data (fill missing values, encode grades, scale features).
- Train multiple models (Linear Regression, Decision Tree, Random Forest, Gradient Boosting, SVR, KNN).
- Print **R² Score** and **MSE** for each model.
- Save the best model (`best_model_with_scaler.pkl`).

---

## ▶️ Launch Streamlit App

```bash
python -m streamlit run app.py
```

Open in browser at:  
👉 [http://localhost:8501](http://localhost:8501)

---

## 📊 Example Workflow
1. Adjust sliders for:
   - Study Hours Per Day  
   - Attendance Percentage  
   - Assignments Completed  
   - Previous Semester Marks  
   - Class Participation  
2. Click **Predict Grade**.  
3. See result with **interactive gauge chart**.  

---

## 🛠️ Tech Stack
- Python 3.11  
- scikit-learn 1.7.1  
- Streamlit 1.35+  
- Plotly 6.5  
- Pandas / NumPy / Matplotlib / Seaborn  

---

## 👩‍💻 Author
Developed by **Tooba Rani** — AI Engineer & Frontend Developer.  
Passionate about **AI-powered document processing** and **secure deployment workflows**.
