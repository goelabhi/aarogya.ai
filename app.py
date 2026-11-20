import streamlit as st
import requests
from ai import get_ai_response
from backend import find_medicine

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
        medicine_data = find_medicine(medicine)
        
        API_URL = "http://localhost:8000"

        pharmacy_response = requests.get(
            f"{API_URL}/pharmacies",
            params={
                "medicine": medicine.split()[0],
                "location": location
            }
        )

        pharmacy_data = pharmacy_response.json()
        
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
Affordability information: {medicine_data["affordable_option"]}

Explain this information simply for the citizen.

Do not invent:
- pharmacy availability
- prices
- medicine substitutions
- government schemes

If information is unavailable, clearly say so.
"""

            with st.spinner("Finding information..."):
                response = get_ai_response(prompt)

            st.subheader("aarogya.ai")
            st.write(response)
