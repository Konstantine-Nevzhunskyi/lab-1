class Planes:
    planes=[]

    def NewPlane(self, name, capacity):
        Planes.planes.append({'Name': name, 'Flights': [], 'Capacity': capacity})

    def NewFlight(self, i, n, froM, to):
        Planes.planes[i].append({'№': n, 'From': froM, 'To': to})
