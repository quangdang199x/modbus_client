import enum
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

# client = ModbusClient(host= "127.0.0.1", port = 502)
# conection = client.connect()
# print(conection)
DataType = {
    "UINT16": 0xffff,
    "UINT32": 0xffffffff,
    "UINT64": 0xffffffffffffffff,
    "INT16": 0x8000,
    "SCALE": 0x8000,
    "ACC32": 0x00000000,
    "FLOAT32": 0x7fc00000,
    "SEFLOAT": 0xffffffff,
    "STRING": ""
}

class registerDataType(enum.Enum):
    UINT16 = 1
    UINT32 = 2
    UINT64 = 3
    INT16 = 4
    SCALE = 4
    ACC32 = 5
    FLOAT32 = 6
    SEFLOAT = 7
    STRING = 9


class MyDevice():
    def __init__(
        self, host, port, unit, timeout, retries=3
    ):
        self.HOST = host
        self.PORT = port
        self.UNIT = unit
        self.TIMEOUT = timeout
        self.client = ModbusClient(
            host=self.HOST,
            port=self.PORT,
            timeout=self.TIMEOUT
        )

    def _read_holding_registers(self, address, length):
        result = self.client.read_holding_registers(address, length, unit = self.UNIT)
        return BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)

    def _decode_value(self, data, length, dtype, vtype):
        try:
            if dtype == registerDataType.UINT16:
                decoded = data.decode_16bit_uint()
            elif (dtype == registerDataType.UINT32 or
                  dtype == registerDataType.ACC32):
                decoded = data.decode_32bit_uint()
            elif dtype == registerDataType.UINT64:
                decoded = data.decode_64bit_uint()
            elif dtype == registerDataType.INT16:
                decoded = data.decode_16bit_int()
            elif (dtype == registerDataType.FLOAT32 or
                  dtype == registerDataType.SEFLOAT):
                decoded = data.decode_32bit_float()
            elif dtype == registerDataType.STRING:
                decoded = data.decode_string(length * 2).decode(encoding="utf-8", errors="ignore").replace("\x00", "").rstrip()
            else:
                raise NotImplementedError(dtype)

            if decoded == DataType[dtype.name]:
                return vtype(False)
            else:
                return vtype(decoded)
        except NotImplementedError:
            raise

    def _read(self, value):
        address, length, rtype, dtype, vtype = value
        return self._decode_value(self._read_holding_registers(address, length), length, dtype, vtype)

    def connect(self):
        return self.client.connect()

Inverter = MyDevice(host = "127.0.0.1", port = 502, unit=1, timeout=1, retries=3)
print(Inverter.connect())

voltage = Inverter._read_holding_registers(address=40001, length=2)
voltage_1 = Inverter._decode_value(Inverter._read_holding_registers(address=40001, length=2), length = 2, dtype = 2, vtype=2)











# result = client.read_holding_registers(40001, 2, unit = 1)
# result_1 = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
# result_decode = result_1.decode_32bit_uint()
# print(result_decode)




# class Car(object):
#     mode = 'Moto'
#     def __init__(self, name, type, color):
#         self.name_name = name
#         self.type_type = type
#         self.color_color = color

#     def MyColor(self):
#         self.favourite_color = "RED"
#         return "My favourite color is: " + self.favourite_color



# Honda = Car("Hoda-AB", "1000cc", "red")
# Yamaha = Car("Yamaha-Z1000", "750cc", "blue")
# Suzuki = Car("Suzuki-125ASD", "125cc", "black")

# # print(Honda.MyColor())



# # print("Honda is:", Honda.name)

# # print("Honda is {}".format(Honda.__class__.mode))
# # print("Yamaha is {}".format(Yamaha.__class__.mode))
# # print("Suzuki is {}".format(Suzuki.__class__.mode))

# print("Honda: name is {}, type is {}, color is {}.".format(Honda.name_name, Honda.type_type, Honda.color_color))
# print("Yamaha: name is {}, type is {}, color is {}.".format(Yamaha.name_name, Yamaha.type_type, Yamaha.color_color))
# print("Suzuki: name is {}, type is {}, color is {}.".format(Suzuki.name_name, Suzuki.type_type, Suzuki.color_color))
