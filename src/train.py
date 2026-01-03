from load_data import load_cmapss_data
from features import add_temperature_features
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def main():
    # Load data
    df = load_cmapss_data("data/train_FD001.txt")

    # Feature engineering
    df = add_temperature_features(df)

    # Define X and y
    features = (
        [f"sensor_{i}_lag1" for i in [2, 3, 4, 11]] +
        ["avg_temp_lag1", "os_1", "os_2", "os_3", "cycle"]
    )

    X = df[features]
    y = df["avg_temp"]

    # Time-aware split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)

    mse_lr = mean_squared_error(y_test, y_pred_lr)
    rmse_lr = np.sqrt(mse_lr)
    print(f"Linear Regression RMSE: {rmse_lr:.2f} °C")

    # Random Forest
    rf = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    
#Visulizing the data from Random Forest 
    N = 200
    plt.figure(figsize=(10, 4))

    plt.plot(
    y_test.values[:N],
    label="Actual Temperature",
    linewidth=2
)
    plt.plot(
    y_pred_rf[:N],
    label="Predicted Temperature",
    linestyle="--"
)
    plt.xlabel("Time (Cycles)")
    plt.ylabel("Average Temperature (°C)")
    plt.title("Actual vs Predicted Rotor Temperature")
    plt.legend()
    plt.grid(True)

    plt.show()

    mse_rf = mean_squared_error(y_test, y_pred_rf)
    rmse_rf = np.sqrt(mse_rf)
    print(f"Random Forest RMSE: {rmse_rf:.2f} °C")

if __name__ == "__main__":
    main()
