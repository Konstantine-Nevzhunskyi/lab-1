import cPickle as pickle

class Planes:
    planes=[]
    def _init_(self):
        input = open('data.pkl', 'rb')
        Planes.planes = pickle.load(input)
        input.close()

    def Print(self):
        for plane in Planes.planes:
            print plane['Name'], plane['Model']

    def NewPlane(self, name, model):
        Planes.planes.append({'Name': name, 'Flights': [], 'Model': model})

    def NewFlight(self, name, time, froM, to):
        f = 0
        for plane in Planes.planes:
            if plane['Name']== name:
                plane['Flights'].append({'Time': time, 'From': froM, 'To': to})
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