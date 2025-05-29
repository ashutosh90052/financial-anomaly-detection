import matplotlib.pyplot as plt

def plot_anomalies(df):
    normal = df[df["anomaly"] == 0]
    anomaly = df[df["anomaly"] == 1]
    
    plt.figure(figsize=(10,6))
    plt.scatter(normal["hour"], normal["amount"], label="Normal", alpha=0.6)
    plt.scatter(anomaly["hour"], anomaly["amount"], label="Anomaly", color="red")
    plt.xlabel("Hour")
    plt.ylabel("Transaction Amount")
    plt.title("Anomaly Detection")
    plt.legend()
    plt.grid(True)
    plt.show()
