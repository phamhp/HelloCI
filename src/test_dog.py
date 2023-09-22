import unittest
from dog import Dog
import xmlrunner


class TestDog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dog = Dog("Peter", 6)
        # print(self.dog.name)

    def testSit(self):
        self.assertEqual(self.dog.sit(), "Peter is now sitting")


if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output='reports')
    unittest.main()
