import requests
from bs4 import BeautifulSoup
import csv

# URL of the website
url = 'https://milimanihighschool.co.ke'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract data
    title = soup.title.text.strip()
    headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    paragraphs = [paragraph.text.strip() for paragraph in soup.find_all('p')]
    links = [link['href'] for link in soup.find_all('a', href=True)]
    
    # Save the data to a CSV file
    csv_file = 'scraped_data.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Headings', 'Paragraphs', 'Links'])
        writer.writerow([title, '; '.join(headings), '; '.join(paragraphs), '; '.join(links)])
    
    print(f"Data has been scraped and saved to '{csv_file}'.")
else:
    print('Failed to retrieve the webpage')
