import os
import requests
from flask import Flask, render_template,request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

# apis
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('message', type=str, location='json')
class HelloWorld(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        msg = json_data['message']
        API_URL = "https://api-inference.huggingface.co/models/aniketface/DialoGPT-product"
        headers = {"Authorization": f"Bearer {'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'}"}

        form_data = request.form
        input = msg 

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        
        output = query({
            "inputs": input
        })
        # take input output here
        if output.get('generated_text', 0):
            return {'data': output['generated_text']}
        else:
            return {'data': "Sorry, Server Error"}

api.add_resource(HelloWorld, '/api')

@app.route('/chat-bot')
def chat():
    return render_template('speak_to_an_expert.html')

@app.route("/api-call", methods=["GET", "POST"])
def apiCall():
    API_URL = "https://api-inference.huggingface.co/models/aniketface/DialoGPT-product"
    headers = {"Authorization": f"Bearer {'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'}"}

    form_data = request.form
    input = form_data["msg"]

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    output = query({
	    "inputs": input
    })

    return render_template("ouput.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)