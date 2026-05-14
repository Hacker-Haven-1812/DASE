`timescale 1ns/1ps

module memory (
    input  wire        clk,
    input  wire        mem_valid,
    input  wire        mem_instr,
    output reg         mem_ready,
    input  wire [31:0] mem_addr,
    input  wire [31:0] mem_wdata,
    input  wire [3:0]  mem_wstrb,
    output reg  [31:0] mem_rdata
);

    reg [31:0] mem [0:1023];

    initial begin
        $readmemh("program.hex", mem);
    end

    always @(posedge clk) begin
        mem_ready <= 0;

        if (mem_valid) begin
            mem_ready <= 1;

            if (mem_wstrb != 0) begin
                if (mem_wstrb[0]) mem[mem_addr[11:2]][7:0]   <= mem_wdata[7:0];
                if (mem_wstrb[1]) mem[mem_addr[11:2]][15:8]  <= mem_wdata[15:8];
                if (mem_wstrb[2]) mem[mem_addr[11:2]][23:16] <= mem_wdata[23:16];
                if (mem_wstrb[3]) mem[mem_addr[11:2]][31:24] <= mem_wdata[31:24];
            end

            mem_rdata <= mem[mem_addr[11:2]];
        end
    end

endmodule

