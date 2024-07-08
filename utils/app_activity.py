"""
I have beem wondering about implementing kind of script for automation of fetching
app name and app activity for devices

I guess it has to be after determing device and app package instalation process
than we can pull the triger using XPATH
take launch app with appium and call csript of app determinanation
worth to try

One thing left, it has to be automated, which means using Appium is needed
Adn this makes it a little bit more complicated as my aim was to provide web driver for tests
and there i also need a driver for app info fetching
"""

from logger import logger
import subprocess

APP_ICON = "//android.widget.TextView[@content-desc=\"Quizlet\"]"


def get_focused_app(device):
    """
    Leveraging adb command to get focused app
    :param device:
    :return:
    """
    command = ["adb", "-s", device, "shell", "dumpsys", "window", "|",
               "grep", "-E", "mCurrentFocus|mFocusedApp"]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        output = result.stdout.strip().split("/")
        logger.info(f"Fetched focused app: {output}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error fetching focused app: {e}")
        return None

    return output

def get_app_activity(device):
    pass

