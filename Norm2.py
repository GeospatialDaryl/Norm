#!/usr/bin/env python3
import mmap
import sys

print("This is the name of the script: ", sys.argv[0]        )
print("Number of arguments: ", len(sys.argv)                 )
print("The arguments are: " , str(sys.argv)                  )

#https://stackoverflow.com/questions/7052883/how-to-find-substring-in-file

episode = sys.argv[1]
print('\n \n \n')

with open(episode, 'rb', 0) as file, \
    mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        for i in 
    tester = s.find(b'Norm')
    print(tester)
    if tester != -1:
            print('true')
            position = tester
            
            print(s[position: position+500].decode('ascii') )
		

print('\n \n')