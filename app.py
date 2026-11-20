import streamlit as st
import requests
import os

from ai import get_ai_response
from backend import find_medicine, find_schemes


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="aarogya.ai",
    page_icon="🌿",
    layout="centered"
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 85% 8%,
                rgba(244, 184, 157, 0.35),
                transparent 28%
            ),
            radial-gradient(
                circle at 10% 40%,
                rgba(235, 202, 177, 0.22),
                transparent 30%
            ),
            #FFF8F2;
    }

    .block-container {
        max-width: 900px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 {
        color: #49352F !important;
    }

    p, label, .stMarkdown {
        color: #5E4A43;
    }


    /* ---------- HERO ---------- */

    .hero {
        background:
            linear-gradient(
                135deg,
                #F7C7AE 0%,
                #FBE1D1 55%,
                #FFF2E7 100%
            );
        border-radius: 28px;
        padding: 2.3rem 2.4rem 2.1rem 2.4rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(172, 111, 82, 0.12);
        box-shadow: 0 10px 30px rgba(110, 70, 50, 0.08);
        position: relative;
        overflow: hidden;
    }

    .hero::after {
        content: "🪷";
        position: absolute;
        right: 28px;
        top: 18px;
        font-size: 3.8rem;
        opacity: 0.25;
    }

    .hero-title {
        font-size: 2.55rem;
        font-weight: 800;
        color: #51372F;
        letter-spacing: -1px;
        margin-bottom: 0.15rem;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #795A4D;
        margin-bottom: 1.2rem;
    }

    .hero-description {
        font-size: 0.95rem;
        color: #6C5147;
        max-width: 650px;
        line-height: 1.65;
    }


    /* ---------- WELLNESS STRIP ---------- */

    .wellness-strip {
        display: flex;
        gap: 0.7rem;
        flex-wrap: wrap;
        margin: 1.1rem 0 1.6rem 0;
    }

    .wellness-pill {
        background: rgba(255, 255, 255, 0.72);
        border: 1px solid #EBD2C2;
        color: #75564A;
        padding: 0.45rem 0.8rem;
        border-radius: 999px;
        font-size: 0.78rem;
    }


    /* ---------- SECTION HEADERS ---------- */

    .section-heading {
        color: #51372F;
        font-size: 1.15rem;
        font-weight: 750;
        margin-top: 1.2rem;
        margin-bottom: 0.55rem;
    }

    .section-caption {
        color: #8A6B5D;
        font-size: 0.82rem;
        margin-bottom: 0.8rem;
    }


    /* ---------- INPUTS ---------- */

    .stTextInput > div > div,
    .stSelectbox > div > div {
        background-color: #FFFDFC !important;
        border-radius: 14px !important;
    }

    .stTextInput input {
        color: #49352F !important;
        background-color: #FFFDFC !important;
    }

    .stTextInput input:focus {
        border-color: #D99270 !important;
        box-shadow: 0 0 0 1px #D99270 !important;
    }

    .stSelectbox label,
    .stTextInput label {
        color: #60483E !important;
        font-weight: 600 !important;
    }


    /* ---------- FILE UPLOADER ---------- */

    [data-testid="stFileUploader"] {
        background: #FFFDFC;
        border: 1.5px dashed #DCA98D;
        border-radius: 18px;
        padding: 0.7rem;
    }

    [data-testid="stFileUploader"] section {
        background: transparent !important;
    }


    /* ---------- BUTTON ---------- */

    .stButton > button {
        width: 100%;
        border-radius: 15px;
        border: none;
        background: linear-gradient(
            135deg,
            #C97855,
            #D99270
        );
        color: white;
        font-weight: 700;
        font-size: 1rem;
        padding: 0.75rem 1rem;
        box-shadow: 0 7px 18px rgba(180, 104, 70, 0.22);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(
            135deg,
            #B96847,
            #C77F5E
        );
        transform: translateY(-1px);
        box-shadow: 0 9px 22px rgba(180, 104, 70, 0.28);
    }


    /* ---------- PHARMACY CARD ---------- */

    .pharmacy-card {
        background: rgba(255, 253, 250, 0.95);
        border: 1px solid #EBD9CD;
        border-radius: 18px;
        padding: 1rem 1.15rem;
        margin: 0.65rem 0;
        box-shadow: 0 5px 18px rgba(90, 58, 45, 0.055);
    }

    .pharmacy-name {
        color: #51372F;
        font-size: 1rem;
        font-weight: 750;
        margin-bottom: 0.35rem;
    }

    .pharmacy-detail {
        color: #735B50;
        font-size: 0.86rem;
        margin: 0.2rem 0;
    }

    .price {
        color: #B86645;
        font-size: 1rem;
        font-weight: 750;
        margin-top: 0.45rem;
    }


    /* ---------- RESULT BOX ---------- */

    .result-header {
        background: linear-gradient(
            135deg,
            #F9D5C0,
            #FCE9DC
        );
        border-radius: 18px;
        padding: 1rem 1.2rem;
        margin-top: 1.7rem;
        margin-bottom: 0.8rem;
        border: 1px solid #EACBB9;
    }

    .result-title {
        color: #51372F;
        font-size: 1.1rem;
        font-weight: 750;
    }


    /* ---------- INFO / DISCLAIMER ---------- */

    .soft-note {
        background: rgba(255, 244, 235, 0.85);
        border-left: 4px solid #D99270;
        border-radius: 12px;
        padding: 0.75rem 0.95rem;
        margin: 1rem 0;
        color: #73594E;
        font-size: 0.78rem;
        line-height: 1.5;
    }


    /* ---------- TRADITIONAL WELLNESS DECOR ---------- */

    .tradition-card {
        background:
            linear-gradient(
                135deg,
                rgba(255, 245, 236, 0.92),
                rgba(250, 226, 210, 0.82)
            );
        border: 1px solid #EBD4C4;
        border-radius: 20px;
        padding: 1rem 1.2rem;
        margin: 1.2rem 0;
        text-align: center;
    }

    .tradition-icons {
        font-size: 1.7rem;
        letter-spacing: 0.55rem;
        margin-bottom: 0.3rem;
    }

    .tradition-text {
        color: #795D50;
        font-size: 0.78rem;
        letter-spacing: 0.2px;
    }


    /* ---------- DIVIDER ---------- */

    hr {
        border: none !important;
        border-top: 1px solid #EBD9CD !important;
        margin: 1.5rem 0 !important;
    }


    /* ---------- MOBILE ---------- */

    @media (max-width: 640px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero {
            padding: 1.7rem;
            border-radius: 22px;
        }

        .hero-title {
            font-size: 2rem;
        }

        .hero::after {
            font-size: 2.8rem;
            right: 18px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🌿 aarogya.ai</div>
        <div class="hero-subtitle">Medicine access, made simpler.</div>
        <div class="hero-description">Ayushman Bharat, Swasth Bharat!</div>
        <div class="hero-description">
            Find nearby medicine availability, compare listed prices,
            discover affordable alternatives and understand government
            support — all in one place.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# WELLNESS STRIP
# ============================================================

st.markdown(
    """
    <div class="wellness-strip">
        <div class="wellness-pill">🧘 Simple & accessible</div>
        <div class="wellness-pill">🌿 Affordability focused</div>
        <div class="wellness-pill">💊 Medicine access</div>
        <div class="wellness-pill">🇮🇳 For every citizen</div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown(
    """
    <div class="soft-note">
        <strong>For medicine access and affordability information only.</strong>
        Always confirm medicine choice and substitution with a doctor or pharmacist.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PRESCRIPTION
# ============================================================

st.markdown(
    """
    <div class="section-heading">
        📋 Prescription
    </div>

    <div class="section-caption">
        Upload a prescription and we’ll identify the medicine for you.
    </div>
    """,
    unsafe_allow_html=True
)


prescription = st.file_uploader(
    "Upload prescription",
    type=["png", "jpg", "jpeg"],
    label_visibility="collapsed"
)


extracted_text = ""

if prescription:

    st.image(
        prescription,
        caption="Uploaded prescription",
        use_container_width=True
    )

    import pytesseract
    from PIL import Image

    image = Image.open(prescription)
    extracted_text = pytesseract.image_to_string(image)

    if not extracted_text.strip():
        st.warning(
            "No readable text was found in the prescription."
        )


# ============================================================
# AI MEDICINE EXTRACTION
# ============================================================

ocr_medicine = ""

if extracted_text.strip():

    extraction_prompt = f"""
You are extracting medicine names from a prescription.

OCR text:
{extracted_text}

Task:
Identify the most likely medicine name written in the prescription.

Rules:
- Return ONLY the medicine name.
- Do not return dosage instructions.
- Do not return quantity.
- Do not return doctor name.
- Do not return patient name.
- Do not explain anything.
- If no medicine name can be identified, return an empty string.
"""

    ocr_medicine = get_ai_response(
        extraction_prompt
    ).strip()


# ============================================================
# MEDICINE SEARCH
# ============================================================

st.markdown(
    """
    <div class="section-heading">
        💊 What medicine do you need?
    </div>

    <div class="section-caption">
        Enter the medicine manually or verify the name detected from your prescription.
    </div>
    """,
    unsafe_allow_html=True
)


medicine = st.text_input(
    "Medicine name",
    value=ocr_medicine,
    placeholder="e.g. Paracetamol 500 mg",
    label_visibility="collapsed"
)


# ============================================================
# LOCATION + LANGUAGE
# ============================================================

location = st.text_input(
    "Your location",
    placeholder="e.g. Mathura"
)


language = st.selectbox(
    "Preferred language",
    [
        "English",
        "Hindi"
    ]
)


# ============================================================
# API
# ============================================================

API_URL = os.getenv(
    "AAROGYA_API_URL",
    "http://localhost:8000"
)


# ============================================================
# SEARCH
# ============================================================

st.markdown("<div style='height: 0.4rem'></div>", unsafe_allow_html=True)

if st.button(
    "Find medicine & nearby options  →",
    type="primary"
):

    if not medicine:

        st.warning(
            "Please enter a medicine name."
        )

    elif not location:

        st.warning(
            "Please enter your location."
        )

    else:

        medicine_data = find_medicine(medicine)
        scheme_data = find_schemes()


        # ====================================================
        # PHARMACY API
        # ====================================================

        try:

            pharmacy_response = requests.get(
                f"{API_URL}/pharmacies",
                params={
                    "medicine": medicine.split()[0],
                    "location": location
                },
                timeout=10
            )

            pharmacy_response.raise_for_status()

            pharmacy_data = pharmacy_response.json()

        except requests.RequestException as e:

            st.error(
                f"Pharmacy API error: {e}"
            )

            pharmacy_data = {
                "medicine": medicine,
                "location": location,
                "count": 0,
                "results": []
            }

            st.warning(
                "Pharmacy availability is currently unavailable. "
                "You can still view medicine information."
            )


        # ====================================================
        # PHARMACY RESULTS
        # ====================================================

        if pharmacy_data["count"] > 0:

            st.markdown(
                """
                <div class="result-header">
                    <div class="result-title">
                        📍 Nearby pharmacies
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            for pharmacy in pharmacy_data["results"]:

                st.markdown(
                    f"""
                    <div class="pharmacy-card">

                        <div class="pharmacy-name">
                            🏪 {pharmacy['name']}
                        </div>

                        <div class="pharmacy-detail">
                            📍 {pharmacy['address']}
                        </div>

                        <div class="price">
                            ₹{pharmacy['price']}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.info(
                "No matching pharmacy was found in the current prototype database."
            )


        # ====================================================
        # MEDICINE INFORMATION
        # ====================================================

        if not medicine_data:

            st.warning(
                "We could not find this medicine in our current database."
            )

        else:

            prompt = f"""
You are aarogya.ai, a citizen-focused medicine access assistant.

Medicine entered by citizen: {medicine}
Location: {location}
Preferred language: {language}

Verified medicine information:
Generic name: {medicine_data["generic_name"]}
Common strengths: {", ".join(medicine_data["strengths"])}
Category: {medicine_data["category"]}
Generic/affordable alternative: {medicine_data["generic_alternative"]}
Affordability information: {medicine_data["affordable_option"]}

Pharmacy information retrieved from the aarogya.ai pharmacy API:
{pharmacy_data["results"]}

Government affordability programmes:
{scheme_data}

Use the verified information above to give the citizen a simple,
practical answer.

Tell the citizen:
1. Whether the medicine was found.
2. Which nearby pharmacies have it, if any.
3. The listed price where available.
4. The generic/affordable information available.
5. That pharmacy information is from the prototype database
   and may not represent live availability.

Do not invent:
- pharmacy availability
- prices
- medicine substitutions
- government schemes

If information is unavailable, clearly say so.

LANGUAGE RULE:
- If the preferred language is English, respond ONLY in natural English.
- If the preferred language is Hindi, respond ONLY in natural Hindi written in Devanagari script.
- Do not use Hinglish.
- Do not mix English and Hindi unless a medicine name, pharmacy name,
  scheme name, or technical medical term must remain in its original form.

Respond according to the language rule above.
"""

            # =================================================
            # AI RESPONSE
            # =================================================

            with st.spinner(
                "Finding the best available options..."
            ):

                response = get_ai_response(
                    prompt
                )


            st.markdown(
                """
                <div class="result-header">
                    <div class="result-title">
                        🌿 Your aarogya.ai guidance
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(response)


# ============================================================
# TRADITIONAL WELLNESS FOOTER
# ============================================================

st.markdown(
    """
    <div class="tradition-card">

        <div class="tradition-icons">
            🧘 🌿 🪷 🌿 🪔
        </div>

        <div class="tradition-text">
            Inspired by India's tradition of accessible,
            holistic wellbeing — built for today's citizen.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)
