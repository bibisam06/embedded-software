from flask import Flask, Response
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/get-date')
def get_date():
    current = datetime.now().strftime("%H:%M:%S")
    xml_response = f"""<?xml version='1.0'?>
<date>{current}</date>"""
    return Response(xml_response, mimetype='text/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

