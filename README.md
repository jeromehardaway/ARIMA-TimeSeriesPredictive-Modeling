# ARIMA Prediction Tool

This Python script performs ARIMA (Autoregressive Integrated Moving Average) time series analysis on a given CSV file and generates predictions for each column. The script uses the `pandas` library for data handling, `statsmodels` for ARIMA modeling, and `sklearn` for evaluating the predictions.

## Installation

1. Clone this repository or download the script directly.
2. Make sure you have Python 3.x installed on your system.
3. Install the required dependencies by running the following command:
   
``````
pip install pandas statsmodels scikit-learn
``````

## Usage

1. Place your CSV file in the same directory as the script. Ensure that the file contains numerical data.
2. Open the script file (`arima_prediction.py`) in a text editor.
3. Replace `'pathto.csv'` with the actual path to your CSV file in the `csv_file_path` variable.
4. (Optional) If you want to limit the number of columns processed, modify the `num_columns` variable to the desired value.
5. Save the changes to the script file.
6. Open a terminal or command prompt and navigate to the script's directory.
7. Run the following command to execute the script:

``````
python arima_prediction.py
``````
8. The script will generate predictions for each column in the CSV file and display them in the terminal.
9. The predictions will be saved in a file named `predictions.csv` in the same directory.

## Customization

- If you want to change the order of the ARIMA model or the number of forecast steps, you can modify the `order` and `forecast_steps` parameters in the `fit_arima()` function within the script.
- If you need further customization or advanced usage, refer to the documentation of the libraries used: [pandas](https://pandas.pydata.org/), [statsmodels](https://www.statsmodels.org/), and [scikit-learn](https://scikit-learn.org/stable/).

Feel free to reach out if you have any questions or encounter any issues while using this tool.
