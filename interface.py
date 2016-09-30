#import db

def menu(planes,i):
    print '__________________________'
    print('1 - to see Planes')
    print('2 - to add Plane')
    print('3 - to del Plane')
    print('4 - to see Flights')
    print('5 - to add Flight')
    print('6 - to del Flight')
    print('7 - to search with Spain destination planes')
    print('8 - to save changes')
    print('9 - to edit')
    c = input('Choose:')
    if c == 1:
        print('_________PLANES___________')
        planes.Print()
    elif c == 2:
        print('________NEW PLANE_________')
        name = raw_input('Name:')
        model = raw_input('Model:')
        planes.NewPlane(name,model)
    elif c == 3:
        print('_________DEL PLANE________')
        name = raw_input('Plane name:')
        planes.DelPlane(name)
    elif c==4:
        print('__________FLIGHTS__________')
        name = raw_input('Plane name:')
        planes.PrintFlight(name)
    elif c==5:
        print('________NEW FLIGHT________')
        name = raw_input('Plane name:')
        froM = raw_input('Flys from:')
        to = raw_input('Flys to:')
        time = raw_input('time:')
        planes.NewFlight(name, time, froM, to)
    elif c == 6:
        print('________DEL FLIGHT________')
        name = raw_input('Plane name:')
        time = raw_input('Flight time:')
        planes.DelFlight(name, time)
    elif c == 7:
        print('_________TO SPAIN_________')
        planes.Search()
    elif c == 8:
        planes.Save()
        print('__________SAVED___________')
    elif c == 9:
        print('___________EDIT___________')

        name = raw_input('Name of the Plane u want to edit:')
        print '__________________________'
        planes.PrintFlight(name)
        print '__________________________'
        newName = raw_input('New plane name:')
        newModel = raw_input('New plane model:')
        f_change = input('to edit some flight?(0/1):')
        if f_change == 1:
            time = raw_input('Time of the Flight u want to edit:')
            newTime = raw_input('New time:')
            newTo = raw_input('New destination:')
            newFrom = raw_input('New Location:')
        time = 0
        newTime = 0
        newTo = 0
        newFrom = 0
        planes.Edit(name, newName, newModel, f_change, time, newTo, newFrom, newTime)
    elif c==0:
        planes.PrintAll()

    c = raw_input('Back to main Menu? (N):')
    if c!='N' and c!='n':
        menu(planes, i + 1)

    if i == 0:
        c = raw_input('Save changes? (N):')
        if c != 'N' or c != 'n':
            planes.Save()
