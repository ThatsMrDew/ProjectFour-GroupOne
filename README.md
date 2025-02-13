# Heart Attack Risk Prediction Project

In this project, we worked with the **Heart Attack Risk Prediction Dataset** available on Kaggle:  
[Heart Attack Prediction Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset).


## 📂 Project Structure
```plaintext
ROOT/
├── etl.ipynb                      # Explores, cleans, and inserts the data into a SQLite database
├── heart.db                       # SQLite database containing the processed data
├── optimization.csv               # Documents model optimization and evaluation, showing iterative changes and performance results
├── Builds/
│   └── models.ipynb               # File where models are trained and tested
└── Resources/
    └── heart_attack_prediction.csv # Raw dataset used for model building
```

## 📝 Summary of Operations

### 1. Data Preprocessing  
- Dropped irrelevant columns, including *Patient ID, Country, Continent, Hemisphere,* and *Income*.  
- Converted all categorical columns into numeric format using `get_dummies()`.  
- Reduced the number of unique values in each column by converting float values to integers, eliminating unnecessary precision.  

### 2. Database Insertion  
- Stored the cleaned data in an SQLite database.  




## 📊 Database Documentation

### Database Schema

- **Age**: Age of the individual (integer, measured in years).  
- **Cholesterol**: Total cholesterol level in mg/dL (integer).  
- **Heart Rate**: Resting heart rate in beats per minute (integer).  
- **Diabetes**: Whether the individual has diabetes (binary: 0 = No, 1 = Yes).  
- **Family History**: Whether the individual has a family history of heart disease (binary: 0 = No, 1 = Yes).  
- **Smoking**: Whether the individual is a smoker (binary: 0 = No, 1 = Yes).  
- **Obesity**: Whether the individual is classified as obese (binary: 0 = No, 1 = Yes).  
- **Alcohol Consumption**: Whether the individual consumes alcohol (binary: 0 = No, 1 = Yes).  
- **Exercise Hours Per Week**: Total hours of exercise per week (integer).  
- **Previous Heart Problems**: Whether the individual has had previous heart problems (binary: 0 = No, 1 = Yes).  
- **Medication Use**: Whether the individual is currently using medication for heart-related conditions (binary: 0 = No, 1 = Yes).  
- **Stress Level**: Self-reported stress level on a scale from 1 to 10 (integer).  
- **Sedentary Hours Per Day**: Number of hours spent sedentary per day (integer).  
- **BMI**: Body Mass Index (BMI) of the individual (integer).  
- **Triglycerides**: Triglyceride level in mg/dL (integer).  
- **Physical Activity Days Per Week**: Number of days per week the individual engages in physical activity (integer).  
- **Sleep Hours Per Day**: Average number of sleep hours per day (integer).  
- **Heart Attack Risk**: Risk classification of heart attack (binary: 0 = Low, 1 = High).  
- **Systolic Pressure**: Systolic blood pressure in mmHg (integer).  
- **Diastolic Pressure**: Diastolic blood pressure in mmHg (integer).  
- **Sex_Female**: Whether the individual is female (binary: 0 = No, 1 = Yes).  
- **Sex_Male**: Whether the individual is male (binary: 0 = No, 1 = Yes).  
- **Diet_Average**: Whether the individual follows an average diet (binary: 0 = No, 1 = Yes).  
- **Diet_Healthy**: Whether the individual follows a healthy diet (binary: 0 = No, 1 = Yes).  
- **Diet_Unhealthy**: Whether the individual follows an unhealthy diet (binary: 0 = No, 1 = Yes).  



## 🛠️ Technologies Used

#### Programming Language
- **Python**: Used for data processing, machine learning, and database interactions.

#### Development Environment  
- **Jupyter Notebook**: Interactive environment for writing and running Python code, used for data exploration, visualization, and model experimentation.    

#### Data Handling & Analysis  
- **pandas**: Used for data manipulation and analysis.  
- **sqlite3**: Used for interacting with SQLite databases.  

#### Data Visualization  
- **matplotlib**: Used for creating static, animated, and interactive visualizations.  

#### Machine Learning  
- **scikit-learn**: Used for implementing machine learning models and preprocessing data.  
  - `StandardScaler`: For feature scaling.  
  - `accuracy_score`, `classification_report`, `confusion_matrix`: For model evaluation.  
  - `train_test_split`: For splitting data into training and testing sets.  
  - `LogisticRegression`: For logistic regression classification.  
  - `RandomForestClassifier`: For random forest classification.  
  - `MLPClassifier`: For neural network-based classification.  

#### Deep Learning  
- **TensorFlow / Keras**: Used for building and training deep learning models.  
  - `Sequential`: For creating sequential neural network models.  
  - `Dense`, `Dropout`, `BatchNormalization`, `LeakyReLU`: Various layers used in neural networks.  
  - `Adam`: An optimizer used for training deep learning models.  




## 💻 How to Use
Ensure that you have access to the technologies mentioned above.

To get started with this project locally:

1. Clone the repository:
   ```bash
   git clone url.git
   ```
2. Navigate to the project directory:
   ```bash
   cd folder
   ```
