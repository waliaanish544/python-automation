import time
import webbrowser
from obsws_python import ReqClient

# -------------------
# CONFIGURATION
# -------------------

# Microsoft Teams meeting link
MEETING_LINK = "https://teams.live.com/meet/9322158007356?p=pSBspphCHOCRwK3dPy"

# Attendance portal link
ATTENDANCE_LINK = "https://mml.accenture.com/trainee-portal"

# OBS WebSocket settings
OBS_HOST = "localhost"
OBS_PORT = 4455
OBS_PASSWORD = "mypassword123"

# Meeting duration in seconds (e.g., 9 hours = 32400 seconds)
MEETING_DURATION = 32400  # change to your actual meeting length

# -------------------
# 1️⃣ Open Teams Meeting
# -------------------
print("Opening Microsoft Teams meeting...")
webbrowser.open("https://teams.live.com/meet/9322158007356?p=pSBspphCHOCRwK3dPy")
time.sleep(20)  # wait for Teams to load (adjust if needed)

# -------------------
# 2️⃣ Open Attendance Portal
# -------------------
print("Opening Attendance Portal...")
webbrowser.open("https://mml.accenture.com/trainee-portal")
time.sleep(5)  # give it a few seconds to open

# -------------------
# 3️⃣ Connect to OBS and start recording
# -------------------
try:
    obs = ReqClient(host="localhost", port=4455, password="mypassword123")
    print("Connected to OBS ✅")
    
    # Start recording
    obs.start_record()
    print("Recording started 🎥")

    # -------------------
    # 4️⃣ Wait for the meeting to finish
    # -------------------
    print(f"Recording for {32400} seconds...")
    time.sleep(32400)

    # Stop recording
    obs.stop_record()
    print("Recording stopped ⏹️")

except Exception as e:
    print(f"Error connecting to OBS: {e}")
