import unittest

from users.services import report_generator


class ReportGeneratorTest(unittest.TestCase):
    def test_generate_report(self):
        report = report_generator.generate_report(1)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
