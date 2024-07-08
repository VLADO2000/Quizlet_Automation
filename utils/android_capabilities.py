from device_capabilities import get_device_capabilities


def get_android_capabilities():
  """
  Returns Android capabilities
  """
  device_capabilities = get_device_capabilities()
  return {
      "platformName": "Android",
      "platformVersion": device_capabilities["platformVersion"],
      "deviceName": device_capabilities["deviceName"],
      "automationName": "UiAutomator2",
      "appPackage": "com.quizlet.quizletandroid",
      "appActivity": ".ui.RootActivity"
    }
get_android_capabilities()