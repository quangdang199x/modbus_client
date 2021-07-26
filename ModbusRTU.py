from typing import Union
import pymodbus
import serial
import time
import enum
from pymodbus.constants import Endian
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
client = ModbusClient(method="rtu", port = "COM6", baudrate = 19200, stopbits = 1, bytesize = 8, parity = 'E',)
conection = client.connect()
# import logging
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

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

def myProject():
    result = client.read_holding_registers(40001, 50, unit = 1)
    currentPhaseA = (result.registers[0] << 16 | result.registers[1])*ScaleFactor.FIX3
    currentPhaseB = (result.registers[2] << 16 | result.registers[3])*ScaleFactor.FIX3
    currentPhaseC = (result.registers[4] << 16 | result.registers[5])*ScaleFactor.FIX3
    powerPhaseA = (result.registers[6] << 16 | result.registers[7])*ScaleFactor.FIX0
    powerPhaseB = (result.registers[8] << 16 | result.registers[9])*ScaleFactor.FIX0
    powerPhaseC = (result.registers[10] << 16 | result.registers[11])*ScaleFactor.FIX0
    voltagePhaseA = (result.registers[12] << 16 | result.registers[13])*ScaleFactor.FIX2
    voltagePhaseB = (result.registers[14] << 16 | result.registers[15])*ScaleFactor.FIX2
    voltagePhaseC = (result.registers[16] << 16 | result.registers[17])*ScaleFactor.FIX2
    frequency = result.registers[18]*ScaleFactor.FIX2
    totalYield = ((result.registers[19] << 16 | result.registers[20]) << 32 | (result.registers[21] << 16 | result.registers[22]))*ScaleFactor.FIX0
    dailyYield = ((result.registers[23] << 16 | result.registers[24]) << 32 | (result.registers[25] << 16 | result.registers[26]))*ScaleFactor.FIX0
    operatingTime = ((result.registers[27] << 16 | result.registers[28]) << 32 | (result.registers[29] << 16 | result.registers[30]))*ScaleFactor.FIX0
    mpptCurrent1 = (result.registers[31] << 16 | result.registers[32])*ScaleFactor.FIX3
    mpptVoltage1 = (result.registers[33] << 16 | result.registers[34])*ScaleFactor.FIX2
    mpptPower1 = (result.registers[35] << 16 | result.registers[36])*ScaleFactor.FIX0

    print("currentPhaseA: %sA" %currentPhaseA)
    print("currentPhaseB: %sA" %currentPhaseB)
    print("currentPhaseC: %sA" %currentPhaseC)
    print("powerPhaseA: %sW" %powerPhaseA)
    print("powerPhaseB: %sW" %powerPhaseB)
    print("powerPhaseC: %sW" %powerPhaseC)
    print("voltagePhaseA: %sV" %voltagePhaseA)
    print("voltagePhaseB: %sV" %voltagePhaseB)
    print("voltagePhaseC: %sV" %voltagePhaseC)
    print("frequency: %sHz" %frequency)
    print("totalYield: %sWh" %totalYield)
    print("dailyYield: %sWh" %dailyYield)
    print("operatingTime: %ss" %operatingTime)
    print("mpptCurrent1: %sA" %mpptCurrent1)
    print("mpptVoltage1: %sV" %mpptVoltage1)
    print("mpptPower1: %sW" %mpptPower1)

while True:
    myProject()
    print("\n")
    time.sleep(10)




# class dataType(): 
#         U16 = result.registers[0]
#         U32 = result.registers[0] << 16 | result.registers[1]
#         U64 = (result.registers[0] << 16 | result.registers[1]) << 32 | (result.registers[2] << 16 | result.registers[3])
#         pass

# def MyProject():
#     print("Voltage: %s" %voltage)
#     print("Current: %s" %current)
#     print("Power: %s" %power)
#     print("Frequency: %s" %frequency)
#     print("mpptCurrent1: %s" %mpptCurrent1)
#     print("mpptVoltage1: %s" %mpptVoltage1)
#     print("mpptPower1: %s" %mpptPower1)
#     print("mpptCurrent2: %s" %mpptCurrent2)
#     print("mpptVoltage2: %s" %mpptVoltage2)
#     print("mpptPower2: %s" %mpptPower2)
#     print("mpptCurrent3: %s" %mpptCurrent3)
#     print("mpptVoltage3: %s" %mpptVoltage3)
#     print("mpptPower3: %s" %mpptPower3)
#     pass

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