## Refreshing

You need to run this everytime you refresh app

$ source env/Scripts/activate
\$ export CLARIFAI_API_KEY=.....YOUR-API-KEY.....

## Quickstart

Have anaconda installed

$ py -m pip install --user virtualenv
$ virtualenv env
$ source env/Scripts/activate
$ pip install -r requirements.txt
\$ export CLARIFAI_API_KEY=.....YOUR-API-KEY.....

## Installing from scratch

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

To install dependencies list

\$ pip install -r requirements.txt

to deploy to web

\$ pip install gunicon

Create a new app on Heroku

Download the windows 64bit exe file package and install heroku CLI

open git bash

\$ heroku login

should take you to heroku to login

\$ heroku git:remote -a twilio-clarifai

"Twilio-clarifai" is the name of your app on heroku

\$ get push heroku-master

## Src notes

https://www.youtube.com/watch?v=18KQIPhiVdc → twilio clarifai
https://www.youtube.com/watch?v=pmRT8QQLIqk → deploy to heroku instead b/c we twilio can't use localhost as an endpoint
