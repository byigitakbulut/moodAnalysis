# Movie Sentiment Analysis API

This project is a full-stack Machine Learning application that predicts the sentiment of movie reviews (Positive, Negative, or Neutral) using a custom-trained **LinearSVC** model. The system is served via a high-performance **FastAPI** backend and includes automated data scraping and preprocessing pipelines.



## Key Features
* **End-to-End Pipeline:** Automated data scraping (Selenium) to live API deployment (FastAPI).
* **High Performance:** Achieved **90% accuracy** on the test dataset through rigorous deduplication and text cleaning.
* **Robust Preprocessing:** Custom regex-based cleaning that handles punctuation, casing, and noise to match training conditions.
* **Interactive API Docs:** Built-in Swagger UI for real-time model testing.

## Tech Stack
* **Language:** Python 3.11.8
* **Data Scraping:** Selenium
* **Data Engineering:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (TfidfVectorizer + LinearSVC Pipeline)
* **Backend:** FastAPI & Uvicorn

## Project Structure

```text
project/
├── DataScrapCodes/
│   └── NegDataScraping.py       # Scraped negative movie reviews
│   └── PosDataScraping.py       # Scraped positive movie reviews
│   └── NotrDataScraping.py      # Scraped notr movie reviews
├── Datasets/
│   └── NegativeDataset.csv      # Extracted negative movie reviews
│   └── PositiveDataset.csv      # Extracted positive movie reviews
│   └── NotrDataset.csv          # Extracted notr movie reviews
├── DataProcessing/
│   └── forNegRev.ipynb          # Processed negative movie reviews
│   └── forPosRev.ipynb          # Processed positive movie reviews
│   └── forNotrRev.ipynb         # Processed notr movie reviews
│   └── forAllReviews.ipynb      # Merged data and processed all reviews
├── PreprocessedData/
│   └── NegativeDataset.csv      # Extracted negative processded movie reviews
│   └── PositiveDataset.csv      # Extracted positive processded movie reviews
│   └── NotrDataset.csv          # Extracted notr processded movie reviews
│   └── ReviewsDataset.csv       # Extracted all processded movie reviews
├── MLCodes/
│   └── modelFit.ipynb           # persist final LinearSVC model trained on full dataset
│   └── modelSelection.ipynb     # Extracted positive processded movie reviews
├── Models/
│   └── modelSVM.pkl             # Pre-trained Scikit-learn Pipeline
├── app/
│   └── main.py                  # FastAPI application & Regex Preprocessing
├── requirements.txt             # Dependencies (FastAPI, Scikit-learn, joblib, etc.)
```

## Installation & Usage

1.   Clone the repository:

```bash
git clone https://github.com/byigitakbulut/moodAnalysis.git
cd moodAnalysis
```

2.   Install dependencies:

```bash
pip install -r requirements.txt
```

3.   Run the API

```bash
cd app
uvicorn main:app --reload
```

4.  Test the API:

Open http://127.0.0.1:8000/docs to access the interactive Swagger UI and test with custom reviews.

## Model Details

The model was trained on a diverse dataset of IMDB reviews, filtered for lengths between 10 and 200 words to ensure high-quality context. The TF-IDF + LinearSVC pipeline was chosen for its optimal balance between training speed and predictive power on text classification tasks.

---
Developed by **Yiğit Akbulut** - 3rd Year Software Engineering Student.
