import mlflow
import mlflow.keras
from sklearn.model_selection import train_test_split
from src.model import build_model


def train_model(dataset, batch_size=512, epochs=50):
    """
    Train the model and log the training process with MLflow.
    """
    # Splitting the data into features (X) and target variable (y)
    y = dataset['total_revenue']
    X = dataset.drop('total_revenue', axis=1)

    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

    # Creating the model
    model = build_model(input_shape=train_X.shape[1])

    # Setting up the experiment in MLflow
    mlflow.set_experiment("AdTech_Project")  # Set the experiment name

    with mlflow.start_run():  # Start logging the experiment
        # Logging parameters
        mlflow.log_param("batch_size", batch_size)
        mlflow.log_param("epochs", epochs)

        # Logging the model structure
        mlflow.log_param("model_structure",
                         model.summary(print_fn=lambda x: None))

        # Training the model
        history = model.fit(
            train_X, train_y,
            validation_data=(val_X, val_y),
            batch_size=batch_size,
            epochs=epochs
        )

        # Logging metrics
        # Final validation loss
        final_val_loss = history.history['val_loss'][-1]
        # Final validation MAE
        final_val_mae = history.history['val_mae'][-1]
        mlflow.log_metric("final_val_loss", final_val_loss)
        mlflow.log_metric("final_val_mae", final_val_mae)

        # Saving and logging the model
        model_path = 'models/trained_model.keras'
        model.save(model_path)
        mlflow.keras.log_model(model, artifact_path="model")

        from tensorflow.keras.models import load_model
        loaded_model = load_model(model_path)

        loaded_model.summary()

    return history
