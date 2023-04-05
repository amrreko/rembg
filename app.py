from flask import Flask, request, send_file
import requests
import os
from rembg import remove

app = Flask(__name__)

@app.route('/', methods=['GET'])
def remove_background():
    # Get the image URL from the query parameter
    image_url = request.args.get('url')
    
    # Download the image to a local file
    r = requests.get(image_url)
    with open('input.png', 'wb') as f:
        f.write(r.content)
    
    # Remove the background from the image using Rembg
    with open('input.png', 'rb') as f:
        with open('output.png', 'wb') as out:
            out.write(remove(f.read()))
    
    # Send the resulting image back to the user
    return send_file('output.png', mimetype='image/png')

if __name__ == '__main__':
    app.run()
