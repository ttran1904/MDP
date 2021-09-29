from MDP import MDP
import unittest 

class MDPTestCase(unittest.TestCase):
    def test_small1(self):
        lst = [['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd']]
        self.__printInput(lst)
        mdp = MDP(lst)
        mdp.run()
        # Get the result Transition Probabilities (dictionary)
        tp = mdp.getTransitionProbs()
        
        self.__printOutput(tp)
        solution = {'a': {'b': 1}, 'b': {'c':1}, 'c' : {'d': 1}}
        self.assertEqual(tp, solution)

    def test_small2(self):
        seq1 = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd']
        seq2 = ['a', 'b', 'b', 'a', 'a', 'd', 'd', 'b', 'b', 'c', 'a']
        lst = [seq1, seq2]
        self.__printInput(lst)
        mdp = MDP(lst)
        mdp.run()
        # Get the result Transition Probabilities (dictionary)
        tp = mdp.getTransitionProbs()
        
        self.__printOutput(tp)
        solution = {'a': {'b': 2/3, 'd': 1/3}, 'b': {'c': 2/3, 'a': 1/3}, 
                    'c': {'d': 1/2, 'a': 1/2}, 'd': {'b': 1}}
        self.assertEqual(tp, solution)
    
    def __printInput(self, lst):
        # Uncomment HERE to see input
        # print("\n......Input: ", lst)
        pass
    
    def __printOutput(self, o):
        # Uncomment HERE to see output
        # print(".....Output:", o)
        pass
    
if __name__ == '__main__':
    unittest.main() 