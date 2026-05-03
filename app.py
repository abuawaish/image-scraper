from flask import Flask, request, render_template, jsonify, send_from_directory, url_for
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Create a directory to save images
save_dir = 'C:/Images' 
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Unsplash API Configuration
UNSPLASH_API_KEY = os.getenv('UNSPLASH_ACCESS_KEY')
if not UNSPLASH_API_KEY:
    raise ValueError('UNSPLASH_ACCESS_KEY environment variable is not set. Please add it to your .env file.')

# Strip any quotes if present (defensive programming)
UNSPLASH_API_KEY = UNSPLASH_API_KEY.strip('\'"')

UNSPLASH_API_BASE = 'https://api.unsplash.com/search/photos'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    query = request.form.get('query', '').strip()
    
    if not query:
        return 'Please enter a search query.'
    
    try:
        # Call Unsplash API
        params = {
            'query': query,
            'client_id': UNSPLASH_API_KEY,
            'per_page': 30,
            'order_by': 'relevant'
        }
        
        response = requests.get(UNSPLASH_API_BASE, params=params, timeout=10)
        
        if response.status_code != 200:
            error_detail = ''
            try:
                error_data = response.json()
                if 'errors' in error_data:
                    error_detail = f" Error: {error_data['errors'][0]}"
            except:
                pass
            return f'Failed to retrieve images from Unsplash (Status: {response.status_code}).{error_detail} Please verify your API key is correct and active.'
        
        data = response.json()
        
        if 'results' not in data or len(data['results']) == 0:
            return 'No images found for this query. Please try a different search term.'
        
        image_urls = []
        
        # Download and save images from API results
        for idx, photo in enumerate(data['results']):
            try:
                # Get the regular size image URL
                image_url = photo['urls']['regular']
                
                if not image_url or not isinstance(image_url, str):
                    continue
                
                # Download the image
                image_d = requests.get(image_url, timeout=10).content
                filename = f"{query.replace(' ', '_')}_{len(image_urls) + 1}.jpg"
                filepath = os.path.join(save_dir, filename)
                with open(filepath, 'wb') as f:
                    f.write(image_d)
                image_urls.append(url_for('download_image', filename=filename))
            except Exception as e:
                # Skip this image and continue
                continue
        
        if not image_urls:
            return 'Failed to download images. Please try again.'
        
        return render_template('download.html', image_urls=image_urls, query = query)
        
    except requests.RequestException as e:
        return f'Network error: Unable to reach Unsplash. Details: {str(e)}'
    except ValueError as e:
        return f'Configuration error: {str(e)}'
    except Exception as e:
        return f'An error occurred: {str(e)}'

@app.route('/download/<filename>')
def download_image(filename):
    return send_from_directory(save_dir , filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
