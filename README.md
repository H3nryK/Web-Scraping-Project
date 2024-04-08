# Web-Scraping-Project

This project demonstrates how to scrape data from a website using Python and BeautifulSoup library.

## Introduction

Web scraping is the process of extracting data from websites. This project showcases a simple web scraping script written in Python using the BeautifulSoup library. The script retrieves various pieces of information from a specified website, such as the page title, headings, paragraphs, and links, and saves the data to a CSV file for further analysis.

## Prerequisites

Before running the web scraping script, make sure you have the following installed:
- Python 3.11^
- BeautifulSoup library
  ```bash
  pip install beautifulsoup4
- Requests library
  ```bash
  pip install requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/H3nryK/Web-Scraping-Project.git
2. Navigate to the project directory:
   ```bash
   cd Web-Scraping-Project

## Usage

1. Change the url value with the website url you want to scrape:
   ```bash
   import requests
   from bs4 import BeautifulSoap

   url = " "

   ...(rest of teh code)...
2. Run the project:
   ```bash
   py scrape.py
3. The scraped data will be saved to a CSV file named scraped_data.csv

## Features

Retrieves page title, headings, paragraphs, and links from a website.
Saves the scraped data to a CSV file for further analysis.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or new features to add, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License.

