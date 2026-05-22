import streamlit as st
import requests

# Dealership Branding
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

st.set_page_config(page_title="MHCH Quick-Gen", page_icon="🏔️")

st.title("🏔️ MHCH Real-Time Creator")

# --- INPUT SECTION ---
vin_input = st.text_input("Scan/Paste VIN:").upper()
miles_input = st.number_input("Current Miles:", min_value=0, step=1000)

# New Carfax/History Section
st.subheader("Carfax Highlights")
col1, col2 = st.columns(2)
with col1:
    one_owner = st.checkbox("1-Owner")
    no_accidents = st.checkbox("No Accidents")
with col2:
    service_history = st.checkbox("Good Service History")
    co_car = st.checkbox("Colorado Car")

# Key Features
features = st.multiselect("Select Key Features:", 
                         ["New Tires", "New Brakes", "Apple CarPlay", "Leather", "Heated Seats", "Tow Package", "Sunroof", "4x4/AWD"])

if st.button("🚀 GENERATE FOR YOUTUBE"):
    if vin_input:
        car = decode_vin(vin_input)
        if car and car['make']:
            # SMART TITLE
            history_hook = "CLEAN CARFAX! ✨ " if no_accidents else ""
            low_miles = "LOW MILES! ⚡ " if miles_input < 70000 else ""
            title = f"{history_hook}{low_miles}{car['year']} {car['make']} {car['model']} - Denver, CO #Shorts"
            
            # DESCRIPTION BUILDING
            history_list = ""
            if one_owner: history_list += "⭐ CARFAX 1-Owner\n"
            if no_accidents: history_list += "⭐ Accident-Free / Clean History\n"
            if service_history: history_list += "⭐ Excellent Service Records\n"
            if co_car: history_list += "⭐ Local Colorado Vehicle\n"

            feat_list = "".join([f"✅ {f}\n" for f in features])

            desc = f"""Full specs & price: https://{WEBSITE}

This {car['year']} {car['make']} {car['model']} is ready for the Mile High City! 

VEHICLE HISTORY:
{history_list}
DETAILS:
✅ {miles_input:,} Miles
✅ {car['drive']} 
{feat_list}
📍 Visit Us: {ADDRESS}
📞 Call/Text: {PHONE}

At Mile High Car Helper, we provide a no-headache buying experience and full-service auto repair. Denver's trusted car helper!

#DenverCars #MileHighCarHelper #CarfaxClean #UsedCarsDenver #ColoradoDrivers #{car['make']} #Shorts"""

            st.subheader("🎥 YouTube Title")
            st.code(title)
            st.subheader("📝 YouTube Description")
            st.code(desc)
        else:
            st.error("VIN Error")
