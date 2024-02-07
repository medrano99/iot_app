class Sensor:
    __id_device : str
    __temperature: int
    __timestamp: int

    def __init__(self,id_device:str):
        self.__id_device = id_device
        self.__temperature = 0
        self.__timestamp = 0
    
    @property
    def id_device(self):
        return self.__id_device
    
    @id_device.setter
    def id_device(self,idDevice):
        self.id_device = idDevice

    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self,temp):
        self.__temperature=temp
    
    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self,timestmp):
        self.__timestamp = timestmp
    
    def payload(self):
        return {
            "id_device":self.__id_device,
            "temperature":self.__temperature,
            "timestamp":self.__timestamp
            }
