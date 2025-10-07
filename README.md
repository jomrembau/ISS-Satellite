# ISS Overhead Notifier

This project is my solution to Dr. Angela Yu's challenge from the **100 Days of Python** course. The starting code was provided, and I modified it to create a working ISS overhead notifier.

## Description
This Python script checks whether the International Space Station (ISS) is currently overhead within ±5° of a specified location and whether it is dark at that location (before sunrise or after sunset). 
If both conditions are true, the script sends an email notification to the user.

## How It Works
1. Retrieves the current ISS position using the [Open Notify API](http://api.open-notify.org/iss-now.json).  
2. Fetches sunrise and sunset times for the user's location using the [Sunrise-Sunset API](https://sunrise-sunset.org/api).  
3. Checks if the ISS is overhead and it is currently dark.  
4. Sends an email notification if conditions are met.

## Setup
1. Replace `email` and `password` with your email credentials (use an app password for Gmail).  
2. Replace `recipient_address` with the email where notifications should be sent.  
3. Install required packages if not already installed:
   ```bash
   pip install requests

Usage

* Run the script, and it will check the ISS position and send an email if conditions are met. For continuous checking, wrap it in a loop with a delay (e.g., using time.sleep(60)).

Notes

* The starting code was provided by Dr. Angela Yu as part of the 100 Days of Python course.

* This is my personal implementation and improvement on the challenge.
