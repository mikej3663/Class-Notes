import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Pseudo Data Generation Function ---
def generate_pseudo_data(n_points, model_type, fold_type):
    np.random.seed(42)

    # Ticker Data
    actual_prices = np.random.randint(80, 180, n_points) + np.cumsum(np.random.normal(0, 2, n_points))
    if model_type == "Ridge":
        predictions = actual_prices + np.random.normal(0, 3, n_points)
    elif model_type == "Lasso":
        predictions = actual_prices + np.random.normal(0, 7, n_points)
    elif model_type == "HistGradientBoostingRegressor":
        predictions = actual_prices + np.random.normal(0, 4, n_points)
    elif model_type == "RandomForrest":
        predictions = actual_prices + np.random.normal(0, 6, n_points)
    else:
        predictions = actual_prices + np.random.normal(0, 5, n_points) # Default

    dates = pd.to_datetime(pd.date_range(start="2024-01-01", periods=n_points))
    df_prices = pd.DataFrame({"Date": dates, "Actual": actual_prices, "Predictions": predictions})

    # S&P 500 Data (for comparison) - Slight variation based on fold type
    if fold_type == "Rolling":
        sp500_actual = np.random.randint(1, 5, n_points) + np.cumsum(np.random.normal(0, 0.08, n_points))
        sp500_predictions = sp500_actual + np.random.normal(0, 0.15, n_points)
    elif fold_type == "Expanding":
        sp500_actual = np.random.randint(1, 5, n_points) + np.cumsum(np.random.normal(0, 0.12, n_points))
        sp500_predictions = sp500_actual + np.random.normal(0, 0.25, n_points)
    else:
        sp500_actual = np.random.randint(1, 5, n_points) + np.cumsum(np.random.normal(0, 0.1, n_points))
        sp500_predictions = sp500_actual + np.random.normal(0, 0.2, n_points)

    df_sp500 = pd.DataFrame({"Date": dates, "S&P 500 Actual": sp500_actual, "S&P 500 Predictions": sp500_predictions})

    # Metrics Data - Vary slightly based on model and fold
    if model_type == "Ridge" and fold_type == "Rolling":
        metrics_values = [7.5, 2.1, 0.95, 0.012]
    elif model_type == "Lasso" and fold_type == "Expanding":
        metrics_values = [9.0, 2.5, 0.93, 0.016]
    elif model_type == "HistGradientBoostingRegressor" and fold_type == "Rolling":
        metrics_values = [6.8, 1.9, 0.96, 0.011]
    elif model_type == "RandomForrest" and fold_type == "Expanding":
        metrics_values = [8.2, 2.3, 0.94, 0.015]
    else:
        metrics_values = [8.392, 2.222, 0.941, 0.014]

    metrics_data = {
        "Metrics": ["MSE", "MAE", "R²", "MAPE"],
        "Value": metrics_values,
    }
    df_metrics = pd.DataFrame(metrics_data)

    return df_prices, df_sp500, df_metrics

# --- Sidebar Controls ---
tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]
selected_ticker = st.sidebar.selectbox("Ticker", tickers) # Ticker selection (currently not affecting data)

model_types = ["Ridge", "Lasso", "HistGradientBoostingRegressor", "RandomForrest"]
selected_model = st.sidebar.selectbox("Model Type", model_types)

fold_types = ["Rolling", "Expanding"]
selected_fold = st.sidebar.selectbox("Fold Type (CV)", fold_types)

# --- Generate Data Based on Selections ---
df_prices, df_sp500, df_metrics = generate_pseudo_data(n_points, selected_model, selected_fold)

# --- Dashboard Layout ---
st.title("Neural Network Dashboard - Asset Pricing")

# Row 1: Predictions vs Actual
st.subheader("Predictions vs Actual")
fig_prices = px.line(df_prices, x="Date", y=["Predictions", "Actual"],
                     labels={"value": "Price", "Date": "Date"})
st.plotly_chart(fig_prices, use_container_width=True)

# Row 2: Predictions vs Actual vs S&P 500
st.subheader("Predictions vs Actual vs S&P 500")
df_comparison = df_prices.merge(df_sp500, on="Date")
fig_comparison = px.line(df_comparison, x="Date", y=["Predictions", "Actual", "S&P 500 Actual"],
                         labels={"value": "Value", "Date": "Date"})
fig_comparison.update_layout(legend_title_text="Legend")
st.plotly_chart(fig_comparison, use_container_width=True)

# Row 3: Metrics Table
st.subheader("Metrics")
st.dataframe(df_metrics, hide_index=True)
