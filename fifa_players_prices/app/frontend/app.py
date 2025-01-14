import streamlit as st
import requests
from numerize import numerize

st.set_page_config(page_title="Price Prediction", layout="centered")

# Set the title and description
st.title("Price prediction of FIFA videogame players ⚽")
st.markdown("This app uses a random forest regressor model to predict the Market Transfer price of football players, \
            based on data from FIFA videogames from the year 2015 to 2023 and given some player attributes.")
st.markdown("[SOURCE CODE](https://github.com/hugojira/fifa_players_prices)")
st.markdown("The most important features in the model are **Potential** and **Age**, followed by the other ones.")
st.markdown("Tune the desired player's features below:")

# Sliders for each feature
col1, col2, col3, col4 = st.columns(4)

with col1:
    age = st.slider(label="Age", min_value=16, max_value=50, step=1, value=22)
    potential = st.slider("Potential", min_value=40.0, max_value=99.0, step=1.0, value=79.0)
    shooting = st.slider("Shooting", min_value=40.0, max_value=99.0, step=1.0, value=83.0)

with col2:
    height_cm = st.slider("Height (in cm)", min_value=160.0, max_value=210.0, step=1.0, value=180.0)
    pace = st.slider("Pace", min_value=40.0, max_value=99.0, step=1.0, value=76.0)
    passing = st.slider("Passing", min_value=40.0, max_value=99.0, step=1.0, value=81.0)

with col3:
    weak_foot = st.slider("Weak foot skill", min_value=0, max_value=5, step=1, value=3)
    physic = st.slider("Physic", min_value=40.0, max_value=99.0, step=1.0, value=74.0)
    dribbling = st.slider("Dribbling", min_value=40.0, max_value=99.0, step=1.0, value=87.0)

with col4:
    international_reputation = st.slider("International reputation", min_value=0, max_value=5, step=1, value=2)
    defending = st.slider("Defending", min_value=40.0, max_value=99.0, step=1.0, value=59.0)

# Create a button to trigger prediction
predict_button = st.button("Predict")

# Make the prediction
if predict_button:
    # Prepare the data for the API request
    data = {
        "age": age,
        "height_cm": height_cm,
        "weak_foot": weak_foot,
        "international_reputation": international_reputation,
        "potential": potential,
        "pace": pace,
        "shooting": shooting,
        "passing": passing,
        "dribbling": dribbling,
        "defending" : defending,
        "physic" : physic
    }

    # Send the request to the FastAPI endpoint
    try:
        response = requests.post("https://fastapi-fifa-prices-137775223493.us-central1.run.app/prediction", json=data) 
        response.raise_for_status()  # Raise an exception for bad status codes

        # Get the prediction from the response
        prediction = response.json()["Prediction"]

        # Numerize the prediction
        numerized_prediction = numerize.numerize(float(prediction), 2)
        # Display the prediction
        st.success(f"Predicted Market Price: {numerized_prediction} Euros!")

    except requests.exceptions.RequestException as e:
        st.error(f"Error making prediction: {e}")