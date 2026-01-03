import matplotlib.pyplot as plt

def plot_predictions(y_true, y_pred, n=200):
    plt.figure(figsize=(10, 4))
    plt.plot(y_true.values[:n], label="Actual")
    plt.plot(y_pred[:n], label="Predicted")
    plt.legend()
    plt.title("Rotor Temperature Prediction")
    plt.show()
