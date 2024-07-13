""" Clean data from raw .csv file to remove statistics that will not be used in calculation of a new model"""


def clean_data(df):
    """ prepare dataframe for modeling and visualization"""
    # Identify unnecessary columns
    columns_to_drop = ['Rk',
                       'Pos',
                       '3PAr',
                       'FTr',
                       'ORB%',
                       'DRB%',
                       'TRB%',
                       'AST%',
                       'STL%',
                       'BLK%',
                       'TOV%',
                       'OWS',
                       'DWS',
                       'WS/48',
                       'OBPM',
                       'DBPM',
                       'Player-additional']
    # Drop listed columns
    df = df.drop(columns=columns_to_drop)

    # Identify players listed multiple times
    duplicate_players = df[df.duplicated(subset=['Player'], keep=False)]

    # Filter out rows where Tm is not TOT for duplicate players
    df_cleaned = df[~((df['Player'].isin(duplicate_players['Player'])) & (df['Tm'] != 'TOT'))]

    # Drop players who played fewer than 20 games
    df_cleaned = df_cleaned[df_cleaned['G'] >= 20]

    return df_cleaned
