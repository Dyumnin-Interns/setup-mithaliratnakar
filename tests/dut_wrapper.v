`timescale 1ns/1ps
module dut_wrapper;

    reg a;
    reg b;
    wire y;

    dut uut (
        .a(a),
        .b(b),
        .y(y)
    );
endmodule
