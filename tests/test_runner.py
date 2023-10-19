from moq_interop.runner import Runner

import unittest
import json


class TestRunner(unittest.TestCase):

    def test_permutations(self):
        with open("tests/fixtures/implementations.json") as fixture:
            implementations = json.load(fixture)

        results = Runner.generate_permutations(implementations)
        expected = [
            ["orange", "apple"],
            ["orange", "banana"],
            ["banana", "apple"],
            ["banana", "banana"]
        ]
        self.assertCountEqual(results, expected)

        self.assertTrue(True)
