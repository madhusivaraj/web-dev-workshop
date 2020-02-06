# Web Dev Workshop

This is for a Web Development workshop teaching Flask and API Integration.

Slide Deck: https://docs.google.com/presentation/d/1J9sz080KM77vZ5pgpBIOOGRNTfrkNbSfANVdiFClcRw/edit?usp=sharing


## Step-by-step Documentation

No knowledge is assumed - the documentation is designed for developers with limited or no experience with Python.

## Setup

After going into the directory, these are the steps to get the app up and running locally:

#### Step 1. Create a Virtual Environment and Install Dependencies

Create a new Virtual Environment for the project and source it. If you don't have Virtual Environment yet, you can find installation  [instructions here](https://virtualenv.readthedocs.org/en/latest/).

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Next we need to install the project dependencies, which are listed in requirements.txt.

```
(venv) $ pip install -r requirements.txt
```


#### Step 2. Create a Twilio Account

Set up Twilio account and retrieve a Trial Number. 

Once set up, replace the account-sid, auth-token, trial number and your number in [app.py]([https://github.com/madhusivaraj/web-dev-workshop/blob/master/app.py](https://github.com/madhusivaraj/web-dev-workshop/blob/master/app.py)).


#### Step 3. Run the Server

Now we're ready to start our server which is as simple as:

```
(venv) $ export FLASK_APP = app.py
(venv) $ flask run
```

## Credit

Built by Madhu Sivaraj and Aditya Shastri at Rutgers University
