#Модульные тесты с использованием TDD

import unittest

from ref import HardDrive, Computer, list_computers_with_hard_drives, average_capacity_per_computer, list_large_hard_drives, create_test_data

class TestComputerFunctions(unittest.TestCase):

    def setUp(self):
        self.computers = create_test_data()

    def test_list_computers_with_hard_drives(self):
        result = list_computers_with_hard_drives(self.computers)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], "Gaming PC")
        self.assertEqual(len(result[0]['hard_drives']), 2)

    def test_average_capacity_per_computer(self):
        result = average_capacity_per_computer(self.computers)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], "Gaming PC")
        self.assertAlmostEqual(result[0][1], 1500.0)  # Средняя вместимость для Gaming PC

    def test_list_large_hard_drives(self):
        result = list_large_hard_drives(self.computers)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].model, "Western Digital Blue")

if __name__ == '__main__':
    unittest.main()
