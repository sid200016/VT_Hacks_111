import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set up Chrome WebDriver (you may need to adjust the path)
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# Read search terms from the text file
with open('search_terms.txt', 'r') as file:
    search_terms = file.read().splitlines()

# Loop through each search term
for search_term in search_terms:
    # Initialize a counter for downloaded images for the current search term
    downloaded_count = 0

    # Create a directory to save the images for the current search term
    image_directory = os.path.join('Google_Images_Search', search_term)
    os.makedirs(image_directory, exist_ok=True)

    # Continue downloading images until 50 are downloaded
    while downloaded_count < 50:
        # Define the Google Images search URL for the current term
        google_images_url = f'https://www.google.com/search?q={search_term}&tbm=isch'

        # Open the Google Images search results URL in the Chrome browser
        driver.get(google_images_url)

        # Scroll down to load more images (adjust the number of scrolls as needed)
        for _ in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Add a delay to allow images to load

        # Get the page source after scrolling
        page_source = driver.page_source

        # Parse the HTML content of the page
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find all image tags (usually <img>) in the HTML
        img_tags = soup.find_all('img')

        # Extract and download up to 50 images for the current term
        for idx, img_tag in enumerate(img_tags):
            if downloaded_count >= 50:
                break  # Stop downloading when 50 images are downloaded

            # Get the source URL of the image
            img_url = img_tag.get('src') or img_tag.get('data-src')

            if img_url:
                # If the src attribute is relative, convert it to an absolute URL
                img_url = urljoin(google_images_url, img_url)

                # Get the image file name from the URL
                img_filename = os.path.join(image_directory, f"image_{downloaded_count + 1}.jpg")

                # Send an HTTP GET request to the image URL with a user-agent header
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                }
                try:
                    img_response = requests.get(img_url, headers=headers, stream=True)
                    time.sleep(1)  # Add a delay to be polite to the server

                    # Check if the request was successful (status code 200)
                    if img_response.status_code == 200:
                        # Save the image to the local directory
                        with open(img_filename, 'wb') as img_file:
                            for chunk in img_response.iter_content(chunk_size=8192):
                                img_file.write(chunk)
                        print(f"Downloaded: {img_filename}")
                        downloaded_count += 1
                    else:
                        print(f"Failed to download: {img_url}")
                except requests.exceptions.RequestException as e:
                    print(f"Error while downloading {img_url}: {e}")

# Quit the WebDriver
driver.quit()
