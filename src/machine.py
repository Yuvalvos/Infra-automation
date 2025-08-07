import logging
class Machine:
    def __init__(self, name, os_type, cpu, ram):
        self.name = name
        self.os_type = os_type
        self.cpu = cpu
        self.ram = ram

        logging.info(f"Machine created: {self.name}, OS: {self.os_type}, CPU: {self.cpu}, RAM: {self.ram}GB")   
    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os_type,
            "cpu": self.cpu,
            "ram": self.ram
        }