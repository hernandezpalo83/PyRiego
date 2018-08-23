
import variables
import time 
from pyfirmata import Arduino


board = Arduino( variables.PUERTO )

while 2:
        board.digital[13].write(1)