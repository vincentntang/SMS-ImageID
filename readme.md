Have Anaconda installed

$ py -m pip install --user virtualenv
$ virtualenv env
$ source env/Scripts/activate
$ pip install flask twilio clarifai

Convert `.env.sample` to `.env` and add your API key from clarifai

\$ python tags.py

to run the code, should return AI tags generated from image src

To save dependencies list on virtualenv

\$ pip freeze > requirements.txt

to deploy to web

\$ pip install gunicon

## Src notes

https://www.youtube.com/watch?v=18KQIPhiVdc → twilio clarifai
https://www.youtube.com/watch?v=skc-ZEU9kO8 → deploy to heroku instead of ngrok
