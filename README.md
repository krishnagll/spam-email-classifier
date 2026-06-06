# 📧 Spam Email Classifier

A Machine Learning project that classifies messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) and the **Multinomial Naive Bayes** algorithm.

## 🚀 Overview

Spam messages are a common issue in digital communication. This project automatically detects spam emails/messages by converting text into numerical features and applying a machine learning model.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-Learn
* CountVectorizer
* Multinomial Naive Bayes

## 📂 Dataset

The project uses the **SMS Spam Collection Dataset**, containing labeled spam and ham messages.

## ⚙️ Workflow

1. Load and preprocess the dataset
2. Convert text into numerical features using CountVectorizer
3. Split data into training and testing sets
4. Train the model using Multinomial Naive Bayes
5. Evaluate performance and predict new messages

## 📈 Results

* Accuracy: **97%–99%**
* High precision and recall for spam detection

## ▶️ Installation

```bash
git clone https://github.com/krishnagll/spam-email-classifier.git
cd spam-email-classifier
pip install -r requirements.txt
python spam_classifier.py
```

## 🧪 Example

**Input:**

```text
Congratulations! You have won ₹50,000. Click here to claim your prize.
```

**Output:**

```text
SPAM EMAIL
```

## 📚 Learning Outcomes

* Text Preprocessing
* Feature Extraction with CountVectorizer
* Naive Bayes Classification
* Model Evaluation Metrics
* NLP Fundamentals

## 👨‍💻 Author

**Krishna Goyal**
Machine Learning Intern – Codec Technologies

GitHub: https://github.com/krishnagll
