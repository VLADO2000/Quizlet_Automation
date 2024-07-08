import subprocess

from logger import logger

def get_devices():
    """
    Run shell command adb devices to check upon
    presented devices in the system
    :return list of available devices:
    """
    command = ["adb", "devices"]
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout.strip().splitlines()[1:]

    #adb devices has to columns with device serialno and devices added with tabulation
    devices = [device.split("\t")[0] for device in output]

    logger.info(f"Fetched devices: {devices}")

    return devices


def select_device(devices):
    """
    If more than one device is presented in the system

    :param devices:
    :return choosen device:
    """
    if len(devices) == 1:
        return devices[0]

    logger.info("More than one device in the system. Please select one")
    for index,device in enumerate(devices):
        print(f'index: {index+1}, device: {device}')

    while True:
        try:
            user_choice = int(input("Please select device: "))
            if 1 <= user_choice <= len(devices):
                logger.info(f"Selected device: {devices[user_choice-1]}")
                return devices[user_choice-1]
            else:
                logger.error("Wrong index. Please try again")
                print("Wrong index. Please try again")
        except ValueError:
            logger.error("Wrong value has been submitted")
            print("Wrong value has been submitted")


def get_device_version(device):
    """
    Device capabilities extraction
    "return dict with
    """
    command = ["adb", "-s", device, "shell",
               "getprop", "|", "grep", "release"]
    result = subprocess.run(command, capture_output=True, text=True)

    #A lot of resutls returns by release pattern as list of strings
    device_version = result.stdout.strip().splitlines()[0]
    device_version = device_version.split(":")[1].strip().strip("[]")
    logger.info(f"Fetched {device} version: {device_version}")

    return device_version

def check_package_persistance(device, package_keyword):
    """"
    Check upon package for automation test persistent
    """
    command = ["adb", "-s", device, "shell", "pm",
               "list", "packages", package_keyword]

    try:
        search = subprocess.run(command, capture_output=True,
                                   text=True, check=True)
        search_result = search.stdout.strip()
        if search_result:
            logger.info(f"Checked {package_keyword} package installed: {search_result}")
        else:
            logger.info(f"Checked {package_keyword} package not installed")
            return False
    except subprocess.CalledProcessError as e:
        logger.error(f"Error checking {package_keyword} package installation: {e}")
        return False

    return True

def install_package(device, path_to_package):
    """
    Automation test package instalation
    :param device:
    :param path_to_package:
    """
    command = ["adb", "-s", device, "install", path_to_package]

    try:
        install = subprocess.run(command, check=True, capture_output=True, text=True)
        logger.info(f"Installed package: {install.stdout.strip()}")

    except subprocess.CalledProcessError as e:
        logger.error(f"Error installing package: {e}")


def get_device_capabilities():
    """
    Device capabilities extraction
    "return dict with
    """
    devices = get_devices()
    if not devices:
        logger.error("No devices in the system")
        raise Exception("No devices in the system")

    device = select_device(devices)
    device_version = get_device_version(device)

    if not check_package_persistance(device, "quizlet"):
        install_package(device, "/Users/sharkeee/Downloads/Quizlet_8.42.1_apkcombo.com.apk")

    device_capabilites = {
        "deviceName": device,
        "platformVersion": str(float(device_version)),
    }


    return device_capabilites





