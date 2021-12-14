# assembler
assembler

# Important
This assembler requires 3 configuration files
 - instructions list
 - parameters list
 - psuedoinstructions list

# Syntax of the parameters list

# Syntax of the instructions list
Every instruction needs to have specifed:
 - name (e.g. "ADD")
 - list of parameters (references to parameters specified in parameters config)
 - base (set of bits, which then get overwritten by coded parameters)

How one instruction definition should look like:  
ADD[00000000000000000000]<REG,REG>

 - ADD - name
 - 00000000000000000000 - base
 - REG - reference to parameter specified in parameters config file

Other detailes:
 - Every line with any uncommented non-space charactes is taken into consideration
 - Comments can be made with # (everything behind this symbol in the line does not affect assembler)
