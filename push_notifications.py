from pushsafer import Client
import os
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from the .env file
client = Client(os.environ["AUTH"])


def send_message(message):


    title = "New item added to the shopping list"


    device  = 73228
    icon = 1
    # icon_color = "#FF0000"
    sound = 4
    vibration = 3
    url = "http://192.168.20.2:5000"
    url_title = "Shopping List"
    time2live = 0
    priority = 2
    retry = 60
    expire = 600
    answer = 1
    image_1 = ""
    image_2 = ""
    image_3 =""

    resp = client.send_message(
        message,
        title,
        device,
        icon,
        sound,
        vibration,
        url,
        url_title,
        time2live,
        priority,
        retry,
        expire,
        answer,
        image_1,

    )

    return resp


# resp = client.send_message("Message" "Hello", "73228", "1", "4", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "60", "600", "1", "", "", "")
