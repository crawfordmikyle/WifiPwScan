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
# print(profiles)
# Some Regex magic to return an array of all the wifi profile names from profiles
profile_names = (re.findall("All User Profile     : (.*)\r", profiles))
# print(profile_names)
# Create empty array to store data
wifi_list = []

# Check to make sure you have gotten profiles and start working
if len(profile_names) != 0:
    for n in profile_names:
        # Each wifi connection will need its own dictionary
        # We will appened this to the wifi_list variable
        wifi_profile = {}
        # Now we run more specific commands to get the information we need
        # about the wifi connection and see if there is a security key
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", n], capture_output= True).stdout.decode()
        # print(profile_info)
        # look for cases where there is no password so we can skip them
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            # Assign the SSID to the dictionary
            wifi_profile["ssid"] = n
            # print(wifi_profile)
            # Run key=clear to get the passwords
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profiles", n, "key=clear"], capture_output= True).stdout.decode()
            # print(profile_info_pass)
            # More Regex magic
            password = re.search("Key Content            :(.*)\r",profile_info_pass)
            # print(password)
            # check if we found a password
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)
    for x in range(len(wifi_list)):
        print(wifi_list[x])