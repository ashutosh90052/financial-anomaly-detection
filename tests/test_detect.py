import pandas as pd
import pytest
from app.anomaly_detection import detect_anomalies

def test_detect_anomalies_basic():
    # Create a sample DataFrame with one outlier
    data = pd.DataFrame({
        'amount': [10, 12, 11, 13, 14, 1000]  # 1000 is an outlier
    })

    # Call the anomaly detection function
    anomalies = detect_anomalies(data, threshold=2.0)

    # Ensure that the output is not empty
    assert not anomalies.empty

    # Check if the detected anomaly is the expected one
    assert 1000 in anomalies['amount'].values
    assert len(anomalies) == 1
