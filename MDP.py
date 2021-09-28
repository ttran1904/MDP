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
        self.__calculateProbs()
    
    # Get transition probability dictionary. 
    # Each key is a state, and its value is a dictionary of 
    # transitions as keys and probabilities as values.
    def getTransitionProbs(self):
        return self.output
    
    # Change the values from COUNT to PROBABILITY 
    # based on how many total transitions a state has
    def __calculateProbs(self):
        for state in self.output:
            transitions = self.output[state]
            # Num of transition is total moves for a state
            n = sum(transitions.values())   
            
            new_trans = {}
            for t in transitions:
                new_trans[t] = transitions[t] / n
            self.output[state] = new_trans
        pass
    
    def __addTransition(self, state, next):
        pass
        
                
            
        
    
    
    