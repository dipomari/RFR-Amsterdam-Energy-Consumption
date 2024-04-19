import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model/PATH/best_model.joblib')

# Create a function to take input as a DataFrame and return predictions
def predict(input_data):
    # input_data should be a DataFrame with columns named correctly
    return model.predict(input_data)[0]

# Define the column names as they were during model training
column_names = ['num_connections', 'delivery_perc', 'annual_consume_lowtarif_perc',
                'perc_of_active_connections', 'smartmeter_perc', 'number_amperage',
                'number_fuses', 'zipcode_processed']


inputs = {
    'num_connections': st.number_input('Number of Connections', min_value=0.0, format='%.2f'),
    'delivery_perc': st.number_input('Delivery Percentage', min_value=0.0, max_value=100.0, format='%.2f'),
    'annual_consume_lowtarif_perc': st.number_input('Low Tarif Consumption Percentage', min_value=0.0, max_value=100.0, format='%.2f'),
    'perc_of_active_connections': st.number_input('Percentage of Active Connections', min_value=0.0, max_value=100.0, format='%.2f'),
    'smartmeter_perc': st.number_input('Smart Meter Percentage', min_value=0.0, max_value=100.0, format='%.2f'),
    'number_amperage': st.number_input('Number of Amperage', min_value=1, format='%d'),
    'number_fuses': st.number_input('Number of Fuses', min_value=1, format='%d'),
    'zipcode_processed': st.text_input('Zipcode Processed')
}

# Convert inputs to DataFrame
input_df = pd.DataFrame([inputs], columns=column_names)

# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_df)
    st.write(f'Estimated Annual Energy Consumption: {prediction:.2f} kWh')
