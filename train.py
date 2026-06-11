import joblib
import nltk

from sklearn.datasets import fetch_20newsgroups
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from preprocess import preprocess_text

nltk.download('stopwords')


def main():
    # Load dataset
    newsgroups = fetch_20newsgroups(
        subset='all', remove=('headers', 'footers', 'quotes'))

    X = newsgroups.data
    y = newsgroups.target

    # Create pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(preprocessor=preprocess_text)),
        ('model', MultinomialNB())
    ])

    # Train on full dataset
    pipeline.fit(X, y)

    # save model
    joblib.dump(pipeline, 'model_pipeline.pkl')

    # save class names
    joblib.dump(
        newsgroups.target_names,
        'target_names.pkl')

    print("Training complete!")
    print("Model saved to model_pipeline.pkl!")
    print("Target names saved to target_names.pkl!")


if __name__ == "__main__":
    main()



