'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        Lm=[]
        for i in range(m):
            Lm.append(crewmate.CrewMate())
        def comparison_function(a,b):
            if a.treas==[] or b.treas==[]:
                return a.load<b.load
            else:
                return a.load<b.load

        self.crew_mates=heap.Heap(comparison_function,Lm)
        # Write your code here
        self.tottreas=[]
        pass
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        classwheretreasure=self.crew_mates.extract()
        if classwheretreasure.load>treasure.arrival_time:
            classwheretreasure.load+=treasure.size
        else:
            #if classwheretreasure.load==0:
                #classwheretreasure.load=treasure.arrival_time
            classwheretreasure.load=treasure.arrival_time+treasure.size
        classwheretreasure.treas.append(treasure)
        self.crew_mates.insert(classwheretreasure)
        #classwheretreasure.sumarrival=treasure.arrival_time
        # Write your code here
        '''if classwheretreasure.load==0:
            classwheretreasure.treas.append(treasure)
            if treasure.arrival_time>classwheretreasure.load+classwheretreasure.starttime:
                classwheretreasure.load=treasure.size
                classwheretreasure.starttime=treasure.arrival_time
            else:
                classwheretreasure.treas.append(treasure)
                classwheretreasure.load+=treasure.size'''
        pass
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        toberet=[]
        for crew in self.crew_mates.data:
            n=len(crew.treas)
            #print(crew.treas)
            trprocess = heap.Heap(lambda a, b: [a[1]+a[0],a[2]]< [b[1]+b[0],b[2]],[])
            for i in range(n):
                # print(trprocess.data,time)
                trprocess.insert([crew.treas[i].arrival_time,crew.treas[i].size,i])
                time=crew.treas[i].arrival_time
                if i==n-1:
                    timenext=0
                else:
                    timenext=crew.treas[i+1].arrival_time
                while time<timenext:
                    if trprocess.data==[]:
                        time=timenext
                        break
                    else:
                        minn=trprocess.extract()
                        #print(minn)
                        if minn[1]<=(timenext-time):
                            time+=minn[1]
                            crew.treas[minn[2]].completion_time=time
                        else:
                            minn[1]-=timenext-time
                            trprocess.insert(minn)
                            #print(minn)
                            time=timenext
                            
                
            while trprocess.data!=[]:
                #print(trprocess.data,time, 'in while')
                minele=trprocess.extract()
                #print(time+minele[1])
                #print(minele)
                if minele[0]<=time:
                    crew.treas[minele[2]].completion_time=time+minele[1]
                    time+=minele[1]
                else:
                    crew.treas[minele[2]].completion_time=minele[0]+minele[1]
                    time=minele[0]+minele[1]
                
            toberet+=crew.treas
                
        toberet.sort(key=lambda t: t.id)
        return toberet
        # Write your code here
        pass
    
    # You can add more methods if required
