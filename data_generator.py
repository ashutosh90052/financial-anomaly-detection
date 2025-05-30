import json
import random
import time
from datetime import datetime

while True:
    # Generate a fake transaction
    transaction = {
        "transaction_id": random.randint(100000, 999999),
        "amount": round(random.uniform(10, 10000), 2),
        "timestamp": datetime.now().isoformat(),
        "user_id": f"user_{random.randint(1, 100)}",
        "is_fraud": random.random() < 0.05  # 5% are fraud
    }
    
    print(json.dumps(transaction))
    time.sleep(0.5)  # 2 transactions per second