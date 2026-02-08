# Welcome to My M And A
***

## Task

The goal of this project is to merge multiple customer datasets coming from different CSV sources into a single, clean, and unified database.
The main challenge is handling inconsistent data formats, cleaning and normalizing fields, and ensuring that all data follows the same schema before storing it in a SQL database.

## Description

The problem is solved by loading the CSV contents into dataframes, cleaning and standardizing the data (such as column names and values), and then merging all datasets into one.
The final merged dataset is exported and inserted into a SQL database using a dedicated utility function.

## Installation

No external installation is required beyond Python and its dependencies.
Make sure the required Python libraries are installed:

pip install pandas

## Usage

Run the project by calling the merge function with the CSV contents, then export the result to SQL:

./my_project argument1 argument2

### The Core Team

EL HOUSSINE EL MALKI
Abdllah Boukadda
