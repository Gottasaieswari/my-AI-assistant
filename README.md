# my-AI-assistant 
This repository contains the code for "AI assistant" a voice-controlled AI assistant built using Python.
This AI assistant script uses voice commands to perform various tasks such as checking the time and date, searching Wikipedia, taking screenshots, sending emails, playing YouTube videos, sending WhatsApp messages, searching the web, remembering information, playing or controlling songs, and shutting down or restarting the PC. If a command is not recognized, it sends the query to an AI model for a response.
Project Overview
The AI Assistant can:

Announce the current time and date.
Search and summarize Wikipedia articles.
Take screenshots.
Send emails.
Play YouTube videos.
Send WhatsApp messages.
Perform web searches.
Remember and recall information.
Control media playback (play, pause, stop songs).
Shutdown or restart the PC.
Answer queries using an AI model.
Main file is thonai.py.
Functions
Main Loop
The main loop listens for voice commands and performs the corresponding actions. If a command is not recognized, it sends the query to the AI model for a response.

speak(audio)
Converts text to speech using the pyttsx3 library. It takes a string audio as input and speaks it out loud.

time()
Announces the current time. Uses the datetime library to get the current time and the speak function to vocalize it.

date()
Announces the current date. Uses the datetime library to get the current date and the speak function to vocalize it.

youtube(ele)
Plays a YouTube video. Uses the pywhatkit library to search for and play the specified video.

chrome(ele)
Searches the web using Chrome. Uses the pywhatkit library to perform the search.

whatsapp(t, msg)
Sends a WhatsApp message. Uses the pywhatkit library to send a message instantly to the specified number t with the message msg.

sendmail(to, msg)
Sends an email using SMTP. Logs in to a Gmail account and sends an email to the recipient to with the message msg.

wish()
Greets the user based on the current time of day. Uses the datetime library to determine the appropriate greeting and the speak function to vocalize it.

inp()
Listens for voice input from the user. Uses the speech_recognition library to capture and recognize speech, returning the recognized text.

screenshot()
Takes a screenshot of the current screen. Uses the pyscreeze library to capture and save the screenshot.

talktoai(query)
Sends a query to an AI model for a response. Uses the requests library to send a request to an AI service and speaks the response using the speak function.

Configuration
Authorization Header
The headers variable contains an authorization token required to access the AI service.

AI Service URL
The url variable specifies the endpoint for the AI service used in talktoai.

Wikipedia Search
The wikipedia library is used to search for and summarize Wikipedia articles.

Sample Module
The sample module is used for playing and controlling songs. It is expected to have functions like 
Key Components and Libraries
Text-to-Speech (pyttsx3): Converts text to speech, allowing the assistant to vocalize responses and prompts.
Speech Recognition (speech_recognition): Captures and recognizes speech input from the user.
Wikipedia (wikipedia): Fetches summaries from Wikipedia based on user queries.
PyWhatKit (pywhatkit): Automates web searches, plays YouTube videos, and sends WhatsApp messages.
Smtplib (smtplib): Sends emails via SMTP.
Pyscreeze (pyscreeze): Captures screenshots.
OpenAI (openai): Interacts with OpenAI's API to handle complex queries.
Requests (requests): Sends HTTP requests to web services.
Datetime (datetime): Handles date and time operations.
OS (os): Performs system operations like shutdown and restart.
Authorization Header: The headers variable contains an authorization token required to access the AI service. AI Service URL: The url variable specifies the endpoint for the AI service used in talktoai. Wikipedia Search: The wikipedia library is used to search for and summarize Wikipedia articles. Sample Module: The sample module contains functions to play and control songs, which are invoked in the main loop.

Requirements: Python 3.x Libraries: pyttsx3, datetime, speech_recognition, wikipedia, pyautogui, pyscreeze, json, requests, openai, pywhatkit, smtplib, sample, os

 How to Use  Clone the repository. Install the required libraries using pip install <library_name>. Run the script using python script_name.py. Interact with the AI assistant using voice commands. This README provides a high-level overview of the functions in the AI assistant. For more detailed usage and customization, refer to the code comments and documentation within the script.
 This AI Assistant project is a versatile tool that leverages several Python libraries to automate tasks via voice commands. It integrates functionalities like web searches, email sending, media control, and more, making it a powerful and user-friendly assistant.









