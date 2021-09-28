import MDP
import unittest 

class MDPTestCase(unittest.TestCase):
    def smallMDP(self):
        seq1 = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd']
        lst = [seq1]
        self.MDP = MDP(lst) 
        self.MDP.run()
        tp = self.MDP.getTransitionProbs()
        print(tp)
    

if __name__ == '__main__':
    unittest.main()