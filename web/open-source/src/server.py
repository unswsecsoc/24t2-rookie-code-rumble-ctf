from flask import Flask, render_template, request, abort, send_from_directory
import os

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/super_secret_admin_page_haha', methods=['GET'])
def protected_assets():
    return render_template('super_secret_admin_page_haha.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)