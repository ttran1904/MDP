# Find a state's transition probabilities.
# Input: a list of list of sequences
# Output: a dictionary with: states as keys, 
#          and values as another dictionary with transition as key 
#          and transition probabilities as values (sum to 1 for a state)
class MDP:
    def __init__(self, sequences=None):
        self.sequences = sequences
        self.output = None
        
    # Input the transition sequence if haven't done so
    def putSequences(self, sequences):
        self.sequences = sequences
    
    # Run through MDP to find transition probabilities
    def run(self):
        if len(self.sequences)==0:
            pass
        
        for seq in self.sequences:
            if len(seq) < 2: continue
            for i in range(1, len(seq)):
                prev, curr = seq[i-1], seq[i]
                if prev != curr:
                    self.__addTransition(prev, curr)
    
    # Get transition probability dictionary. 
    # Each key is a state, and its value is a dictionary of 
    # transitions as keys and probabilities as values.
    def getTransitionProbs(self):
        self.__calculateProbs()
        pass
    
    def __calculateProbs(self):
        for state in self.output:
            dict = self.output[]
        pass
    
    def __addTransition(self, state, next):
        pass
        
                
            
        
    
    
    