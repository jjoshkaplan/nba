""" Transform raw data to calculate advanced metric and visualize """

import argparse
from loader import load_csv_data
from clean import clean_data
from model import assign_roles, calculate_advanced_value
from visualize import visualize


def main(file_path):
    """
    load, clean, model, and visualize data from .csv file path
    :param file_path:
    :return: graph
    """
    # Load data
    data = load_csv_data(file_path)
    print(data.head())

    # Clean data
    cleaned_data = clean_data(data)
    print(cleaned_data.head())

    # Model data
    role_assigned_data = assign_roles(cleaned_data)
    final_data = calculate_advanced_value(role_assigned_data)
    print(final_data.head())

    # Visualize Advanced Metric by Role
    visualize(final_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process NBA player stats.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    main(args.file_path)
