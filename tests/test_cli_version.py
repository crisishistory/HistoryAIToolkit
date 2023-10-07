import unittest
import subprocess

class TestCLIVersion(unittest.TestCase):
    
    def test_version_option(self):
        # Run the CLI command and capture its output
        result = subprocess.run(["python", "-m", "src.interviewkit.cli", "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        self.assertEqual(result.returncode, 0)

        # Check if the version number is correct
        self.assertIn(f"HistoryAIToolKit: 0.0.1", result.stdout)

if __name__ == '__main__':
    unittest.main()