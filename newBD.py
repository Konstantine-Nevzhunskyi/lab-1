import cPickle as pickle

class DB:

    planes=[]
    flights=[]
    all = [planes, flights]

    def __init__(self):
        input = open('data.pkl', 'rb')
        DB.all = pickle.load(input)
        input.close()
        DB.planes = DB.all[0]
        DB.flights = DB.all[1]
        #input_p = open('planes.pkl', 'rb')
        #DB.planes= pickle.load(input_p)
        #input_p.close()
        #input_f = open('flights.pkl', 'rb')
        #DB.flights = pickle.load(input_f)
        #input_f.close()

    def Save(self):
        DB.all[0] = DB.planes
        DB.all[1] = DB.flights
        output = open('data.pkl', 'wb')
        pickle.dump(DB.all, output, 2)
        output.close()
        #output_p = open('planes.pkl', 'wb')
        #pickle.dump(DB.planes, output_p, 2)
        #output_p.close()
        #output_f = open('flights.pkl', 'wb')
        #pickle.dump(DB.planes, output_f, 2)
        #output_f.close()

    def NewPlane(self, name, model):
        if len(DB.planes)>0:
            id = DB.planes[len(DB.planes) - 1]['id'] + 1
        else:
            id = 1
        f = 0
        for plane in DB.planes:
            if plane['Name'] == name:
                f = 1
        if f == 0:
            DB.planes.append({'id': id, 'Name': name, 'Model': model})
        else:
            print 'Error, there is the same name'

    def Print(self):
        for plane in DB.planes:
            print plane['Name'], plane['Model']

    def PrintID(self, id):
        for plane in DB.planes:
            if plane['id'] == id:
                print plane['Name'], plane['Model']
                return

    def PrintAll(self):
        f2 = 0
        f = 0
        for plane in DB.planes:
            print plane['Name'], plane['Model']
            for flight in DB.flights:
                if flight['plane_id']==plane['id']:
                    print '   ', flight['Time'], '      ', flight['From'], '->', flight['To']
                    f2 = 1
            if f2 == 0:
                    print '    This plane has no Flights'
            f = 1
        if f == 0:
            print('No planes')

    def NewFlight(self, name, time, froM, to):
        if len(DB.flights)>0:
            id = DB.flights[len(DB.flights) - 1] + 1
        else:
            id = 1
        f = 0
        for plane in DB.planes:
            if plane['Name'] == name:
                f = 1
                f2 = 0
                for flight in DB.flights:
                    if flight['plane_id'] == plane['id'] and time == flight['Time']:
                        f2 = 1
                if f2 == 0:
                    DB.flights.append({'id': id, 'Time': time, 'From': froM, 'To': to, 'plane_id': plane['id']})
                else:
                    print 'Error, there is flight with this time'
        if f == 0:
            print('Error, no planes with this name')

    def PrintFlight(self, name):
        f = 0
        f2 = 0
        for plane in DB.planes:
            if plane['Name']== name:
                print plane['Name'], plane['Model']
                for flight in DB.flights:
                    if flight['plane_id'] == plane['id']:
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
        while DB.planes[i]['Name']!=name:
            i+=1
        if DB.planes[i]['Name']==name:
            f = 1
            for j in range (0,len(DB.flights)):
                if DB.flights[j]['plane_id'] == DB.planes[i]['id']:
                    DB.flights[j].clear()
                    del(DB.flights[j])
            DB.planes[i].clear()
            del(DB.planes[i])
        if f == 0:
            print 'Error, no planes with this name'

    def DelFlight(self, name, time):
        f = 0
        f2 = 0
        for plane in DB.planes:
            if plane['Name'] == name:
                for i in range(0,len(DB.flights)):
                    if plane['id'] == DB.flights[i]['plane_id'] and time == DB.flights[i]['Time']:
                        DB.flights[i].clear()
                        del(DB.flights[i])
                        f2 = 1
                #i = 0
                #while plane['Flights'][i]['Time']!=time:
                #    i+=1
                #if plane['Flights'][i]['Time']==time:
                #    plane['Flights'][i].clear()
                #    del (plane['Flights'])[i]
                #    f2 = 1
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
            for plane in DB.planes:
                if plane['Name'] == newName:
                    f3 += 1
            if f3 == 0 or f3 == 1 and newName == name:
                f = 0
                for plane in DB.planes:
                    if plane['Name'] == name:
                        f = 1
                        f2 = 0
                        plane['Name'] = newName
                        plane['Model'] = newModel
                        if f_change == 1:
                            f4 = 0
                            for flight in DB.flights:
                                if plane['id'] == flight['plane_id'] and flight['Time'] == newTime:
                                    f4 += 1
                            if f4 == 0 or f4 == 1 and time == newTime:
                                for flight in DB.flights:
                                    if plane['id'] == flight['plane_id'] and flight['Time'] == time:
                                        f2 = 1
                                        flight['Time'] = newTime
                                        flight['From'] = newFrom
                                        flight['To'] = newTo
                                if f2 == 0:
                                    print 'Error, no flight with this time'
                            else:
                                print 'Error, wrong time'

                if f == 0:
                    print('Error, no planes with this name')
            else:
                print('Error, wrong new name')

        def Search(self):
            p = []
            for flight in DB.flights:
                if flight['To'] == 'Spain':
                    if p.count(flight['plane_id']) == 0:
                        DB.PrintId(flight['plane_id'])
                        p.append(flight['plane_id'])