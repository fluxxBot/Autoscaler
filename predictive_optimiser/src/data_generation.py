import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_autoscaler_data(num_samples=1000):
    start_time = datetime.now()
    timestamps = [start_time + timedelta(seconds=i*60) for i in range(num_samples)]
    cpu_usage = np.random.uniform(10, 90, num_samples)
    memory_usage = np.random.uniform(30, 95, num_samples)
    status_codes = np.random.choice([200, 404, 500], num_samples, p=[0.85, 0.1, 0.05])
    instance_count = np.random.randint(1, 50, num_samples)  # Ensure integer values
    dataset = pd.DataFrame({
        'timestamp': timestamps,
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'status_code': status_codes,
        'instance_count': instance_count
    })
    return dataset

if __name__ == "__main__":
    data = generate_autoscaler_data()
    data.to_csv('data/autoscaler_dataset.csv', index=False)
