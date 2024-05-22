import pandas as pd

# Load data from database
data = pd.read_sql('SELECT * FROM solar_data', con=your_database_connection)

# Descriptive statistics
print(data.describe())

# Time series analysis
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)

# Plot voltage over time
data['voltage'].plot()

# Predictive analytics using machine learning (e.g., Linear Regression)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Feature selection
features = data[['voltage', 'temperature', 'light_intensity']]
target = data['current']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluate the model
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

