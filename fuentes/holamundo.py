
import variables
import time 
from pyfirmata import Arduino


board = Arduino( PUERTO )

while 2:
        board.digital[13].write(1)
        time.sleep(2)
        board.digital[13].write(0)
        time.sleep(1)