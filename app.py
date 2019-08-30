import os 
import pandas as pd 
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('fileform.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    print(request.files)
    if 'excel' in request.files:
        file = request.files['excel']
        df = pd.read_excel(file)
        print(df.head())
        # if photo.filename != '':            
            # photo.save(os.path.join('C:/Users/Public/Pictures', photo.filename))
    return redirect(url_for('fileFrontPage'))
 

if __name__ == '__main__':
    app.debug = True 
    _host = os.environ.get('IP', '127.0.0.1') 
    _port = int(os.environ.get('PORT', 5000))
    # app.config['MONGO_DBNAME'] = 'restdb'
    # app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
    app.run(host=_host, port=_port)