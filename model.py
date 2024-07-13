""" Assign roles for each player based on USG% and calculate Advanced Metric """

import pandas as pd


def assign_roles(df):
    """
    Assign roles based on USG% (Usage Percentage)
    :param df: Dataframe with player stats
    :return: Dataframe with new 'Role' column
    """
    # Establish and Assign Role Percentile
    usg_percentiles = df['USG%'].quantile([0.2, 0.4]).values
    df['Role'] = pd.cut(df['USG%'], bins=[-float('inf'), usg_percentiles[0],
                                          usg_percentiles[1], float('inf')],
                        labels=['ALFRED', 'ROBIN', 'BATMAN'])
    return df


def calculate_advanced_value(df):
    """
    Calculate new value based on weighted combination of PER, TS%, WS, BPM, and VORP
    :param df: Dataframe with player stats
    :return: Dataframe with Advanced Metric
    """
    # Define weights for each column
    weights = {
        'PER': 0.2,
        'TS%': 0.2,
        'WS': 0.2,
        'BPM': 0.2,
        'VORP': 0.2
    }

    # Calculate NEW value
    df['ADVANCED'] = (df['PER'] * weights['PER'] +
                 df['TS%'] * weights['TS%'] +
                 df['WS'] * weights['WS'] +
                 df['BPM'] * weights['BPM'] +
                 df['VORP'] * weights['VORP'])

    return df


def process_data(df):
    """
    Process data by assigning roles, calculating the new value, and splitting the data frame
    :param df: Dataframe with player stats
    :return: Tuple of processed dataframe and dataframes for each role
    """
    df = assign_roles(df)
    df = calculate_advanced_value(df)

    # Split the dataframe into three based on the Role
    batman_df = df[df['Role'] == 'BATMAN'].sort_values(by='ADVANCED', ascending=False)
    robin_df = df[df['Role'] == 'ROBIN'].sort_values(by='ADVANCED', ascending=False)
    alfred_df = df[df['Role'] == 'ALFRED'].sort_values(by='ADVANCED', ascending=False)

    return batman_df, robin_df, alfred_df
