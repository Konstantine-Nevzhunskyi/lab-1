#import db

def menu(planes,i):
    print('1 - to see Planes info')
    print('2 - to add Plane')
    print('3 - to see Flight')
    print('4 - to add Flight')
    print('5 - to save changes')
    c = input('Choose:')
    print '______________________'
    if c == 1:
        planes.Print()
    elif c == 2:
       name = raw_input('Name:')
       model = raw_input('Model:')
       planes.NewPlane(name,model)
    elif c==3:
        name = raw_input('Plane name:')
        planes.PrintFlight(name)
    elif c==4:
        name = raw_input('Plane name:')
        planes.NewFlight(name)
    elif c == 5:
        planes.Save()

    c = raw_input('Back to main Menu? (Y):')
    if c=='Y' or c=='y':
        menu(planes, i + 1)

    if i == 0:
        c = raw_input('Save changes? (N):')
        if c != 'N' or c != 'n':
            planes.Save()
