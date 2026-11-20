import streamlit as st
from ai import get_ai_response

st.set_page_config(
    page_title="aarogya.ai",
    page_icon="💊",
    layout="centered"
)

st.title("💊 aarogya.ai")
st.caption("Medicine Access Assistant")

st.write(
    "Find nearby availability, affordable alternatives, "
    "and government support for your medicine."
)

st.divider()

medicine = st.text_input(
    "What medicine are you looking for?",
    placeholder="e.g. Paracetamol 500 mg"
)

location = st.text_input(
    "Your location",
    placeholder="e.g. Meerut"
)

language = st.selectbox(
    "Preferred language",
    [
        "English",
        "Hindi"
    ]
)

if st.button("Find medicine", type="primary"):
    if not medicine:
        st.warning("Please enter a medicine name.")
    elif not location:
        st.warning("Please enter your location.")
    else:
        prompt = f"""
You are aarogya.ai, a citizen-focused medicine access assistant.

Medicine: {medicine}
Location: {location}
Preferred language: {language}

Explain what information would be useful to the citizen about
this medicine, including availability, approximate price,
affordable alternatives, and relevant government support.

Do not invent pharmacy availability, prices, medicine substitutions,
or government schemes. Clearly state when information is unavailable.
Respond simply and clearly.
"""

        with st.spinner("Finding information..."):
            response = get_ai_response(prompt)

        st.subheader("aarogya.ai")
        st.write(response)
