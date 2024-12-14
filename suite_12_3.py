import unittest
import test_12_3


runTest = unittest.TestSuite()
runTest.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
runTest.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runTest)