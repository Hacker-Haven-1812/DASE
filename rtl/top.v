module top;

    reg clk = 0;
    reg resetn = 0;

    always #5 clk = ~clk;

    initial begin
        #20 resetn = 1;
    end

    wire mem_valid;
    wire mem_instr;
    wire mem_ready;
    wire [31:0] mem_addr;
    wire [31:0] mem_wdata;
    wire [3:0]  mem_wstrb;
    wire [31:0] mem_rdata;

    wire trap;

    // ------------------------------------
    // BRANCH DETECTION SIGNAL
    // ------------------------------------
    reg branch_taken;

    // ------------------------------------
    // Instantiate PicoRV32
    // ------------------------------------
    picorv32 core (
        .clk         (clk),
        .resetn      (resetn),

        .mem_valid   (mem_valid),
        .mem_instr   (mem_instr),
        .mem_ready   (mem_ready),
        .mem_addr    (mem_addr),
        .mem_wdata   (mem_wdata),
        .mem_wstrb   (mem_wstrb),
        .mem_rdata   (mem_rdata),

        .trap        (trap)
    );

    // ------------------------------------
    // Memory
    // ------------------------------------
    memory mem (
        .clk        (clk),
        .mem_valid  (mem_valid),
        .mem_instr  (mem_instr),
        .mem_ready  (mem_ready),
        .mem_addr   (mem_addr),
        .mem_wdata  (mem_wdata),
        .mem_wstrb  (mem_wstrb),
        .mem_rdata  (mem_rdata)
    );

    // ------------------------------------
    // Simple Branch Detection Logic
    // ------------------------------------
    always @(posedge clk) begin
        branch_taken <= 0;

        if (mem_valid && mem_instr) begin
            // Detect opcode 0x63 (BRANCH)
            if (mem_rdata[6:0] == 7'b1100011)
                branch_taken <= 1;
        end
    end

endmodule

