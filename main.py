import argparse
from loader import load_csv_data
from clean import clean_data
from model import assign_roles, calculate_ADVANCED_value
from visualize import visualize


def main(file_path):
    # Load data
    data = load_csv_data(file_path)
    print(data.head())

    cleaned_data = clean_data(data)
    print(cleaned_data.head())

    role_assigned_data = assign_roles(cleaned_data)
    final_data = calculate_ADVANCED_value(role_assigned_data)
    print(final_data.head())

    # Visualize the roles
    visualize(final_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process NBA player stats.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file containing NBA player stats')
    args = parser.parse_args()

    main(args.file_path)
