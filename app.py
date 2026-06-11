import joblib
import streamlit as st

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="Newsgroup Classifier",
    page_icon="📰",
    layout="centered"
)

# -----------------------
# Load Model
# -----------------------
pipeline = joblib.load("model_pipeline.pkl")

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

# -----------------------
# Custom CSS
# -----------------------
st.markdown("""
<style>

/* App Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 40%,
        #2563eb 100%
    );
}

/* Watermark */
.stApp::before {
    content: "Myles24hrNews";
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-30deg);
    font-size: 90px;
    font-weight: 900;
    color: rgba(255,255,255,0.05);
    z-index: 0;
    pointer-events: none;
}

/* Glass Container */
.main-container {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.15);
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #dbeafe;
    margin-bottom: 25px;
    font-size: 18px;
}

/* Text Area */
textarea {
    border-radius: 12px !important;
    border: 2px solid #60a5fa !important;
    font-size: 16px !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    color: white;
    border: none;
    border-radius: 12px;
    height: 52px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg, #0891b2, #2563eb);
}

/* Count Box */
.count-box {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 12px;
    border-radius: 12px;
    color: white;
    text-align: center;
    margin-top: 8px;
    margin-bottom: 18px;
    font-size: 16px;
}

/* Result Card */
.result-card {
    background: linear-gradient(90deg, #10b981, #059669);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# Main UI
# -----------------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown(
    '<div class="title">📰 Newsgroup Classifier</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Topic Prediction for News Articles and Text</div>',
    unsafe_allow_html=True
)

# Text Input
text = st.text_area(
    "✍️ Enter your text below",
    height=220,
    placeholder="Paste your article, message, or news content here..."
)

# Word and Character Counts
word_count = len(text.split()) if text else 0
char_count = len(text)

st.markdown(
    f"""
    <div class="count-box">
        📝 <b>Words:</b> {word_count}
        &nbsp;&nbsp;|&nbsp;&nbsp;
        🔤 <b>Characters:</b> {char_count}
    </div>
    """,
    unsafe_allow_html=True
)

# Prediction
if st.button(" Predict Topic"):
    if text.strip():
        pred = pipeline.predict([text])[0]

        st.markdown(
            f"""
            <div class="result-card">
                Predicted Topic<br><br>
                {target_names[pred]}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Please enter some text before prediction.")

st.markdown("</div>", unsafe_allow_html=True)