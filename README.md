# Pakwheels LMS Attendance Punching Request Automation

This Python script automates the process of punching in attendance on PakWheels LMS. The script logs in to the LMS, navigates to the requests section, and submits the attendance punch-in request for a specified date. 

The employee of Pakwheels only needs to enter their username, password, and the date they want to punch in. The script automatically increments the date for subsequent runs.

## Features
- Automates the login process to LMS.
- Navigates to the "Punching Request" section.
- Automatically selects the date for punching in, incrementing from the previously recorded date.
- Allows the user to select a punch-in time and submit the request.
- Updates the date for the next punch-in request.

## Prerequisites
Before running the script, make sure the following are installed:

- **Python 3**
- **Selenium**: Install using pip:
   ```
  pip install selenium
  ```
## Getting Started
Clone or Download the Repository:
```
git clone https://github.com/ahsannachos/lms-punching-automation.git
```
## Configure Login Credentials:
  - Modify the login section of the script by replacing the username and password values:
```
username.send_keys("your_username")
password.send_keys("your_password")
```
## Date Management
You will see a text file `backenddate.txt`. It must be in the same folder where the main code is. Open it and add the date for which you want to punchin in `yyyy-mm-dd`. The script reads the last punched-in date from the file and increments it by one day for the next run.

## Running the Script
When you run the code, you'll see a pop-up of Chrome with a notification _"Chrome is being controlled by automated software"_, that's the Selenium behind on which the code is based on. Now, the LMS of Pakwheels will be open, it will login to your id though the login and password provided, head over to the punchin requests and submit your punchin attendance for 9 am.

