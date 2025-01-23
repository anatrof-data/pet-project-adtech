from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense


def build_model(input_shape):
    """Build and return a neural network model."""
    model = Sequential([
        Dense(128, activation='relu', input_shape=[input_shape]),
        Dense(64, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mae', metrics=['mae'])
    return model
