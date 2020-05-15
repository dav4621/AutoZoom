# AutoZoom
AutoZoom is a small program written in Python, designed to automate the basic features of Zoom by Zoom Video Communications. The basis of the project was for a user to enter the required information for a meeting, such as the ID and password, beginning and end times. Then, the software would automatically launch the application, join the meeting at a specified time, and leave the meeting/close the application at a specified time as well.

# Supported Platforms
Currently macOS and Windows only. There's some code for Linux systems in there, however certain dependencies for the program to work are currently bugged, preventing function.

# Dependencies Required
  - Any version of Python3 w/ Pip
  - pyautogui -> https://pyautogui.readthedocs.io/en/latest/install.html#
  - darkdetect -> https://pypi.org/project/darkdetect/

This will be an ongoing project, for there are more features I'd like to add, such as:
  - More reliable method for GUI traversal
  - Support for password protected meetings
  - Linux support
  - Store multiple sets of session data for reoccurring use
