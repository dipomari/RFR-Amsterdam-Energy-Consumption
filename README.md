
# RFR Amsterdam Energy Consumption Forecast

## Overview
This project focuses on developing an advanced predictive model to forecast energy consumption within Amsterdam. It employs machine learning techniques using a comprehensive dataset that encompasses infrastructural metrics collected from 2009 to 2020. By accurately predicting energy usage, this model aids in informing sustainable energy management and policy decisions.

## Dataset
The dataset used for this study includes various infrastructural metrics and spans from the years 2009 to 2020, reflecting the consumption patterns within Amsterdam. Access the dataset through this [Google Drive link](https://drive.google.com/file/d/1GpXqhv_ROWwRsiMM5r2aeA_hnhB5Eir7/view?usp=share_link).

## Model Usage
To utilize the pre-trained model for consumption forecasting:

1. Download the model from the provided Google Drive link.
2. Update the model path in `02_AI Annual Consumption Predictor.py`:
   ```python
   model = joblib.load('model/PATH/best_model.joblib')
   ```
3. Install the required dependencies (preferably in a virtual environment):
   ```shell
   pip install -r requirements.txt
   ```
4. Run the application with Streamlit by executing the following command in your terminal:
   ```shell
   streamlit run Main\ Page.py
   ```

## Key Insights
- The adoption of smart meters is inversely related to the average annual energy consumption, suggesting a potential impact on energy efficiency improvements.
- A significant finding is the increase in electricity usage during low tariff hours, especially notable between 2019 and 2020, likely influenced by the COVID-19 lockdowns.
- The project's model, based on the Random Forest Regressor algorithm, has been optimized with Optuna, resulting in a model that balances complexity with accuracy.

## Future Directions
The research underpinning this model will continue to evolve. Upcoming studies will explore the COVID-19 impact more deeply and integrate additional features to lower predictive errors further.
