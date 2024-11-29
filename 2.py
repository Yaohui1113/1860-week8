CHIP DisplayCounter<group number> {
    IN inc, reset;
    OUT a, b, c, d, e, f, g;
    
    PARTS:
    // 16-bit counter register to store the current count
    Register(in=counterNext, load=load, out=counterValue);

    // Increment the counter value by 1
    Inc16(in=counterValue, out=incrementedValue);

    // Multiplex between incremented value or reset value (0)
    Mux16(a=incrementedValue, b=false[16], sel=reset, out=counterNext);

    // Load control: increment only when 'inc' is high
    Or(a=inc, b=reset, out=load);

    // Decode the 4 least significant bits of the counter to drive the 7-segment display
    Decoder(in=counterValue[0..3], out[0]=a, out[1]=b, out[2]=c, out[3]=d, out[4]=e, out[5]=f, out[6]=g);
}
