# requires 2 config files:
# - instructions configs list
# - parameters configs list

parameterDescriptionsDict = dict()

class bitsOverwriteDetailes():
    #if firstbit==-1 there will be endBit bits added on the left of instruction;
    def __init__(self, firstBit:int) -> None:
        
        pass

class parameterDescripion():
    def __init__(self, prefix:str, typeofparam:str, postfix:str, bitsOverwrites:list()) -> None:
        self.prefix = prefix
        self.typeofparam = typeofparam
        self.postfix = postfix
        self.bitsOverwrites = bitsOverwrites
        

def start(instConfigPath:str,parametersConfigPath:str) -> list:
    return None

if(__name__=="__main__"):
    start("exampleInstConfig.txt","exampleParametersConfig.txt")


