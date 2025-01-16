"""
Model for predicting reserve prices in an auction.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras import Input, Sequential
from tensorflow.keras.layers import Dense

# Load the data
# Ensure the CSV files are in the correct path or modify accordingly.
y = pd.read_csv('dataset_y.csv')
X = pd.read_csv('dataset_X.csv')

# Split the data into training and validation sets
train_features, val_features, train_labels, val_labels = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Build the neural network model
model = Sequential([
    Input(shape=(train_features.shape[1],)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mae')

# Train the model
history = model.fit(
    train_features, train_labels,
    validation_data=(val_features, val_labels),
    batch_size=512,
    epochs=50,
    verbose=1
)

# Save the trained model
model.save('trained_model.keras')

print("Model training completed and saved as 'trained_model.keras'.")
