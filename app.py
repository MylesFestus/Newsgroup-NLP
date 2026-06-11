import joblib
import streamlit as st

pipeline = joblib.load('model_pipeline.pkl')

target_names = [
    "alt.atheism",
    "comp.graphics",
    "comp.os.ms-windows.misc",
    "comp.sys.ibm.pc.hardware",
    "comp.sys.mac.hardware",
    "comp.windows.x",
    "misc.forsale",
    "rec.autos",
    "rec.motorcycles",
    "rec.sport.baseball",
    "rec.sport.hockey",
    "sci.crypt",
    "sci.electronics",
    "sci.med",
    "sci.space",
    "soc.religion.christian",
    "talk.politics.guns",
    "talk.politics.mideast",
    "talk.politics.misc",
    "talk.religion.misc"
]

st.title('Newsgroup Text Classifier')

st.write('This app predicts the topic of a given text.')

text = st.text_area('Enter a text')

if st.button('Predict'):
    pred = pipeline.predict([text])[0]
    st.write('Predicted group:', target_names[pred[0]])
