import os
from bitstring import BitArray

os.chdir('C:/Users//Desktop/py binary')
b=BitArray(bytes=open('Capture.JPG','rb').read())

# Store result
with open('filename_bits.txt', 'w') as file1: 
    file1.write(b.bin)