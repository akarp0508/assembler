# assembler
assembler

# Important
This assembler requires 3 configuration files
 - instructions list
 - parameters list
 - psuedoinstructions list

# Syntax of the parameters list
Every parameter needs to have specified its:
 - name (later used as referece in instructions config)
 - syntax of a parameter, with all numbers named (e.g. "REG[%regnum/decusnumber(0_32)]", the correct way to write this parameter is REG[0], REG[1], REG[2] ... REG[31])
 - syntax of coding the value in parameters (e.g. 0-5:regnum meaning that the value will be stored in first 5 bits)
 
Other detiales:
 - you can also code static numbers in a parameter (e.g. 0-5:01001 meaning that 5 first bits will be 01001)
 - tou can also add bits after or before instruction by adding -/+ sign (e.g. +0-5:00000, this means that there will be 00000 added to the end of current instruction code)
 
There are 6 types of number values you can easily read:
 - number - reads decimal, hexadecimal and binary values
 - usnumber - reads unsigned decimal, hexadecimal and binary values
 - decnumber - reads decimal values
 - usdecnumber - reads decimal unsigned values
 - hexnumber - reads hexadecimal values
 - binnumber - reads binary values

These predefined types of number values have a parameter with the range of values e.g. number(-32_32) means that the number needs to be within -32 (inclusively) and 32 (exclusively)

Syntax:
NAME<sometext%miniparametername/passToThisParameter>[startbit_endbit:miniparametername]

Syntax examples:
 REG<REG[%regnum/decusnumber(0_32)]>[0-5:regnum]
 
There is a possibility of passing parameters. For example:
 Parameters config:
 REG<>
 

# Syntax of the instructions list
Every instruction needs to have specifed its:
 - name (e.g. "ADD")
 - list of parameters (references to parameters specified in parameters config)
 - base (set of bits, which then get overwritten by coded parameters)

How one instruction definition should look like:  
ADD[00000000000000000000]<REG><REG|NUMBER>

 - ADD - name
 - 00000000000000000000 - base
 - REG - reference to parameter specified in parameters config file
 - REG|NUMBER - two references to parameters specified in config file, the first one that does not give error will be used in assembling process

Other detailes:
 - Every line with any uncommented non-space charactes is taken into consideration
 - Comments can be made with # (everything behind this symbol in the line does not affect assembler)
