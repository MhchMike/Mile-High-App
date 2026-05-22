import streamlit as st
import requests

# Dealership Branding
DEALER_NAME = "Mile High Car Helper"
WEBSITE = "milehighcarhelper.com"
LOCATION = "Denver, CO"

def decode_vin(vin):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vin}?format=json"
    try:
        response = requests.get(url)
        data = response.json()['Results'][0]
        return {
            "year": data.get("ModelYear"),
            "make": data.get("Make"),
            "model": data.get("Model"),
        }
    except:
        return None

# --- UI DESIGN ---
st.set_page_config(page_title="MHCH Shorts Gen", page_icon="📱")

st.markdown("""
    <style>
    .main { max-width: 100%; }
    .stButton>button { width: 100%; height: 3em; background-color: #FF0000; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏔️ MHCH Shorts Creator")

vin_input = st.text_input("Paste VIN:", placeholder="17-digit number").upper()
miles_input = st.text_input("Enter Miles:", placeholder="e.g. 85000")

if st.button("🚀 GENERATE FOR SHORTS"):
    if vin_input:
        car = decode_vin(vin_input)
        if car and car['make']:
            shorts_title = f"{car['year']} {car['make']} {car['model']} Walkaround! 🔥 #Shorts"
            shorts_desc = f"""{car['year']} {car['make']} {car['model']} at {DEALER_NAME}! 

✅ {miles_input} Miles
📍 {LOCATION}
🔗 Full info: {WEBSITE}

#CarSales #Denver #UsedCars #Walkaround #{car['make']} #MileHighCarHelper #Shorts"""

            st.subheader("Copy Title:")
            st.code(shorts_title)
            st.subheader("Copy Description:")
            st.code(shorts_desc)
        else:
            st.error("Invalid VIN. Try again.")
