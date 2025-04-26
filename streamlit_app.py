# import streamlit as st
# import pyrebase
# import time

# # Firebase config
# firebase_config = {
#     "apiKey": "AIzaSyDp1wox6CIg1sbRf9uqPnLXYMf-1hLWuGg",
#     "authDomain": "Yadeliot-feb2f.firebaseapp.com",
#     "databaseURL": "https://adeliot-feb2f-default-rtdb.asia-southeast1.firebasedatabase.app",
#     "storageBucket": "adeliot-feb2f.firebasestorage.app"
# }

# # Initialize Firebase
# firebase = pyrebase.initialize_app(firebase_config)
# auth = firebase.auth()
# db = firebase.database()

# # Login
# email = "afifahadelia.2022@student.uny.ac.id"
# password = "Adel0407"
# user = auth.sign_in_with_email_and_password(email, password)

# # Helper to get the latest value from a node
# def get_latest_value(node):
#     data = db.child("sensor").child(node).order_by_key().limit_to_last(1).get(user['idToken']).val()
#     if data:
#         last_key = list(data.keys())[0]
#         return data[last_key]
#     return None

# # UI setup
# st.title("🌡️ Live Sensor Data")
# st.title("Afifah Adelia")
# st.title("22518241033")
# # Create placeholders for data
# temperature_placeholder = st.empty()
# humidity_placeholder = st.empty()


# # Fetch and display data every 5 seconds
# while True:
#     # Fetch the latest temperature and humidity
#     tem = get_latest_value("temp")
#     hum = get_latest_value("humi")

#     # Update the placeholders with new data
#     if tem is not None and hum is not None:
#         temperature_placeholder.metric("Temperature (°C)", tem)
#         humidity_placeholder.metric("Humidity (%)", hum)
#     else:
#         temperature_placeholder.warning("No temperature data available.")
#         humidity_placeholder.warning("No humidity data available.")

#     # Sleep for 5 seconds before refreshing data
#     time.sleep(5)

import streamlit as st
import pyrebase
import time
import matplotlib.pyplot as plt

# Firebase config
firebase_config = {
    "apiKey": "AIzaSyDp1wox6CIg1sbRf9uqPnLXYMf-1hLWuGg",
    "authDomain": "Yadeliot-feb2f.firebaseapp.com",
    "databaseURL": "https://adeliot-feb2f-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "adeliot-feb2f.firebasestorage.app"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

# Login
email = "afifahadelia.2022@student.uny.ac.id"
password = "Adel0407"
user = auth.sign_in_with_email_and_password(email, password)

# Helper to get the latest value from a node
def get_latest_value(node):
    data = db.child("sensor").child(node).order_by_key().limit_to_last(1).get(user['idToken']).val()
    if data:
        last_key = list(data.keys())[0]
        return data[last_key]
    return None

# UI setup
st.title("🌡️ Live Sensor Data")
st.title("Afifah Adelia")
st.title("22518241033")

# Create placeholders for metrics and charts
temperature_placeholder = st.empty()
humidity_placeholder = st.empty()
chart_temp_placeholder = st.empty()
chart_humi_placeholder = st.empty()

# Helper to create simple bar-like charts
def create_bar_chart(value, label, max_value=100):
    fig, ax = plt.subplots(figsize=(5, 0.7))
    ax.barh([label], [float(value)], color='skyblue')
    ax.set_xlim(0, max_value)
    ax.set_xlabel(f"{label}")
    ax.set_title(f"{label}: {value}")
    plt.tight_layout()
    return fig

# Live update loop
while True:
    # Fetch latest data
    tem = get_latest_value("temp")
    hum = get_latest_value("humi")

    # Update metrics and charts
    if tem is not None and hum is not None:
        temperature_placeholder.metric("Temperature (°C)", tem)
        humidity_placeholder.metric("Humidity (%)", hum)

        # Create and display bar charts
        fig_temp = create_bar_chart(tem, "Temperature (°C)")
        fig_humi = create_bar_chart(hum, "Humidity (%)")

        chart_temp_placeholder.pyplot(fig_temp)
        chart_humi_placeholder.pyplot(fig_humi)

    else:
        temperature_placeholder.warning("No temperature data available.")
        humidity_placeholder.warning("No humidity data available.")

    time.sleep(5)
