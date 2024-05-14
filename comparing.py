from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import httpx
import multiprocessing
from flask import Flask


url = "https://www.capitoltrades.com/issuers?per_page=96&sortBy=-countPoliticians"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Make an HTTP request using httpx
response = httpx.get(url, headers=headers)

giants_httpx = {}  # Define the dictionary for httpx outside the loop

if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup_httpx = BeautifulSoup(response.text, 'html.parser')

    member_names_httpx = [member.text.strip() for member in soup_httpx.select('.q-field.countPoliticians')]
    company_names_httpx = [company.text.strip() for company in soup_httpx.select('.q-fieldset.issuer-name')]

    for index, name in enumerate(member_names_httpx):
        # Convert the string to an integer
        num_politicians_httpx = int(name)

        print(f"Company (httpx): {company_names_httpx[index]}, Politicians: {num_politicians_httpx}")

        if num_politicians_httpx > 20:
            print(f"The Company {company_names_httpx[index]} has 20 or more politicians invested")
            giants_httpx[num_politicians_httpx] = company_names_httpx[index]

    print("Giants dictionary (httpx):", giants_httpx)
else:
    print(f"Failed to retrieve the page using httpx. Status code: {response.status_code}")

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

# Initialize the webdriver
driver = webdriver.Chrome(options=chrome_options)

# Make an HTTP request using Selenium
driver.get(url)

# Wait for dynamic content to load (you might need to adjust the sleep time)
time.sleep(5)

# Get the page source after dynamic content has loaded
page_source = driver.page_source

# Parse the HTML content with BeautifulSoup
soup_selenium = BeautifulSoup(page_source, 'html.parser')

giants_selenium = {}  # Define the dictionary for Selenium outside the loop

member_names_selenium = [member.text.strip() for member in soup_selenium.select('.q-field.countPoliticians')]
company_names_selenium = [company.text.strip() for company in soup_selenium.select('.q-fieldset.issuer-name')]


#####KEY TO FIND ALL NUMBERS 
missing_members_selenium = [missing.text.strip() for missing in soup_selenium.select('.q-cell.cell--count-politicians')]

for index, name in enumerate(member_names_selenium):
    num_politicians_selenium = int(name)

    if num_politicians_selenium > 20:
        giants_selenium[num_politicians_selenium] = company_names_selenium[index]

# Sort the dictionary based on keys (number of politicians)
sorted_giants_selenium = dict(sorted(giants_selenium.items()))

print("Sorted Giants dictionary (Selenium):", sorted_giants_selenium)
print(f"Possible missing companies (Selenium): {missing_members_selenium} !!!!!!!!!!!!!!!!!!!!!!!")

# Combine the two dictionaries and remove duplicates
combined_giants = {**sorted_giants_selenium, **giants_httpx}

# Remove duplicates
unique_combined_giants = dict(sorted(set(combined_giants.items())))

print("Combined and unique Giants dictionary:")
for key, value in unique_combined_giants.items():
    print(f"{key}: {value}")

# Close the webdriver
driver.quit()
























