import pandas as pd
import xgboost as xgb
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_and_save_model(data_path, model_path):
    # Load data
    data = pd.read_csv(data_path)
    
    # Ensure target variable is integer
    data['instance_count'] = data['instance_count'].astype(int)
    
    # Prepare data for training
    X = data[['cpu_usage', 'memory_usage', 'status_code']]
    y = data['instance_count']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = xgb.XGBRegressor(objective='reg:squarederror')
    model.fit(X_train, y_train)
    
    # Predict on test data
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    # Save the model
    joblib.dump(model, model_path)
    print("Model trained and saved successfully.")

if __name__ == "__main__":
    train_and_save_model('data/autoscaler_dataset.csv', 'models/xgboost_model.pkl')
