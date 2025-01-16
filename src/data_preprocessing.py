import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(file_path):
    """Load the dataset from the specified CSV file."""
    dataset = pd.read_csv(file_path)
    return dataset


def transform_data(dataset):
    """
    Preprocess the dataset: remove columns, create features
    """
    dataset = dataset.drop(['integration_type_id',
                            'revenue_share_percent'], axis=1)
    dataset['date'] = pd.to_datetime(dataset['date'])
    dataset['year'] = dataset['date'].dt.year
    dataset['month'] = dataset['date'].dt.month
    dataset['day'] = dataset['date'].dt.day
    dataset = dataset.drop(['date', 'year', 'month'], axis=1)
    return dataset


def scale_features(dataset, columns):
    """Scale the specified columns using StandardScaler."""
    scaler = StandardScaler()
    dataset[columns] = scaler.fit_transform(dataset[columns])
    return dataset


def handle_outliers(dataset, columns):
    """
    Handle outliers by capping them to 3 standard deviations from the mean.
    """
    for column in columns:
        upper_boundary = dataset[column].mean() + 3 * dataset[column].std()
        print(f"{column} outliers are values > {upper_boundary}")
        dataset.loc[dataset[column] > upper_boundary, column] = upper_boundary
    return dataset


def remove_correlated_features(dataset, columns, threshold=0.9):
    """
    Remove features that are highly correlated with others
    above a given threshold.
    """
    selected_data = dataset[columns]
    corr_matrix = selected_data.corr(method='spearman').abs()
    mask = ~np.tril(np.ones(corr_matrix.shape)).astype(bool)
    upper_triangle = corr_matrix.where(mask)

    to_drop = [
        column for column in upper_triangle.columns
        if any(upper_triangle[column] > threshold)
    ]
    print(f"Removing correlated features: {to_drop}")
    return dataset.drop(columns=to_drop, axis=1)
