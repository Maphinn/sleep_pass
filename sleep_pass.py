#!/usr/bin/python
##############################################################################################
#   _____  _                         ______
#  (  __ \| |                       (_____ \
#   \ \ \_) | ____ ____ ____         _____) )___  ___  ___
#  _ \ \  | |/ _  ) _  )  _ \       |  ____/ _  |/___)/___)
# ( \_\ \ | ( (/ ( (/ /| | | |______| |   ( ( | |___ |___ |
#  \_____)|_|\____)____) ||_(_______)_|    \_||_(___/(___/
#                      |_|
#                                 Computer Crime and Forensics - 2017
#                                   VU/UvA - Tim Veenman
#
#  Is there a lingering fear that the police are going to raid your place any second now
#  while you are busy with completely legal activities?
#  This might help (to keep the forensics team out).
#  USAGE:
#    1. Change the password, command and time intervals to your liking.
#    2. Rename the script into something that could legally be running on your pc.
#    3. Place the script in a plausable location (e.g /usr/bin/)
#    4. Once you start working on your legal business keep a terminal open on the side
#       with this script running and answer the password prompt when it comes.
#    5. When you are done, move the program to the background of the shell
#       (most likely ctrl-z)
#    6. Kill it using the process id with SIGKILL.
#       sudo kill -9 [pid]
#    7. ???
#    8. Profit
#
#  Keep in mind that killing the process any other way
#  will still cause the command to trigger.
#
#  Disclaimer:
#    This script is for educational purposes only.
#    Please do not use this for illegal purposes.
#    The script is provided AS IS without warranty of any kind.
#    Anything you use this script for is your own responsibility.
#
##############################################################################################
# Imports
from subprocess import call
import threading
import getpass
import signal
import time
import os

##############################################################################################
# Make changes here:
##############################################################################################
# Time in seconds before the user is prompted for the password
PROMPT_SLEEP_TIME = 180
# Time in seconds to answer the password prompt before command is executed
PASS_SLEEP_TIME = 20
# Password for the computer
PASSWORD = "CorrectHorse"
# Command and args to be executed to lock, encrypt or wipe the pc.
COMMAND = "/usr/bin/i3lock"
ARGS = ["-c", "111111"]
##############################################################################################

# Global constant
password = ""

class timeThread(threading.Thread):
  def run(self):
    global password
    for i in range (PASS_SLEEP_TIME):
      if password == "":
        time.sleep(1)
      else:
        break
    if PASSWORD == password:
      print "Password correct"
    else:
      print "Password incorrect, executing given command."
      command()

def checkPassword():
  global password
  password = getpass.getpass()

def run():
  global password
  while True:
    password = ""
    checkThread = timeThread()
    time.sleep(PROMPT_SLEEP_TIME)
    checkThread.start()
    checkPassword()
    while (checkThread.isAlive()):
      pass
    print "Service restarting"

def command():
  call([COMMAND] + ARGS, shell=False)
  os._exit(0)


def signal_handler(signal, frame):
  if signal == 2:
    print "\nSIGINT",
  elif signal == 15:
    print "SIGTERM",
  else:
    print "Unknown signal",
  print " detected, executing given command."
  command()

print "Starting"
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
run()
print "Error: bypassed command"
