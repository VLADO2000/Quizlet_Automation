from device_capabilities import get_device_capabilities
from utils.app_activity import get_app_activity

def get_android_capabilities():
  """
  Returns Android capabilities
  """
  device_capabilities = get_device_capabilities()

  #Should be used only after carefull consideration
  app_activity = get_app_activity(device_capabilities["deviceName"], device_capabilities)

  return {
      "platformName": "Android",
      "platformVersion": device_capabilities["platformVersion"],
      "deviceName": device_capabilities["deviceName"],
      "automationName": "UiAutomator2",
      "appPackage": "com.quizlet.quizletandroid",
      "appActivity": ".ui.RootActivity"
    }



