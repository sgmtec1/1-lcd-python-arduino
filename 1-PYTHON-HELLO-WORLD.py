from pyfirmata import Arduino
import lcd
import time

board=Arduino ('COM6')

lcd.escrever(board, 0, 0, 'SGMTEC1 EM 100')
lcd.escrever(board, 0, 1, 'DIAS DE PYTHON')
time.sleep(100.0)
lcd.limpar(board)
board.exit()