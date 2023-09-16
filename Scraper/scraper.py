import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Define the directory to save the images
image_directory = 'zeBRa_mussel'
os.makedirs(image_directory, exist_ok=True)

# Set up Chrome WebDriver (you may need to adjust the path)
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# Define the URL of the Google Images search results page
google_images_url = 'https://www.google.com/search?q=zebra+mussEL+&tbm=isch&ved=2ahUKEwiStPX_zK-BAxWSM1kFHdcfBr0Q2-cCegQIABAA&oq=zebra+mussEL+&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6CAgAEIAEELEDOggIABCxAxCDAToKCAAQigUQsQMQQzoNCAAQigUQsQMQgwEQQzoHCAAQigUQQ1D9Clj7MGCUOWgDcAB4AIABtgKIAdkMkgEIMTAuNC4wLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=m94FZdL6MpLn5NoP17-Y6As&bih=955&biw=1920&rlz=1C1ONGR_enUS937US937'

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

# Extract and download each image
for idx, img_tag in enumerate(img_tags):
    # Get the source URL of the image
    img_url = img_tag.get('src') or img_tag.get('data-src')

    if img_url:
        # If the src attribute is relative, convert it to an absolute URL
        img_url = urljoin(google_images_url, img_url)

        # Get the image file name from the URL
        img_filename = os.path.join(image_directory, f"image_{idx + 1}.jpg")

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
            else:
                print(f"Failed to download: {img_url}")
        except requests.exceptions.RequestException as e:
            print(f"Error while downloading {img_url}: {e}")

# Quit the WebDriver
driver.quit()
