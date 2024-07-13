# NBA Player Analysis Project

This project analyzes NBA player statistics to categorize players based on their roles (BATMAN, ROBIN, and ALFRED) and calculates a new performance metric called `NEW`. The project includes data loading, cleaning, processing, modeling, and visualization.

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

## Installation

Install the required packages:
    
 - **pip install pandas**
 - **pip install matplotlib**

## Running the Project

Load the data:

Ensure the CSV file is placed in the correct path or modify the path in main.py.

Run the main script:
python main.py