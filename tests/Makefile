SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v $(PWD)/../hdl/dut_wrapper.v
TOPLEVEL = dut_wrapper
MODULE = dut_test

include $(shell cocotb-config --makefiles)/Makefile.sim
