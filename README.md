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
![#f03c15] ADD `#f03c15`[![#c5f015] 00000000000000000000`#c5f015`]<![#1589F0]REG,REG`#1589F0`>

![#f03c15] ADD - Name `#f03c15`
![#c5f015]00000000000000000000 - base`#c5f015`
![#1589F0]REG - reference to parameter specified in parameters config file`#1589F0` 

Other detailes:
 - Every line with any uncommented non-space charactes is taken into consideration
 - Comments can be made with # (everything behind this symbol in the line does not affect assembler)
