import json
import sys

for line in sys.stdin:
    try:
        transaction = json.loads(line)
        
        # Simple rule: flag large transactions
        if transaction["amount"] > 5000:
            transaction["is_fraud"] = True
            print(f"🚨 Fraud detected: {transaction}")
        else:
            print(f"✅ Normal transaction: {transaction['amount']}")
            
    except Exception as e:
        print(f"Error: {e}")