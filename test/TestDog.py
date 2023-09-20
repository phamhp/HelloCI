import unittest

# import sys

# sys.path.append("/Users/ppham/Documents/PersonalProject/HelloWorld_Git/src")

from src.dog import Dog

# import sys

# sys.path.insert(0, "/Users/ppham/Documents/PersonalProject/HelloWorld_Git/src")


class TestDog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dog = Dog("Peter", 6)

    def TestSit(self):
        self.assertEqual(self.dog.sit(), "Peter is now sitting")


if __name__ == "__main__":
    unittest.main()
