
import variables
import time 
from pyfirmata import Arduino


    
board = Arduino( variables.PUERTO )

def f_blik( encender ):
        valor = board.digital[13].read()
        if valor == True:
                board.digital[13].write(0)
        else:
                board.digital[13].write(1)
