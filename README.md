# Unsplash Image Scraper

A Flask web application for searching images on Unsplash and downloading the returned results locally.

## Features

- 🔍 Search Unsplash images using a text query
- ⬇️ Download saved images directly from the browser
- 🌐 AJAX-powered search for faster page updates
- 📁 Downloads are stored locally on your machine
- 🎨 Clean responsive UI with image gallery cards

## How it works

1. User enters a search term on the main page
2. The form submits via AJAX to the `/scrape` endpoint
3. `app.py` calls the Unsplash Search Photos API
4. The app downloads each returned image to `C:/Images`
5. The gallery is rendered with download links

## Prerequisites

- Python 3.7 or higher
- A valid Unsplash API Access Key
- Windows is recommended for the default output directory (`C:/Images`)

## Installation

1. Open a terminal and navigate to the project folder:
```powershell
cd "d:\image scraper"
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

## Get Unsplash API key

1. Visit https://unsplash.com/oauth/applications and sign in or sign up.
2. Click **Create a new application**.
3. Enter a name, description, and website URL for your app.
4. Accept the Unsplash API terms and submit the application.
5. Copy the **Access Key** from your new application details.

## Configure `.env`

1. Create a `.env` file in the project root.
2. Add your Unsplash Access Key:
```text
UNSPLASH_ACCESS_KEY=your_actual_api_key_here
```

> Note: This repository does not include a `.env.example` file, so create `.env` manually.

3. If you use version control, add `.env` to `.gitignore` so your API key is not committed.

## Running the app

Start the Flask server:
```powershell
python app.py
```

Open this URL in your browser:

`http://127.0.0.1:5001`

## Usage

1. Open the app in your browser
2. Enter a search keyword such as `dog`, `sunset`, or `city`
3. Click **Scrape Images**
4. Wait while the app fetches and saves the images
5. Click a thumbnail or **Download** button to download the saved image

## Local download directory

Downloaded images are saved by default to:

`C:/Images`

If you want to use another folder or a different platform, change the `save_dir` value in `app.py`.

## Project structure

```
d:\image scraper\
├── app.py                # Flask application and Unsplash integration
├── requirements.txt      # Python dependencies
├── .env                  # Local environment variables (API key)
├── README.md             # Project documentation
├── templates/
│   ├── index.html        # Search page and AJAX form
│   └── download.html     # Image gallery and download links
├── downloaded_images/    # Local folder in repo (not used by app)
└── C:/Images/            # Default runtime download folder
```

## Dependencies

- Flask
- requests
- python-dotenv
- gunicorn

## Environment variables

- `UNSPLASH_ACCESS_KEY` — your Unsplash API access key

## Troubleshooting

### `UNSPLASH_ACCESS_KEY environment variable is not set`
- Create a `.env` file in the project root
- Add `UNSPLASH_ACCESS_KEY=your_actual_api_key_here`
- Restart the Flask app

### `Failed to retrieve images from Unsplash (Status: 403)`
- Verify your Access Key is correct and active
- Check your app registration on Unsplash
- Try creating a new Unsplash app if needed

### No images found
- Try a broader search term
- Search for a more common topic
- Some specific queries may not return results

### Images do not download
- Ensure `C:/Images` exists and is writable
- Run the app with sufficient permissions or change `save_dir` in `app.py`
- Confirm your internet connection

## API notes

- The app requests up to 30 results per query
- Unsplash API rate limits apply; see Unsplash developer docs for details

## License

This project uses the Unsplash API. Refer to the [Unsplash License](https://unsplash.com/license) for permitted image usage.

## Support

- **Unsplash API**: https://unsplash.com/developers
- **This app**: Use the troubleshooting section above
