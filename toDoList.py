#Diego Aspinwall
#10-16-17
#toDoList.py

dolist = []

print('Valid commands: add, delete, print, quit')
while True:
    qsearch = input('>')
    if 'quit' in qsearch:
        break
    elif qsearch == 'print':
        for w in dolist:
            print(w)
    if qsearch[:3] == 'add':
        dolist.append(qsearch[4:])
    if qsearch[:6] == 'delete':
        if qsearch[7:] in dolist:
            dolist.remove(qsearch[7:])
        else:
            print('Not on List')
    else:
        print('Invalid Command')
