class Tower(object):
    def __init__(self, sim, name):
        self.sim = sim
        self.name = name
        
        self.floors = []
        self.addFloor('Main Floor')
        self.main_floor = self.floors[0]
        
        self.elevators = []
        
    def addFloor(self, name = 'Floor'):
        floor = Floor(name)
        self.floors.append(floor)
        print "Added floor: {}!".format(floor.name)
        
    def tick(self):
        for floor in self.floors:
            #floor.tick()
            pass
            
class Floor(object):
    def __init__(self,name):
        self.name = name
        

class Idea(object):
    def __init__(self, label):
        self.label = label
        self.vars = {'0':100}
    
class Simulation(object):
    def __init__(self, name='Default Corp. Tower'):
        self.tower = Tower(self,name)
        self.iteration = 0
        self.log('Simulation Started')
        
    def iterate(self, num_iterations=1):
        for _ in range(num_iterations):
            self.iteration+=1
            self.tower.tick()
            
    def log(self, message):
        print "{:<5} {}".format(self.iteration,message)

    
def main():
    sim = Simulation()
    
    while True:
        sim.iterate()
    
if __name__ == '__main__':
    main()
    