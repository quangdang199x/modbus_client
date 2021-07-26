from pyModbusTCP.client import ModbusClient
import time
client = ModbusClient(host="127.0.0.1", port=502, unit_id=1, auto_open=True)
def myModbusTCP():
        print("Voltage: %sV" %voltage[0])
        print("Current: %sA" %current[0])
        print("Power: %sA" %power[0])
        print("Frenquency: %sHz" %frequency[0])
        print("mpptCurrent1: %sA" %mpptCurrent1[0])
        print("mpptVoltage1: %sV" %mpptVoltage1[0])
        print("mpptPower1: %sW" %mpptPower1[0])
        print("mpptCurrent2: %sA" %mpptCurrent2[0])
        print("mpptVoltage2: %sV" %mpptVoltage2[0])
        print("mpptPower2: %sW" %mpptPower2[0])
        print("mpptCurrent3: %sA" %mpptCurrent3[0])
        print("mpptVoltage3: %sV" %mpptVoltage3[0])
        print("mpptPower3: %sW" %mpptPower3[0])
while 1:
#     regs_1 = client.read_holding_registers(0, 20)
#     regs_2 = client.read_input_registers(0, 10)
    # voltage = regs_2[0]
    # current = regs_1[1]
    # power = regs_2[2]
    # voltage = regs_1[0]
    # current = regs_1[1]
    # power = regs_1[2]
    # frequency = regs_1[3]
    # mpptCurrent1 = regs_1[4]
    # mpptVoltage1 = regs_1[5]
    # mpptPower1 = regs_1[6]
    # mpptCurrent2 = regs_1[7]
    # mpptVoltage2 = regs_1[8]
    # mpptPower2 = regs_1[9]
    # mpptCurrent3 = regs_1[10]
    # mpptVoltage3 = regs_1[11]
    # mpptPower3 = regs_1[12]
    voltage = client.read_holding_registers(0,1)
    current = client.read_holding_registers(1,1)
    power = client.read_holding_registers(2,1)
    frequency = client.read_holding_registers(3,1)
    mpptCurrent1 = client.read_holding_registers(4,1)
    mpptVoltage1 = client.read_holding_registers(5,1)
    mpptPower1 = client.read_holding_registers(6,1)
    mpptCurrent2 = client.read_holding_registers(7,1)
    mpptVoltage2 = client.read_holding_registers(8,1)
    mpptPower2 = client.read_holding_registers(9,1)
    mpptCurrent3 = client.read_holding_registers(10,1)
    mpptVoltage3 = client.read_holding_registers(11,1)
    mpptPower3 = client.read_holding_registers(12,1)
    myModbusTCP()
    # if regs_1:
    #     print("""Voltage: %sV; Current: %sA; Power: %sW; Frequency: %sHz;
    #         mpptCurrent1: %s; mpptVoltage1: %s; mpptPower1: %s;
    #         mpptCurrent2: %s;  mpptVoltage2: %s; mpptPower2: %s;
    #         mpptCurrent3: %s;  mpptVoltage3: %s; mpptPower3: %s;""" %(voltage, current, power, frequency, mpptCurrent1, mpptVoltage1, mpptPower1, mpptCurrent2, mpptVoltage2, mpptPower2, mpptCurrent3, mpptVoltage3, mpptPower3))
    # else:
    #     print("read error")
    time.sleep(10)