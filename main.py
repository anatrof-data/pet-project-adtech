from src.utils import ensure_directory_exists
from src.data_preprocessing import (
    load_data,
    transform_data,
    scale_features,
    handle_outliers,
    remove_correlated_features
)
from src.train import train_model
from src.evaluate import plot_training_history


def main():
    # Ensure directories exist
    ensure_directory_exists('models')
    ensure_directory_exists('data')

    file_path = 'data/dataset-adtech.csv'
    # Load data
    dataset = load_data(file_path)
    # Transform data
    dataset = transform_data(dataset)

    # Handle outliers
    columns_for_handle_outliers = [
        'total_impressions', 'viewable_impressions',
        'measurable_impressions', 'total_revenue'
    ]
    dataset = handle_outliers(dataset, columns_for_handle_outliers)

    # Correlation amalysis
    columns_for_corr_analysis = [
        'day', 'total_impressions', 'viewable_impressions',
        'measurable_impressions', 'total_revenue'
    ]
    remove_correlated_features(dataset, columns_for_corr_analysis)

    # Data scaling
    columns_for_scaling = [
        'site_id', 'ad_type_id', 'geo_id', 'device_category_id',
        'advertiser_id', 'order_id', 'line_item_type_id', 'os_id',
        'monetization_channel_id', 'ad_unit_id', 'total_impressions',
        'viewable_impressions', 'measurable_impressions',
        'total_revenue', 'day'
    ]
    dataset = scale_features(dataset, columns_for_scaling)

    # Train the model
    history = train_model(dataset)

    # Plot training history
    plot_training_history(history)


if __name__ == "__main__":
    main()
