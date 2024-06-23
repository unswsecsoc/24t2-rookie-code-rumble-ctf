from flask import Flask, render_template, request, abort, send_from_directory
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    href = "../static/css/styles.css"  
    if request.method == 'POST':
        path = request.form.get('path')  
        if os.path.exists(path):
            try:
                files = os.listdir(path)
            except NotADirectoryError as e:
                return render_template('index.html', output="Stop poking around", href=href)
            output = "<br>".join(files)
            return render_template('index.html', output=output, href=href)
        else:
            return render_template('index.html', output=f'{path}', href=href)
    else:
        return render_template('index.html', href=href)

@app.route('/assets/<path:filename>')
def protected_assets(filename):
    referrer = request.referrer
    # Change this section when we have actual ports
    if referrer and "my-first-page" in referrer:
        return send_from_directory('assets', filename)
    else:
        abort(451)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
