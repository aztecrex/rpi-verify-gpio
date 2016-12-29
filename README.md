# Check if Pi GPIO works at all

This just checks that I can do GPIO input and output on the Raspberry Pi 3.

## Test Circuit

Output: LED in series with 220Ω resistor

Input: momentary switch with pull-up and debounce.  Debounce is not necessary
for this program but I am using this configuration in another project.
To adjust the debounce, I used `gpio wfi` in a loop in Bash and kept adding
5pF capacitors until I liked the result. I think it's about 75ms as it is right
now. I still get a spurious trigger occassionally so maybe another 5pF, bringing
the delay to about 100ms would make it better.

[Circuit and breadboard](https://aztecrex.github.io/rpi-verify-gpio/) .

## Run It

0. `python verify-gpio.py`
0. expect the LED to turn on
0. press the button
0. expect LED to flash
0. expect the LED to turn off as the GPIO is reset

