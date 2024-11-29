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
        comparison = lambda a, b: a.load<b.load
        self.crew_mates=heap.Heap(comparison,Lm)
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
        classwheretreasure.load+=treasure.size
        classwheretreasure.treas.append(treasure)
        self.crew_mates.insert(classwheretreasure)
        # Write your code here
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
            trprocess = heap.Heap(lambda a, b: a[0]+a[1] < b[0]+b[1], [[crew.treas[0].arrival_time, crew.treas[0].size,0]] if crew.treas else [])
            if trprocess.data!=[]:
                time=crew.treas[0].arrival_time
            else:
                time=1
                pass
            for i in range(n-1):
                # print(trprocess.data,time)
                if trprocess.data!=[] and i<=n-2:
                    #print(trprocess.data)
                    minn=trprocess.extract()
                    #print(crew.treas[i].arrival_time,time)
                    time=crew.treas[i+1].arrival_time
                    time0=crew.treas[i].arrival_time
                    timedel=time-crew.treas[i].arrival_time
                    #print(minn,time,time0)
                    while timedel>0 and trprocess.data!=[]:
                        #print(trprocess.data, crew.treas[i+1].arrival_time,time0)
                        dif= minn[1]-crew.treas[i+1].arrival_time+time0
                        if dif<=0:
                            if timedel>=minn[1] and minn[1]>=0:
                                #print(minn)
                                time0+=minn[1]
                                #print(time0)
                                crew.treas[minn[2]].completion_time=time0
                                #print(crew.treas[minn[2]].completion_time)
                                minn1=minn
                                minn=trprocess.extract()
                                #if minn[0]==52:
                                    #print('102',minn,time,time0)
                                timedel=time-time0
                            else:
                                #if minn[0]==52:
                                    #print('102')
                                minn[1]-=timedel
                                if minn[1]>=0:
                                    trprocess.insert(minn)
                                time0+=timedel
                                timedel=0
                       #print('##########',crew.treas[i].completion_time)
                        else:
                            break
                    if timedel>0 and trprocess.data==[]:
                        crew.treas[minn[2]].completion_time=time0
                        minn[1]=0
                    else:
                        minn[1]-=crew.treas[i+1].arrival_time-time0
                        #print(minn,time0)
                        if minn[1]>=0:
                            trprocess.insert(minn)
                        else:
                            trprocess.insert(minn)

                trprocess.insert([crew.treas[i+1].arrival_time,crew.treas[i+1].size,i+1])
                time=crew.treas[i+1].arrival_time
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
                
            toberet+=crew.treas
                
        toberet.sort(key=lambda t: t.id)
        return toberet
        # Write your code here
        pass
    
    # You can add more methods if required
