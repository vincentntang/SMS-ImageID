![](https://i.imgur.com/83R3fYd.png)

Twilio Python Clarifai is a lightweight flask app.

Send over a SMS text with an image to a designated phone number.

It will send a response based on what the Clarifai API thinks the image is

## Installation

Install Anaconda for Windows

```py
py -m pip install --user virtualenv
virtualenv env
source env/Scripts/activate
pip install -r requirements.txt
```

Add your API_KEY as an `env` variable

```
export CLARIFAI_API_KEY=.....YOUR-API-KEY.....
```
