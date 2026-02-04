# EGAIN-CHATBOT
Simple customer service chatbot that tracks customer packages. 

# SETUP:
1. Installing Python3 from python.org onto your device.
2. Downloading or cloning this repo.
3. Opening up a terminal
4. Run: -> python chatbot.py

# DESIGN APPROACH:
- Designed a conversation flowchart that would occur between the bot and user.
- Incorporated input validation and error handling.
- Utilizing mock input data to simulate package status (on time, delayed, lost)
  note: each package tracking number will have 10 exactly digits, however if a package is either     delayed OR lost, they will have an additional index label as 'd' as delayed or 'l' as lost.. 
- Prioritizing clean code and comments explaining the purpose of specific functions.

# BRIEF EXAMPLE:
Hello! I am eGain Package Bot! I will track your package! 
Please enter your 10-digit tracking number or type 'q' to leave.
-> 12345
-> Unfortunately, your input is not valid.
    Please enter 10-digit tracking number.
-> 1234567890
-> Great news!! Your package is en route and will arrive as scheduled.
