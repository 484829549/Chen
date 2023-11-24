import time
import serial


class Therapy:
    def __init__(self, port, baudrate, time) -> None:
        self.serial = serial.Serial(port, baudrate, timeout=time)

        self.commands = [b'\x55\xAA\xC9\x00', b'\x55\xAA\xC9\x01', b'\x55\xAA\xC9\x02', b'\x55\xAA\xC9\x03',
                         b'\x55\xAA\xC9\x04', b'\x55\xAA\xC9\x05', b'\x55\xAA\xC9\x06', b'\x55\xAA\xC9\x07',
                         b'\x55\xAA\xC9\x08', b'\x55\xAA\xC9\x09', b'\x55\xAA\xC9\x0A']

    def sendCommand(self, toSend):
        if self.serial.isOpen():
            print("Sending command ", toSend)
            self.serial.write(self.commands[toSend])  # 编码
            time.sleep(0.1)
    
    def receiveData(self):
        print("Waiting for responds...")
        while True:
            data = self.serial.read_all()
            if data == '':
                continue
            else:
                break
        print("Receive: ", data)
        hex_str = data.hex()
        return hex_str
