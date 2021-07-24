# Import the stuff we need
# pip install influxdb
from dateutil.parser import DEFAULTPARSER
from pymodbus import payload
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time
from twisted.internet.defer import Deferred
import json
from influxdb import InfluxDBClient, client
from datetime import datetime

#Setup database:
client_1 = ModbusClient(host="127.0.0.1", port=502)
conection = client_1.connect()
print(conection)
client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')
# client.create_database('mydb')
client.get_list_database()
client.switch_database('mynewdb')

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
def myField():
    result = client_1.read_holding_registers(40001, 50, unit = 1)
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

    #Setup Payload:
    json_payload = []
    current_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    data = {
        "measurement"  : "Inverter_1",
        "tags" : {},
        "time" : current_time,
        "fields" : {
            "currentPhaseA" : currentPhaseA, 
            "currentPhaseB" : currentPhaseB, 
            "currentPhaseC" : currentPhaseC, 
            "powerPhaseA" : powerPhaseA, 
            "powerPhaseB" : powerPhaseB, 
            "powerPhaseC" : powerPhaseC, 
            "voltagePhaseA" : voltagePhaseA, 
            "voltagePhaseB" : voltagePhaseB, 
            "voltagePhaseC" : voltagePhaseC, 
            "frequency" : frequency, 
            "totalYield" : totalYield, 
            "dailyYield" : dailyYield, 
            "operatingTime" : operatingTime, 
            "mpptCurrent1" : mpptCurrent1, 
            "mpptVoltage1" : mpptVoltage1, 
            "mpptPower1" : mpptPower1 
        }
    }
    json_payload.append(data)

#Send our payload:
    client.write_points(json_payload)
# while True:
# myField()
    payload = client.query('select * from Inverter_1;')
    time.sleep(5)
    # print(data)
    # print(json_payload)
    print(payload)
while True:
    myField()
    time.sleep(10)