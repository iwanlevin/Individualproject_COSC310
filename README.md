# Individual Assingment - An Interactive Conversational Agent

This last individual part of the project was completed by Iwan Levin.
## Description

This part adds on to group Assignment 3 by adding two new features by using internet API’s. The two API’s I chose were Google translate and Wolfram Alpha to implement two new features in Calm Bot app.

The program is made up of two classes:
>chatbot is the class that can has all the attributes of the chat bot and its methods

>main class is where a chatbot object gets created and is run to extract quotes from file as  
>well as running a loop to continuously ask the user for input with a loop in the class until  
>they enter an exit word  

## Installation

To be able to run the chat bot, you need the nltk and sklearn Python packages.
Open up command prompt and type the following:  

`pip install nltk`  

`pip install -U scikit-learn` 

Next you need to install the packages for Google Translate and Wolfram alpha.
Type the following in the command prompt:

`pip install googletrans == 3.1.0a0`

`pip install wolframalpha == 5.0.0`


You should then open up a Python interactive console (IDLE) and download all nltk packages by:

`import nltk`  

`nltk.download()`

A GUI should pop up, select 'all | All packages' and press download, afterwards close the GUI.

Afterwards, you may run the main.pyw file and the bot should work accordingly.
***NOTE: When running the main.pyw file, a delay of 10-15 seconds is normal to train the model in the sentiment file***

## New features

Wolfram Alpha API: Using the API I queried the wolfram alpha computational engine to gain a definition of a word when the sentance is started with define. When a user input is started with 'define' the chat bot queries wolfram alpha and return the definition of the word imediatily preceeding the 'define' tag.

Example: <br />
You: define anxiety <br />
Calm bot: Anxiety: <br />
1 | noun | (psychiatry) a relatively permanent state of worry and nervousness occurring in a variety of mental disorders, usually accompanied by compulsive behavior or attacks of panic <br />
2 | noun | a vague unpleasant emotion that is experienced in anticipation of some (usually ill-defined) misfortune

Google Translate API: Using a module for python that allows a user to make use of the google translate API with out having to pay for googl cloud services the user input is analized to determine the language it was written in then is translated to english so the bot can formulate a response based on user input then the bot response is translated into the language that the user input was deteermined to be. So the bot can converse in any language supported by google translate.

Example: <br />
You: Hello <br />
Calm bot: Hello <br />
You: Je suis anxieux. <br />
Calm bot: Je suis là pour vous aider à aller mieux.
