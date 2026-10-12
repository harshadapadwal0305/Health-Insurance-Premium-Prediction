
import streamlit as st
import pickle
import time

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Health Insurance Premium Prediction",
    page_icon="🩺",
    layout="centered"
)

# ---------------- LOAD MODEL ---------------- #

model = pickle.load(open("HI_model.pkl", "rb"))

# ---------------- CSS ---------------- #

st.markdown("""
<style>

/* ---------- GLOBAL THEME ---------- */

.stApp {
    background-color: #F7F5EF;
    color: #263B32;
    font-family: "Trebuchet MS", sans-serif;
}

.block-container {
    max-width: 1000px;
    padding-top: 2.5rem;
    padding-bottom: 1rem;
}

/* Hide Streamlit Branding */

#MainMenu,
footer,
header {
    visibility: hidden;
}

/* ---------- HEADER ---------- */

.brand {
    color: #52695A;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    text-align: center;
    margin-bottom: 25px;
}

.title {
    text-align: center;
    font-family: Georgia, serif;
    font-size: 39px;
    line-height: 1.25;
    font-weight: 500;
    letter-spacing: -1px;
    color: #1F4035;
    margin-bottom: 12px;
}

.subtitle {
    text-align: center;
    color: #7B8177;
    font-size: 15px;
    line-height: 1.9;
    margin: 0 auto 32px auto;
    max-width: 600px;
}

.heading-line {
    width: 42px;
    height: 2px;
    background: #A8B49A;
    margin: 0 auto 22px auto;
}

/* ---------- FORM CARD ---------- */

[data-testid="stForm"] {
    background: #FFFEFA;
    padding: 32px;
    border: 1px solid #E7E4D9;
    border-radius: 8px;
    box-shadow: 0 12px 35px rgba(46, 61, 47, 0.055);
}

/* Labels */

[data-testid="stWidgetLabel"] p {
    color: #354B3F !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    letter-spacing: 0.2px;
}

/* Number Inputs */

[data-testid="stNumberInput"] input {
    background-color: #FBFAF6 !important;
    color: #263B32 !important;
    border: 1px solid #DEDCCF !important;
    border-radius: 5px !important;
    min-height: 43px;
}

/* Select Box */

[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #FBFAF6 !important;
    border-color: #DEDCCF !important;
    border-radius: 5px !important;
    color: #263B32 !important;
    min-height: 43px;
}

/* Radio Buttons */

div[role="radiogroup"] {
    gap: 12px;
}

div[role="radiogroup"] label {
    background: #F8F7F1;
    border: 1px solid #E4E2D8;
    border-radius: 5px;
    padding: 8px 13px;
}

div[role="radiogroup"] label p {
    color: #354B3F !important;
    font-size: 14px !important;
}

/* ---------- BUTTON ---------- */

[data-testid="stFormSubmitButton"] > button {
    width: 100%;
    min-height: 49px;
    background: #254B3B;
    color: #FFFFFF;
    border: 1px solid #254B3B;
    border-radius: 5px;
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 0.5px;
    transition: all 0.25s ease;
}

[data-testid="stFormSubmitButton"] > button:hover {
    background: #18392D;
    color: #FFFFFF;
    border-color: #18392D;
    box-shadow: 0 5px 15px rgba(37, 75, 59, 0.16);
}

/* ---------- RESULT CARD ---------- */

.result-card {
    background: #FFFEFA;
    padding: 35px 25px;
    margin-top: 26px;
    border: 1px solid #E7E4D9;
    border-top: 3px solid #6C866F;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 12px 30px rgba(46, 61, 47, 0.05);
}

.result-label {
    color: #7B8177;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.result-amount {
    color: #254B3B;
    font-family: Georgia, serif;
    font-size: 43px;
    font-weight: 500;
    letter-spacing: -1px;
    margin: 8px 0 18px 0;
}

.result-divider {
    width: 55px;
    border: none;
    border-top: 1px solid #C8D0C0;
    margin: 20px auto;
}

.result-description {
    color: #7B8177;
    font-size: 14px;
    line-height: 1.9;
}

/* ---------- SUMMARY ---------- */

.summary-title {
    color: #254B3B;
    font-family: Georgia, serif;
    font-size: 25px;
    font-weight: 500;
    margin-top: 30px;
    margin-bottom: 15px;
}

/* Summary Alerts */

[data-testid="stAlert"] {
    border-radius: 5px;
    border: 1px solid #E7E4D9;
}

/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background: #213E32;
    border-right: 1px solid #314F41;
}

section[data-testid="stSidebar"] * {
    color: #F8F5EC;
}

section[data-testid="stSidebar"] h1 {
    font-family: Georgia, serif;
    font-size: 24px;
    font-weight: 500;
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #D0D9C8;
    font-size: 14px;
    letter-spacing: 1px;
}

section[data-testid="stSidebar"] hr {
    border-color: #506557;
}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    font-size: 14px;
    line-height: 1.9;
}

/* ---------- FOOTER ---------- */

.footer-line {
    border-top: 1px solid #E2DFD4;
    margin-top: 35px;
    padding-top: 22px;
}

.footer {
    text-align: center;
    color: #898D82;
    font-size: 12px;
    line-height: 2;
    letter-spacing: 0.5px;
    padding-bottom: 8px;
}

/* ---------- MOBILE ---------- */

@media (max-width: 640px) {
    .block-container {
        padding: 1.3rem 1rem;
    }

    .title {
        font-size: 29px;
    }

    .subtitle {
        font-size: 13px;
    }

    [data-testid="stForm"] {
        padding: 20px 16px;
    }

    .result-card {
        padding: 27px 15px;
    }

    .result-amount {
        font-size: 34px;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("🩺 Health Insurance")

    st.markdown("---")

    st.subheader("ABOUT")

    st.write("""
Estimate your annual health insurance premium
using Machine Learning.

Fill in your details and click **Predict Premium**.
""")

    st.markdown("---")

    st.subheader("PARAMETERS USED")

    st.write("👤 Age")
    st.write("🚻 Gender")
    st.write("⚖️ BMI")
    st.write("👶 Number of Children")
    st.write("🚬 Smoking Status")

# ---------------- TITLE ---------------- #

st.markdown("""
<div class="brand">HEALTHCARE · INTELLIGENCE</div>

<div class="heading-line"></div>

<div class="title">
    Health Insurance<br>Premium Prediction
</div>

<div class="subtitle">
    A smarter way to estimate your annual health insurance premium.
    Enter your details below to receive a personalised estimate
    powered by Machine Learning.
</div>
""", unsafe_allow_html=True)

# ---------------- FORM ---------------- #

with st.form("insurance_form"):

    col1, col2 = st.columns(2, gap="large")

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=25,
            step=1
        )

        sex = st.radio(
            "Gender",
            ["Male", "Female"],
            horizontal=True
        )

        children = st.selectbox(
            "Number of Children",
            [0, 1, 2, 3, 4, 5, 6]
        )

    with col2:

        bmi = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=60.0,
            value=22.5,
            step=0.1
        )

        smoker = st.radio(
            "Smoking Status",
            ["Yes", "No"],
            horizontal=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    submit = st.form_submit_button("🔍  Predict Premium")

# ---------------- PREDICTION ---------------- #

if submit:

    # Encode categorical values
    sex_enc = 1 if sex == "Female" else 0
    smoker_enc = 1 if smoker == "Yes" else 0

    # Input for prediction
    q = [[age, sex_enc, bmi, children, smoker_enc]]

    # Predict
    with st.spinner("Calculating your insurance premium..."):
        time.sleep(1)
        prediction = round(model.predict(q)[0], 2)

    # Toast Notification (instead of balloons)
    st.toast("✅ Prediction Completed Successfully!")

    
    
    # Result Card
    st.markdown(f"""
        <div class="result-card">
        <div class="result-label">Estimated Annual Premium</div>
        <div class="result-amount">₹ {prediction:,.2f}</div>
        <hr class="result-divider">
        <p class="result-description">
        Based on the details you entered, your estimated
        <b>annual health insurance premium</b> is shown above.
        </p>
        </div>
    """, unsafe_allow_html=True)


    st.markdown(
        '<div class="summary-title">Your Details</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"👤 **Age:** {age}")
        st.info(f"🚻 **Gender:** {sex}")
        st.info(f"👶 **Children:** {children}")

    with col2:
        st.info(f"⚖️ **BMI:** {bmi}")
        st.info(f"🚬 **Smoking:** {smoker}")
        st.success(f"💰 **Premium:** ₹ {prediction:,.2f}")

# ---------------- FOOTER ---------------- #

st.markdown("""
<div class="footer-line">
    <div class="footer">
        HEALTH INSURANCE PREMIUM PREDICTION
        <br>
        Powered by Machine Learning
    </div>
</div>
""", unsafe_allow_html=True)
