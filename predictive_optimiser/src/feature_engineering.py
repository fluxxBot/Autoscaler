import pandas as pd

def create_lag_features(df, lags=3):
    for lag in range(1, lags + 1):
        df[f'lag_{lag}'] = df['y'].shift(lag)
    return df

def prepare_data(file_path):
    data = pd.read_csv(file_path, parse_dates=['timestamp'])
    data.rename(columns={'timestamp': 'ds', 'instance_count': 'y'}, inplace=True)
    data = create_lag_features(data, lags=3)
    data = data.dropna()
    return data

if __name__ == "__main__":
    data = prepare_data('data/autoscaler_dataset.csv')
    print(data.head())
