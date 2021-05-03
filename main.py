# This is a Wifi Password Scanner
# Mainly python practice
# Here I am making sure get works ignore this

# Start For Real
# Import subprocess so we can access system commands
import subprocess

# Import Regex
import re

# Create a variable and store the list of wifi profiles
profiles = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

