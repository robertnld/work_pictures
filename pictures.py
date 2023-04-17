"""
pictures.py
"""

import time
import requests

# URL of the ESP32-CAM's still image capture endpoint
URL = 'http://192.168.1.135/capture'

# Interval at which to capture still images (in seconds)
CAPTURE_INTERVAL = 900  # 15 minutes

while True:
    # Send a GET request to the ESP32-CAM's capture endpoint to get a still image, and respect TIME OUT
    try:
        response = requests.get(URL, timeout=5)
    except requests.exceptions.Timeout:
        print('Timeout')
    else:
        # Save the still image to disk
        with open(f'still_{time.time()}.jpg', 'wb') as f:
            f.write(response.content)

    # Wait for the specified interval before capturing the next still image
    time.sleep(CAPTURE_INTERVAL)
