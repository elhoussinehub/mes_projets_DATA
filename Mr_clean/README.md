# Welcome to My Mr Clean
***
## Task
The problem is to build a simple search engine for EncyclEarthpedia, an online encyclopedia about Earth. 
The challenge is that the real database and API are unavailable, so we must work with Wikipedia articles instead and implement content extraction, 
cleaning, tokenization, and frequency analysis to simulate a search engine.
## Description
We solved the problem by:
Retrieving article content from Wikipedia using the API (without external libraries like wikipedia).
Extracting and merging the meaningful content from the JSON response.
Cleaning and tokenizing the text into words.
Converting all words to lowercase for consistency.
Counting the frequency of each word to build a simple frequency model.
Filtering out stop words to focus on relevant keywords.
Visualizing the most frequent words with histograms to understand the content distribution.
This approach forms a basic proof of concept for a search engine, using term frequency as a simple ranking method.
## Installation
No special installation is required beyond Python 3. You just need to ensure you have requests and BeautifulSoup installed:
pip install requests beautifulsoup4
## Usage
Run the main script to fetch, process, and analyze a Wikipedia article:
python main.py "Ozone_layer"
This will output:
The raw content of the article
Tokenized and cleaned words
Frequency counts of words
Filtered frequent words
### The Core Team
El Houssine El Malki
Abdllah Boukadda
