from MDP import MDP
import unittest 

class MDPTestCase(unittest.TestCase):
    def test_smallMDP(self):
        lst = [['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd']]
        self.mdp = MDP(lst)
        self.mdp.run()
        tp = self.mdp.getTransitionProbs()
        
        solution = {'a': {'b': 1}, 'b': {'c':1}, 'c' : {'d': 1}}
        self.assertEqual(tp, solution)

        
    

if __name__ == '__main__':
    unittest.main() 