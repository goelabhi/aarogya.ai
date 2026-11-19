import streamlit as st

st.set_page_config(
    page_title="aarogya.ai",
    page_icon="💊",
    layout="centered"
)

st.title("💊 aarogya.ai")
st.subheader("Medicine Access Assistant")

st.write(
    "Find medicine availability, prices, affordable alternatives, "
    "and relevant government support."
)

medicine = st.text_input(
    "Enter the medicine name",
    placeholder="e.g. Paracetamol 500 mg"
)

if st.button("Find Medicine"):
    if medicine.strip():
        st.info(f"Searching for: {medicine}")
    else:
        st.warning("Please enter a medicine name.")
