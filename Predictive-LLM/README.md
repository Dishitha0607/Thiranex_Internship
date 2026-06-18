# Student Performance Prediction Using Machine Learning

## Overview

This project focuses on predictive modeling using machine learning techniques to classify student performance as either **Pass** or **Fail**. The model analyzes various academic factors such as study hours, attendance, previous marks, and assignment completion to make predictions.

The project demonstrates the complete machine learning workflow, including data generation, preprocessing, model training, evaluation, and visualization.

---

## Objectives

* Build a predictive model to classify student performance.
* Apply supervised machine learning algorithms.
* Train and test models using historical data.
* Evaluate model performance using accuracy metrics.
* Visualize results using confusion matrices and ROC curves.

---

## Dataset

A synthetic dataset containing 100 student records was generated for this project.

### Features

| Feature       | Description                             |
| ------------- | --------------------------------------- |
| StudyHours    | Number of study hours                   |
| Attendance    | Attendance percentage                   |
| PreviousMarks | Marks obtained in previous examinations |
| Assignments   | Number of assignments completed         |
| Result        | Pass (1) or Fail (0)                    |

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Machine Learning Algorithms

The following supervised learning algorithms were implemented:

### Decision Tree Classifier

* Creates a tree-based model using decision rules.
* Easy to interpret and visualize.

### Random Forest Classifier

* Ensemble learning method using multiple decision trees.
* Improves prediction accuracy and reduces overfitting.

---

## Project Workflow

1. Dataset Generation
2. Data Loading and Inspection
3. Data Preprocessing
4. Feature Selection
5. Train-Test Split
6. Model Training
7. Prediction
8. Performance Evaluation
9. Visualization
10. Model Comparison

---

## Evaluation Metrics

The models were evaluated using:

* Accuracy Score
* Confusion Matrix
* ROC Curve
* AUC Score

---

## Results

Both Decision Tree and Random Forest models were trained and tested on the dataset. Model performance was compared using accuracy and classification metrics.

The Random Forest model achieved the best overall performance and demonstrated strong predictive capability for student performance classification.

---

## Learning Outcomes

Through this project, the following concepts were explored:

* Supervised Machine Learning
* Classification Problems
* Data Preprocessing
* Model Training and Testing
* Performance Evaluation
* Data Visualization
* Predictive Analytics

---

## Future Enhancements

* Use a real-world student performance dataset.
* Implement additional algorithms such as Logistic Regression, Support Vector Machines, and XGBoost.
* Develop a web application using Streamlit for real-time predictions.
* Deploy the model for online access.

---

## Conclusion

This project successfully demonstrates the application of machine learning techniques for predictive modeling. By utilizing Decision Tree and Random Forest algorithms, student performance can be accurately predicted based on academic indicators. The project provides practical experience in supervised learning, model evaluation, and data visualization.
