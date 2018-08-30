from pyfirmata import Arduino, util, STRING_DATA
import variables

board = Arduino( PUERTO )
board.send_sysex( STRING_DATA, util.str_to_two_byte_iter('Hello!') )

def msg( text ):
    if text:
        board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( text ) )