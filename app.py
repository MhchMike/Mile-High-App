import streamlit as st
import requests

# Dealership Branding - UPDATED
DEALER_NAME = "Mile High Car Helper"
WEBSITE = "milehighcarhelper.com"
PHONE = "(720) 605-1749"
ADDRESS = "1709 S. Acoma St., Denver, CO 80223"

def decode_vin(vin):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vin}?format=json"
    try:
        response = requests.get(url)
        data = response.json()['Results'][0]
        return {
            "year": data.get("ModelYear"),
            "make": data.get("Make"),
            "model": data.get("Model"),
            "drive": data.get("DriveType"),
        }
    except:
        return None

st.set_page_config(page_title="MHCH SEO Gen", page_icon="🏔️")

st.markdown("""
    <style>
    .stButton>button { width: 100%; height: 3em; background-color: #FF0000; color: white; font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏔️ MHCH SEO Creator")

vin_input = st.text_input("Paste VIN:", placeholder="17-digit number").upper()
miles_input = st.number_input("Enter Miles:", min_value=0, step=1000)

if st.button("🚀 GENERATE SEO CONTENT"):
    if vin_input:
        car = decode_vin(vin_input)
        if car and car['make']:
            # SMART TITLE: Includes Denver for search reach
            low_miles_hook = "LOW MILES! ⚡ " if miles_input < 60000 else ""
            shorts_title = f"{low_miles_hook}{car['year']} {car['make']} {car['model']} - Denver, CO #Shorts"
            
            # SEO DESCRIPTION: Includes the full NAP (Name, Address, Phone)
            shorts_desc = f"""Check out this {car['year']} {car['make']} {car['model']}! 
👉 View details: https://{WEBSITE}

This {car['make']} is currently available at {DEALER_NAME}! We are a no-headache used car dealer and full-service repair shop in the heart of Denver.

✅ Miles: {miles_input:,}
✅ Drive: {car['drive']}
📍 Location: {ADDRESS}
📞 Call/Text: {PHONE}

#DenverCars #MileHighCarHelper #UsedCarsDenver #ColoradoDrivers #{car['make']} #Shorts"""

            st.success("SEO Content Ready!")
            st.subheader("🎥 YouTube Title (Copy this)")
            st.code(shorts_title)
            
            st.subheader("📝 YouTube Description (Copy this)")
            st.code(shorts_desc)
            
            st.info("💡 Pro-Tip: When uploading, set the 'Location' field in YouTube to '1709 S Acoma St' to link this video to your shop's Google map!")
        else:
            st.error("Invalid VIN. Please check and try again.")
