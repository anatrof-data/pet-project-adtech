import matplotlib.pyplot as plt
import pandas as pd


def plot_training_history(history):
    """Plot the training and validation loss over epochs."""
    history_df = pd.DataFrame(history.history)
    history_df[['loss', 'val_loss']].plot()
    plt.title('Model Loss Over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend(['Training Loss', 'Validation Loss'])
    plt.show()
