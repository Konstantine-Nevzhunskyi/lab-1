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

    def PrintAll(self):
        f2 = 0
        f = 0
        for plane in Planes.planes:
            print plane['Name'], plane['Model']
            for flight in plane['Flights']:
                print '   ', flight['Time'], '      ', flight['From'], '->', flight['To']
                f2 = 1
            if f2 == 0:
                    print '    This plane has no Flights'
            f = 1
        if f == 0:
            print('No planes')

    def NewFlight(self, name, time, froM, to):
        f = 0
        for plane in Planes.planes:
            if plane['Name'] == name:
                plane['Flights'].append({'Time': time, 'From': froM, 'To': to})
                f = 1
        if f == 0:
            print('Error, no planes with this name')

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
                    print '   ', flight['Time'], '      ', flight['From'], '->', flight['To']
                    f2 = 1
                if f2 == 0:
                    print '    This plane has no Flights'
                f = 1
        if f == 0:
            print('Error, no planes with this name')

    def DelPlane(self,name):
        f = 0
        i=0
        while Planes.planes[i]['Name']!=name:
            i+=1
        if Planes.planes[i]['Name']==name:
            f = 1
            for j in range (0,len(Planes.planes[i]['Flights'])):
                Planes.planes[i]['Flights'][j].clear()
            del(Planes.planes[i]['Flights'])
            Planes.planes[i].clear()
            del(Planes.planes[i])
        if f == 0:
            print 'Error, no planes with this name'

    def DelFlight(self, name, time):
        f = 0
        f2 = 0
        for plane in Planes.planes:
            if plane['Name'] == name:
                i = 0
                while plane['Flights'][i]['Time']!=time:
                    i+=1
                if plane['Flights'][i]['Time']==time:
                    plane['Flights'][i].clear()
                    del (plane['Flights'])[i]
                    f2 = 1
                #for flight in plane['Flights']:
                    #if flight['Time']==time:
                        #flight=[]
                        #flight.clear()
                        #del (plane['Flights'])[i]

                        #f2 = 1
                if f2 == 0:
                    print '    Error, no flights with this time'
                f = 1
        if f == 0:
            print('Error, no planes with this name')
    def Edit(self, name, newName, newModel, f_change, time, newTo, newFrom, newTime):
        f3 = 0
        for plane in Planes.planes:
            if plane['Name'] == newName:
              f3 += 1
        if f3 == 0 or f3 == 1 and newName==name:
            f = 0
            for plane in Planes.planes:
                if plane['Name'] == name:
                    f = 1
                    f2 = 0
                    plane['Name'] = newName
                    plane['Model'] = newModel
                    if f_change == 1:
                        f4=0
                        for flight in plane['Flights']:
                            if flight['Time']==newTime:
                                f4 += 1
                        if f4 == 0 or f4 == 1 and time == newTime:
                            for flight in plane['Flights']:
                                if flight['Time']==time:
                                    f2 = 1
                                    flight['Time']=newTime
                                    flight['From']=newFrom
                                    flight['To']=newTo
                            if f2 == 0:
                                print 'Error, no flight with this time'
                        else:
                            print 'Error, wrong time'

            if f == 0:
                print('Error, no planes with this name')
        else:
            print('Error, wrong new name')


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
