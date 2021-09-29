from MDP import MDP
import unittest 

class MDPTestCase(unittest.TestCase):
    def test_small1(self):
        lst = [['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd']]
        mdp = MDP(lst)
        mdp.run()
        # Get the result Transition Probabilities (dictionary)
        tp = mdp.getTransitionProbs()
        
        solution = {'a': {'b': 1}, 'b': {'c':1}, 'c' : {'d': 1}}
        self.assertEqual(tp, solution)

    def test_small2(self):
        seq1 = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd']
        seq2 = ['a', 'b', 'b', 'a', 'a', 'd', 'd', 'b', 'b', 'c', 'a']
        mdp = MDP([seq1, seq2])
        mdp.run()
        # Get the result Transition Probabilities (dictionary)
        tp = mdp.getTransitionProbs()
        
        solution = {'a': {'b': 2/3, 'd': 1/3}, 'b': {'c': 2/3, 'a': 1/3}, 
                    'c': {'d': 1/2, 'a': 1/2}, 'd': {'b': 1}}
        self.assertEqual(tp, solution)
        
    
if __name__ == '__main__':
    unittest.main() 