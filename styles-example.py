#!/usr/bin/python3

# examples for print styles for use with ESC/POS thermal printer

# abbr. name             hex   decimal
# NUL   Null             0x00   0
# LF    Line Feed        0x0A  10
# ESC   Escape           0x1B  27
# GS    Group Separator  0x1D  29

ESC = chr(27)
GS  = chr(29)

InitializePrinter = ESC + '@';
BoldOn            = ESC + 'E' + chr(1)
BoldOff           = ESC + 'E' + chr(0)
DoubleOn          = GS  + '!' + chr(16+32);  # double-high + double-wide \u0011
DoubleOff         = GS  + '!' + chr(0)
RegularFont       = ESC + 'M' + chr(0)
SmallFont         = ESC + 'M' + chr(1)

sample = "0123 abcd ABCD !@£% (){}\n"

T = InitializePrinter
T += sample
T += BoldOn + sample + BoldOff
T += SmallFont
T += sample
T += BoldOn + sample + BoldOff

print(T)
