
import variables
import time 
from pyfirmata import Arduino


    
board = Arduino( variables.PUERTO )

def f_blik( encender ):
        if encender == True:
                board.digital[13].write(0)
        else:
                board.digital[13].write(1)
