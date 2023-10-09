"""Inverter"""
def inverter():
    """Inverter"""
    bit = str(input())
    bit_out = ""
    for out in bit:
        if out == "1":
            bit_out += "0"
        else:
            bit_out += "1"
    print(bit_out.lstrip("0"))
inverter()
