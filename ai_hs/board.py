class board:
    comp1=[]
    comp2=[]
    
    def __init__(self):
           self.comp1=["","","","","","",""]
           self.comp2=["","","","","","",""]
    
    def update_unit(self, compNum, index, unit):
        if compNum==1:
            self.comp1[index]=unit
        elif compNum==2:
            self.comp2[index]=unit
            
            
        
        
    