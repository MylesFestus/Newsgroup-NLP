<div align="center">

# News Group Classifier

## NLP Fundamental Steps and Actions

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?logo=streamlit)](https://streamlit.io)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Text%20Classification-success)
![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?logo=kaggle&logoColor=white)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A machine learning application that classifies text documents into one of the 20 Newsgroups categories using NLP preprocessing, feature extraction, and text classification techniques.

</div>


## Overview

This project demonstrates the fundamental stages of a Natural Language Processing (NLP) workflow, including:

* Data acquisition
* Text preprocessing
* Feature extraction
* Model training
* Model evaluation
* Interactive deployment

The project uses the **20 Newsgroups Dataset**, one of the most widely used benchmark datasets for text classification tasks. The goal is to build an NLP pipeline capable of classifying documents into their corresponding newsgroup categories.

The solution is developed through a Jupyter Notebook for experimentation, modular Python scripts for reproducibility, and a Streamlit application for interactive predictions.

---

---

## Live Demo
***App URL: [https://mylesfestus-newsgroup-nlp-app-bzhdgd.streamlit.app]***

---

## Dataset

The project uses the **20 Newsgroups Dataset**, a collection of approximately 20,000 newsgroup documents partitioned across 20 different categories.

### Categories

* comp.graphics
* comp.os.ms-windows.misc
* comp.sys.ibm.pc.hardware
* comp.sys.mac.hardware
* comp.windows.x
* rec.autos
* rec.motorcycles
* rec.sport.baseball
* rec.sport.hockey
* sci.crypt
* sci.electronics
* sci.med
* sci.space
* misc.forsale
* talk.politics.misc
* talk.politics.guns
* talk.politics.mideast
* talk.religion.misc
* alt.atheism
* soc.religion.christian

Dataset source:

https://www.kaggle.com/datasets/crawford/20-newsgroups

---

## Project Structure

```text
├── notebooks/
│ └── main.ipynb


│── preprocess.py
├── train.py
├── app.py

├── model_pipeline.pkl
├── target_names.pkl
├── requirements.txt
├── README.md
└── .streamlit/
```

---

## NLP Pipeline

### 1. Data Acquisition

The dataset is loaded and explored to understand:

* Document distribution
* Category labels
* Class balance
* Sample texts

### 2. Text Preprocessing

The text cleaning pipeline includes:

* Lowercasing
* Removing punctuation
* Removing special characters
* Tokenization
* Stopword removal
* Text normalization

### 3. Feature Extraction

Text is transformed into numerical representations using techniques such as:

* Bag of Words (BoW)
* TF-IDF Vectorization

These features serve as input for machine learning algorithms.

### 4. Model Training

Classification models are trained on the processed text data to learn category patterns and predict unseen documents.

Typical workflow:

1. Split data into training and testing sets
2. Vectorize text
3. Train classifier
4. Evaluate performance

### 5. Model Evaluation

Performance is assessed using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/nlp-fundamental-steps-and-actions.git

cd nlp-fundamental-steps-and-actions
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Notebook

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/NLP_Fundamental_Steps_and_Actions.ipynb
```

---

## Running the Streamlit Application

Start the Streamlit app locally:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Streamlit Features

The deployed application allows users to:

* Enter custom text
* Process text using the NLP pipeline
* Generate features using the trained vectorizer
* Predict the most likely newsgroup category
* View prediction confidence scores

---

## Deployment

The application is deployed using Streamlit Community Cloud.

### Deployment Steps

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new app.
4. Connect the GitHub repository.
5. Select:

```text
app.py
```

6. Deploy the application.

---

## Libraries

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Jupyter Notebook
* Streamlit

---

## Learning Outcomes

This project demonstrates the complete NLP workflow from raw text data to production deployment, covering:

* Text preprocessing techniques
* Feature engineering for NLP
* Text classification
* Model evaluation
* Interactive web application development
* Cloud deployment using Streamlit

---

## Future Improvements

Potential enhancements include:

* Hyperparameter tuning
* Advanced text embeddings
* Word2Vec
* FastText
* BERT-based models
* Multi-label classification
* Explainable AI visualizations
* Docker deployment
* CI/CD integration

---

## Author
Festus and Krystyna
Developed as part of an MasterSchool Institute of Technology (MSIT), NLP learning project focused on understanding the core stages of text classification and deployment in real-world applications.
