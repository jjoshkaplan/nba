# NBA Player Analysis Project

This project analyzes NBA player statistics to categorize players based on their roles (BATMAN, ROBIN, and ALFRED) and calculates a new performance metric called `ADVANCED`. The project includes data loading, cleaning, processing, modeling, and visualization.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Project Overview

The NBA Player Analysis Project is designed to:

1. **Load Data**: Read player statistics from a CSV file.
2. **Clean Data**: Remove unnecessary columns and filter players with fewer than 20 games played.
3. **Process Data**: Assign roles to players based on usage percentage (USG%) and calculate a new performance metric (`ADVANCED`) using PER, TS%, WS, BPM, and VORP.
4. **Visualize Data**: Generate scatter plots of the top 15 players in each role, displaying their ADVANCED statistic versus minutes played (MP).

This analysis is meant to assist the user in evaluating players across different roles. In order for a team to be successful, they can't simply rely on their star player. A successful team has different players with different skills playing a variety of roles. 

## Installation

Install the required packages:
    
 - **pip install pandas**
 - **pip install matplotlib**

### Steps

1. **Clone the repository**:
   ```
   git clone https://github.com/jjoshkaplan/nba.git

2. **Navigate to the project directory**:
   ```
   cd nba
   
3. **Create a virtual environment**:
   ```
   python -m venv venv

### Data Files

You will need an NBA player statistics CSV file to run the analysis. Ensure your CSV file contains the necessary columns such as player names, usage percentages (USG%), PER, TS%, WS, BPM, and VORP. This file can be located at https://www.basketball-reference.com/ and found for any year. Can also analyze the regular season or playoffs!

## Usage

Prepare your CSV data file: Ensure you have the NBA player statistics CSV file ready.

#### Run the analysis:

   ```
   python main.py --file_path path_to_your_csv_file.csv
   ```
#### View the results: 

The script will output the cleaned data and generate visualizations for the top players based on their roles by color.

## File Structure

loader.py: Contains the function to load data from a CSV file.

clean.py: Contains functions to clean the data and assign roles based on USG%.

process_data.py: Contains functions to calculate the new performance metric (ADVANCED).

visualize.py: Contains functions to visualize the data.

main.py: The main script to run the entire analysis.

requirements.txt: Lists the required packages for the project.
