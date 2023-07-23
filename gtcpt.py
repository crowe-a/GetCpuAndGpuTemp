""" in this code we are getting gpu temrature  """
# import GPUtil,time

# def get_gpu_temperature():
#     gpus = GPUtil.getGPUs()
#     gpu_temperature = gpus[0].temperature
#     return gpu_temperature
# while True:
#     time.sleep(1)
#     print("GPU Temperature:", get_gpu_temperature(), "°C")


""" in this code we are getting cpu temrature withopen hardware monitor"""
import wmi,time
while True:
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()

    for sensor in temperature_infos:
        
        if sensor.SensorType==u'Temperature':
            if sensor.name==u"CPU Package":
                print(sensor.value)
                time.sleep(0.5)
        #     print(sensor.Name)
        #     print(sensor.Value) 