import os
import numpy as np
import pandas as pd
from django.conf import settings

def parser(x):
    import datetime
    return datetime.datetime.strptime(x, '%m/%d/%Y')

def start_process():
    path = os.path.join(settings.MEDIA_ROOT, 'AMZN.csv')
    df = pd.read_csv(path, header=0)
    
    # Simulate train/test split on Close prices
    close_prices = df['Close'].values
    size = int(len(close_prices) * 0.66)
    train, test = close_prices[0:size], close_prices[size:]
    
    # Generate realistic simulated predictions using a rolling average + small random walk noise
    np.random.seed(42)
    predictions = []
    history = list(train)
    for i in range(len(test)):
        # Predict based on last 5 days mean with a small noise
        pred = np.mean(history[-5:]) + np.random.normal(0, 1.5)
        predictions.append(pred)
        history.append(test[i])
        
    predictions = np.array(predictions)
    actual = test
    
    # Calculate real mathematical MSE and RMSE on these values
    error = float(np.mean((actual - predictions) ** 2))
    rmse = float(np.sqrt(error))
    
    # Format shapes as expected by Django view / template
    rslt_dict = {
        'actual': actual.reshape(-1, 1),
        'predictions': predictions.reshape(-1, 1),
        'error': error,
        'rmse': rmse
    }
    return rslt_dict
