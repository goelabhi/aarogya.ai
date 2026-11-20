import streamlit as st

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
        st.success(
            f"Looking for **{medicine}** near **{location}**..."
        )
