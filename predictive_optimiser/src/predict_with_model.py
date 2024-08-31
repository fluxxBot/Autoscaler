import pandas as pd
import numpy as np
import joblib
import os


def generate_test_data(num_samples=5):
    start_time = pd.Timestamp.now()
    timestamps = [start_time + pd.Timedelta(seconds=i*60) for i in range(num_samples)]
    cpu_usage = np.random.uniform(10, 90, num_samples)  # Ensure np.random is used correctly
    memory_usage = np.random.uniform(30, 95, num_samples)
    status_codes = np.random.choice([200, 404, 500], num_samples, p=[0.85, 0.1, 0.05])
    dataset = pd.DataFrame({
        'timestamp': timestamps,
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'status_code': status_codes
    })
    return dataset

def predict_with_model(model_path, output_file):
    # Load the model
    model = joblib.load(model_path)
    
    # Generate test data
    test_data = generate_test_data(1)
    
    # Prepare data for prediction
    X_test = test_data[['cpu_usage', 'memory_usage', 'status_code']]
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Convert predictions to integers
    y_pred = y_pred.astype(int)


    for i, pred in enumerate(y_pred):
      print(f"Predicted instance count = {pred}")


    output_lines = []
    for timestamp, pred in zip(test_data['timestamp'], y_pred):
        output_lines.append(f"{pred}")

    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    output_path = os.path.join(root_dir, output_file)
    
    
    with open(output_file, 'w') as file:
        file.write("\n".join(output_lines))
    
    print(f"Predictions saved to {output_file}")

if __name__ == "__main__":
    predict_with_model('models/xgboost_model.pkl', 'output.txt')
