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
Small side script for computer crime and forensics project.
Which causes the pc to go to execute a command (and for example lock) when you are not at the pc.
Even when forensics try to prevent try to prevent the command.
