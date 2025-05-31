`timescale 1ns/1ps
module dut_wrapper(
    input  wire a,
    input  wire b,
    output wire y
);

    dut uut (
        .a(a),
        .b(b),
        .y(y)
    );

endmodule
