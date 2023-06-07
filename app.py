from flask import Flask, request, render_template
import openai
import requests, os, uuid, json
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# API key for your OpenAI account
openai.api_key = os.environ['KEY']
openai.api_base =  os.environ['BASE'] # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = os.environ['TYPE']
openai.api_version = os.environ['VERSION'] # this may change in the future
deployment_name = os.environ['DEPLOYMENT_NAME']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        start_phrase = request.form['start_phrase']

        # Use the OpenAI API to generate a response
        response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=1000)
        text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()

        return render_template('results.html', start_phrase=start_phrase, text=text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
