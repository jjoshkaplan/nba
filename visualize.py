"""Display Top NBA Players by Role and NEW Statistic"""

import matplotlib.pyplot as plt


def visualize(df):
    """
    Visualize NEW statistic vs. MP for all roles with different colors
    :param df: Dataframe with player stats including roles
    """
    roles = ['BATMAN', 'ROBIN', 'ALFRED']
    colors = {'BATMAN': 'red', 'ROBIN': 'blue', 'ALFRED': 'green'}
    plt.figure(figsize=(12, 8))

    for role in roles:
        role_df = df[df['Role'] == role].sort_values(by='ADVANCED', ascending=False).head(15)
        plt.scatter(role_df['MP'], role_df['ADVANCED'],
                    alpha=0.7, edgecolors='w', s=100, label=role, color=colors[role])
        # Adding labels to each point
        for _, row in role_df.iterrows():
            plt.text(row['MP'], row['ADVANCED'], row['Player'], fontsize=8, ha='right')
    plt.xlabel('Minutes Played (MP)')
    plt.ylabel('ADVANCED Statistic')
    plt.title('ADVANCED Statistic vs. Minutes Played by Role')
    plt.legend(title='Role')
    plt.grid(True)
    plt.show()
