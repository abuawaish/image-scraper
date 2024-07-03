from flask import Flask, request, render_template, jsonify, send_from_directory, url_for
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Create a directory to save images
save_dir = 'C:/Images' 
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    query = request.form['query']
    url = f"https://unsplash.com/s/photos/"+query
    response = requests.get(url)
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,'html.parser')
            image_data = soup.find_all('img',attrs={'class':"ApbSI"})
            image_urls = []
            for i in image_data[20:-11]:
                image_url = i.get('src')
                image_d = requests.get(image_url).content
                with open(os.path.join(save_dir , f"{query}_{image_data.index(i)}.jpg") , "wb") as f:
                    f.write(image_d)
                image_urls.append(url_for('download_image', filename=f"{query}_{image_data.index(i)}.jpg"))
            return render_template('download.html', image_urls=image_urls)
        else:
            return 'Failed to retrieve images from Unsplash'
    except Exception as e:
        return 'Some internal error has occurred: ' + str(e)

@app.route('/download/<filename>')
def download_image(filename):
    return send_from_directory(save_dir , filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
