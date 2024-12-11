import unittest
import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        pervii = Runner('первый')
        # for i in range(9):   # проверка неуспешного теста (вывод ниже)
        for i in range(10):
            pervii.walk()
        self.assertEqual(pervii.distance, 50)

    def test_run(self):
        vtoroi = Runner('второй')
        for i in range(10):
            vtoroi.run()
        self.assertEqual(vtoroi.distance, 100)

    def test_challenge(self):
        pervii = Runner('первый')
        vtoroi = Runner('второй')
        for i in range(10):
            pervii.walk()
            vtoroi.run()
        self.assertNotEqual(pervii.distance, vtoroi.distance)


if __name__ == '__main__':
    unittest.main()


