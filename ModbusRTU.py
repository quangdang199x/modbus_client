import pymodbus
import serial
import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
client = ModbusClient(method="rtu", port = "COM6", baudrate = 19200, stopbits = 1, bytesize = 8, parity = 'E',)
conection = client.connect()
# import logging
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

def MyProject():
    print("Voltage: %s" %voltage)
    print("Current: %s" %current)
    print("Power: %s" %power)
    print("Frequency: %s" %frequency)
    print("mpptCurrent1: %s" %mpptCurrent1)
    print("mpptVoltage1: %s" %mpptVoltage1)
    print("mpptPower1: %s" %mpptPower1)
    print("mpptCurrent2: %s" %mpptCurrent2)
    print("mpptVoltage2: %s" %mpptVoltage2)
    print("mpptPower2: %s" %mpptPower2)
    print("mpptCurrent3: %s" %mpptCurrent3)
    print("mpptVoltage3: %s" %mpptVoltage3)
    print("mpptPower3: %s" %mpptPower3)
    pass
class ScaleFactor:
    GAIN0 = 1
    GAIN1 = 10
    GAIN2 = 100
    GAIN3 = 1000
    FIX0 = 1
    FIX1 = 0.1
    FIX2 = 0.01
    FIX3 = 0.001
    pass

# while True:
#     result = client.read_holding_registers(0,15, unit =1)
#     voltage = result.registers[0]*ScaleFactor.FIX2
#     current = result.registers[1]*ScaleFactor.FIX3
#     power = result.registers[2]*ScaleFactor.FIX0
#     frequency = result.registers[3]*ScaleFactor.FIX2
#     mpptCurrent1 = result.registers[4]*ScaleFactor.FIX3
#     mpptVoltage1 = result.registers[5]*ScaleFactor.FIX2
#     mpptPower1 = result.registers[6]*ScaleFactor.FIX0
#     mpptCurrent2 = result.registers[7]*ScaleFactor.FIX3
#     mpptVoltage2 = result.registers[8]*ScaleFactor.FIX2
#     mpptPower2 = result.registers[9]*ScaleFactor.FIX0
#     mpptCurrent3 = result.registers[10]*ScaleFactor.FIX3
#     mpptVoltage3 = result.registers[11]*ScaleFactor.FIX2
#     mpptPower3 = result.registers[12]*ScaleFactor.FIX0
#     MyProject()
#     print("\n")
#    time.sleep(10)
result = client.read_holding_registers(40001, 15, unit = 1)
x = result.registers[0]
y = result.registers[1]
print(x)
print(y)

voltage = ((result.registers[0] << 16) | result.registers[1])*ScaleFactor.FIX3
print("Voltage: %sV" %(voltage))
