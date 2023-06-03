from flask import Flask,request
import openai
app = Flask(__name__)
# Disable SSL certificate verification
openai.api_key = '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'
openai.api_base = 'https://api.openai.com'

@app.route('/getRanking', methods=['GET','POST'])
def accomThingsToDo():
        accomName = request.args;
        accomPrompt = 'things to do in '+accomName.get('accomName')
        response = openai.Completion.create(
                engine='text-davinci-003',  # Specify the ChatGPT engine
                prompt=accomPrompt,
                max_tokens=100,              # Define the maximum response length
                temperature=0.7,             # Adjust the response randomness (0.0 to 1.0)
                n=1                          # Specify the number of responses to generate
            )
        return response.choices[0].text.strip()

if __name__=='__main__':
    app.run(debug=True)