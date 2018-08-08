#!/usr/bin/env python3
import mmap
import sys

print("This is the name of the script: ", sys.argv[0]        )
print("Number of arguments: ", len(sys.argv)                 )
print("The arguments are: " , str(sys.argv)                  )

#https://stackoverflow.com/questions/7052883/how-to-find-substring-in-file
#  https://teamtreehouse.com/community/fatal-remote-origin-already-exists
#  https://stackoverflow.com/questions/89228/calling-an-external-command-in-python
#  https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files
#  https://stackoverflow.com/questions/7052883/how-to-find-substring-in-file
#  https://docs.python.org/3/library/mmap.html
#  https://docs.python.org/2/library/mmap.html
#  http://effbot.org/pyfaq/how-do-i-check-if-an-object-is-an-instance-of-a-given-class-or-of-a-subclass-of-it.htm
#  https://stackoverflow.com/questions/28011104/undo-git-add-all
#  https://teamtreehouse.com/community/fatal-remote-origin-already-exists
#

episode = sys.argv[1]
print('\n \n \n')

def mmapFinder(s, inSubStr, inOutList):
    if isinstance(s, mmap.mmap):
	    print("is an instance!")
    # generate the range tuple
    res = s.find(inSubStr)
    print('res:',res)
    if res == -1:
        return inOutList
    else:
        inOutList.append(res)
        t = s[res:]
        mmapFinder(t,inSubStr,inOutList)


with open(episode, 'rb', 0) as file:
    s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
    listTst = []
    mmapFinder(s, b'1', listTst)
    tester = s.find(b'Norm')
    print(tester)
    if tester != -1:
            print('true')
            position = tester
            
            print(s[position: position+500].decode('ascii') )
		

print('\n \n')