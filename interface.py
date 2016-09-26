#import db

def menu(planes):

    planes.NewPlane('BD-112','Boinge T1000')
    print('1 - to see Planes info')
    print('2 - to add Plane')
    print('3 - to see Flight')
    c = input('Choose: ')
    print '______________________'
    if c == 1:
        planes.Print()
    elif c == 2:
       name = input('Name: ')
       model = input('Model: ')
       planes.NewPlane(name,model)

    c = input('Back to main Menu? (Y):')
    if c=='Y' or c=='y':
        menu(planes)
