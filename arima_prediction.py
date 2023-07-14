import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Function to round the values in a series to the nearest whole number
def round_series(series):
    return series.apply(round)

# Function to fit ARIMA model and make predictions for a series
def fit_arima(series, order=(5, 1, 0), forecast_steps=3):
    model = ARIMA(series, order=order)
    model_fit = model.fit()
    output = model_fit.forecast(steps=forecast_steps)
    predictions = round_series(output)
    return predictions

# Read the CSV file
csv_file_path = 'pathto.csv'  # replace with your actual csv file path
df = pd.read_csv(csv_file_path)

# Prepare a DataFrame to store the predictions
predictions = pd.DataFrame()

# Fit model and make predictions for each column
num_columns = min(6, df.shape[1])  # Limit to a maximum of 6 columns
for i in range(num_columns):
    series = df.iloc[:, i]
    column_name = f'Column {i+1}'
    predicted_values = fit_arima(series)
    predictions[f'Predicted future values for {column_name}'] = predicted_values

# Print and save the predictions
print(predictions)
output_file_path = 'predictions.csv'
predictions.to_csv(output_file_path, index=False)
print(f"Predictions saved to '{output_file_path}'")
