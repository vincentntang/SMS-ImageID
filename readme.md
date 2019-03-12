$ py -m pip install --user virtualenv
$ virtualenv env
$ source env/Scripts/activate
$ pip install flask twilio clarifai

Convert `.env.sample` to `.env` and add your API key from clarifai

\$ python tags.py

to run the code, should return AI

To save dependencies list on virtualenv

\$ pip freeze > requirements.txt
