# Welcome to My First Scraper Ds
***
## Task
The goal of this project is to scrape GitHub trending repositories from a given URL, extract relevant information such as developer name, repository name, and number of stars, transform the data into a structured format, and save it as a CSV file.
The main challenge is correctly parsing the HTML and handling numbers formatted with commas.
## Description
This project solves the problem in four main steps:
Request: Fetch the HTML content of the trending repositories page using requests.
Extract: Parse the HTML with BeautifulSoup to find all repository rows.
Transform: Extract the developer name, repository name, and number of stars, clean the data, and store it in a list of dictionaries.
Format: Write the data to a CSV file using csv.DictWriter.
## Installation
Make sure Python 3 is installed.
Install the required packages:
pip install requests beautifulsoup4
## Usage
Run the script directly:
python your_script.p
It will fetch the trending repositories from the provided URL and create a CSV file csv-file.csv with the extracted data.
### The Core Team
El houssine El malki
Ayoub El fakhari
