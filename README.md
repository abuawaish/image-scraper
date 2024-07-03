# Image Scraper and Downloader

**This is a Flask web application that allows users to search for images on Unsplash and download them.**

# Functionality

- 1. The user can enter a search query on the index page, which is then sent to the `/scrape` route using a POST request.

- 2. The `/scrape` route uses the `requests` library to fetch the search results from `Unsplash`, and the `BeautifulSoup` library to parse the HTML content and extract the image URLs.

- 3. The images are then downloaded and saved to a local directory `(C:/Images)` on the server.

- 4. The application generates a list of URLs for the downloaded images and renders them on a separate `download.html` template.

- 5. The user can then click on the image URLs to download the corresponding images using the `/download/<filename>` route, which serves the images from the local directory.

# Requirements
- Python 3
- Flask
- Requests
- BeautifulSoup4

# Usage

- Enter a search query in the input field on the index page.
- Click the "Scrape" button to initiate the image search and download process.
- The downloaded images will be displayed on the download.html page.
- Click on the image URLs to download the corresponding images.
