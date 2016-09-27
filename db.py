import cPickle as pickle

class Planes:
    planes=[]
    def __init__(self):
        input = open('data.pkl', 'rb')
        Planes.planes = pickle.load(input)
        input.close()

    def Print(self):
        for plane in Planes.planes:
            print plane['Name'], plane['Model']


    def NewFlight(self, name, time, froM, to):
        f = 0
        for plane in Planes.planes:
            if plane['Name'] == name:
                plane['Flights'].append({'Time': time, 'From': froM, 'To': to})
                f = 1
        if f == 0:
            print('Error, no plane with this name')

    def NewPlane(self, name, model):
        f = 0
        for plane in Planes.planes:
            if plane['Name'] == name:
                f = 1
        if f == 0:
            Planes.planes.append({'Name': name, 'Flights': [], 'Model': model})
        else:
            print 'Error, there is the same name'

    def PrintFlight(self, name):
        f = 0
        f2 = 0
        for plane in Planes.planes:
            if plane['Name']== name:
                print plane['Name'], plane['Model']
                for flight in plane['Flights']:
                    print '   ', flight['Time'], flight['From'], flight['To']
                    f2 = 1
                if f2 == 0:
                    print '    This plane has no Flights'
                f = 1
        if f == 0:
            print('Error, no plane with this name')

    def Search(self):
        for plane in Planes.planes:
            f = 0
            for flight in plane['Flights']:
                if flight['To']=='Spain':
                    f = 1
            if f == 1:
                print(plane['Name'], plane['Model'])

    def Save(self):
        output = open('data.pkl', 'wb')
        pickle.dump(Planes.planes, output, 2)
        output.close()
