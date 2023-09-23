#This programs receive data from arduino and save it into a csv file

import serial
import csv

nombre_csv = 'hoja_de_calculo3.csv'

archivo = open(nombre_csv,'w')
archivo_obj = csv.writer(archivo)

arduino = serial.Serial(port='COM3',baudrate=9600)
#arduino.reset_input_buffer()
ready = arduino.read_until(expected=b'!') #this returns message in bytes including the expected parameter
print(ready)
decoded_ready = ready[0:len(ready)-1].decode('utf-8') #convert bytes to string and eliminates the expected parameter
print(decoded_ready)

arduino.write('x'.encode('utf-8')) #telling arduino python is ready

while True:
    rows = arduino.read_until(b'!') #we will read one row at a time without \n or \r in the message
    print(rows)
    decoded_rows = rows[0:len(rows)-1].decode('utf-8') #eliminating expected parameter from message
    if (decoded_rows == 'stop'): # stop is telling us arduino is no longer going to send data
        break
    print(decoded_rows)
    decoded_rows_list = decoded_rows.split(',') #decode funcion returns a str we need to convert to list, using ',' as separator for split funcion
    archivo_obj.writerow(decoded_rows_list) #writerow expects a list variable
                                            #also each time we call writerow it is going to write what we sent
                                            #in the next row
print('finished')
arduino.close() #close port
