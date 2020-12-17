import unittest
from calculators.calculators import prefix_op, infix_op


inputs_prefix = ['3', '+ 1 2', '+ 1 * 2 3', '+ * 1 2 3', '- / 10 + 1 1 * 1 2', '- 0 3', '/ 3 2', '- -100 99', '/ -100 99', '+/ -100 99']
results_prefix = ['3', '3', '7', '5', '3', '-3', '1', '-199', '-1', '-1']
inputs_infix = ['( 1 + 2 )', '( 1 + ( 2 * 3 ) )', '( ( 1 * 2 ) + 3 )', '( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )']
results_infix = ['3', '7', '5', '-1']
    

class Tests(unittest.TestCase):

    def test_0(self):
        print('\nprefix test: standard calculations')
        
        for i, o in zip(inputs_prefix, results_prefix):
            result = prefix_op(i)
            print('\ntest input: "{}"; expecting result: {}; actual result: {};'.format(i, o, result))
            self.assertEqual(result, o)

    def test_1(self):
        print('\ninfix test: standard calculations')
        
        for i, o in zip(inputs_infix, results_infix):
            result = infix_op(i)
            print('\ntest input: "{}"; expecting result: {}; actual result: {};'.format(i, o, result))
            self.assertEqual(result, o)

            
if __name__ == '__main__':
    unittest.main()