from sklearn.model_selection import train_test_split
from src.model import build_model


def train_model(dataset, batch_size=512, epochs=50):
    """
    Train the model and return the training history.
    """
    y = dataset['total_revenue']
    X = dataset.drop('total_revenue', axis=1)

    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

    model = build_model(input_shape=train_X.shape[1])

    history = model.fit(
        train_X, train_y,
        validation_data=(val_X, val_y),
        batch_size=batch_size,
        epochs=epochs
        )
    model.save('models/trained_model.keras')

    return history
