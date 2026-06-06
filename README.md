# 📧 Spam Email Classifier using Machine Learning

This repository contains a Machine Learning-based Spam Email Classifier developed as part of my Machine Learning Internship at Codec Technologies. The model classifies messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) and the Naive Bayes algorithm.

---

## 🚀 Overview

Spam emails and messages are a common problem in digital communication. This project uses text classification techniques to automatically detect whether a message is spam or legitimate.

The workflow includes:

1. Data Loading and Cleaning
2. Text Vectorization using CountVectorizer
3. Model Training using Multinomial Naive Bayes
4. Performance Evaluation
5. Real-Time Message Prediction

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* CountVectorizer
* Multinomial Naive Bayes

---

## 📂 Dataset

The project uses the **SMS Spam Collection Dataset**, which contains thousands of labeled SMS messages.

### Labels:

* **Ham (0)** → Legitimate Message
* **Spam (1)** → Unwanted or Promotional Message

---

## ⚙️ Machine Learning Pipeline

### Step 1: Data Preprocessing

* Load dataset using Pandas
* Select relevant columns
* Convert labels into numerical format

### Step 2: Feature Extraction

Text data is converted into numerical vectors using:

```python
CountVectorizer()
```

This creates a vocabulary of unique words and transforms messages into feature vectors.

### Step 3: Train-Test Split

```python
train_test_split()
```

Dataset is split into:

* 80% Training Data
* 20% Testing Data

### Step 4: Model Training

```python
MultinomialNB()
```

Multinomial Naive Bayes is highly effective for text classification problems where features represent word frequencies.

### Step 5: Evaluation

The model is evaluated using:

* Accuracy Score
* Precision
* Recall
* F1-Score
* Classification Report

---

## 📈 Results

The model achieves approximately:

* Accuracy: 97% – 99%
* High Precision and Recall for Spam Detection
* Fast Prediction Time

---

## 💡 Features

✅ Automatic Spam Detection

✅ Real-Time User Input Prediction

✅ Efficient NLP-Based Text Classification

✅ Easy to Train and Deploy

---

## ▶️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/krishnagll/spam-email-classifier.git
```

Move into the project directory:

```bash
cd spam-email-classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python spam_classifier.py
```

---

## 🧪 Example

Input:

```text
Congratulations! You have won ₹50,000. Click here to claim your prize.
```

Output:

```text
SPAM EMAIL
```

Input:

```text
Hi Krishna, are we meeting tomorrow for the project discussion?
```

Output:

```text
NOT SPAM
```

---

## 📚 Learning Outcomes

Through this project, I learned:

* Text Preprocessing
* Natural Language Processing Basics
* Feature Extraction using CountVectorizer
* Naive Bayes Classification
* Model Evaluation Metrics
* Real-World Spam Detection Applications

---

## 👨‍💻 Author

**Krishna Goyal**

Machine Learning Intern

Codec Technologies

GitHub: https://github.com/krishnagll

---

## 📜 License

This project is intended for educational and learning purposes.
