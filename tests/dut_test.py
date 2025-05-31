import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

@cocotb.test()
async def dut_test(dut):
    test vectors = [
        (0,0,0),
        (0,1,1),
        (1,0,1),
        (1,1,0)
    ]
    for a, b, expected in test_vectors:
        dut.a.value = a 
        dut.b.value = b

        await Timer( 1, units='ns')
    
        actual = int(dut.y.value)
        dut.log.info(f"Testing a = {a}, b={b} => y={actual}")
    
        assert actual == expected, f"FAILED": a={a}, b={b}, expected={expected},got={actual}"
