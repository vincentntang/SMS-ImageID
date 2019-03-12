from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from tags import get_relevant_tags

app = Flask(__name__)

# should show an html file with "OK!" on the page
@app.route('/')
def index():
    return 'I AM WORKING YAY!'

# Route to await a POST hook from twilio
@app.route('/sms', methods=['POST'])
def sms_reply():
    resp = MessagingResponse()

    if request.form('NumMedia') != '0' :
        image_url = request.form['MediaUrl0']
        relevant_tags = get_relevant_tags(image_url) # get tags
        resp.message('\n'.join(relevant_tags)) # combine tags
    else:
        resp.message('Please send an image')
    return str(resp)

if __name__ == '__main__':
    app.run()