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
'''html
<span style="color: red"> ADD </span>[<span style="color: green"> 00000000000000000000</span>]<<span style="color: blue">REG,REG</span>>

<span style="color: red"> ADD - Name </span>  
<span style="color: green">00000000000000000000 - base</span>  
<span style="color: blue">REG - reference to parameter specified in parameters config file</span>  
'''

Other detailes:
 - Every line with any uncommented non-space charactes is taken into consideration
 - Comments can be made with # (everything behind this symbol in the line does not affect assembler)
