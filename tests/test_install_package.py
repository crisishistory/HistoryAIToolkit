import subprocess
import unittest
import os
import shutil
import sys

class TestInstallPackage(unittest.TestCase):

    def setUp(self):
        # Create a virtual environment
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        
    def tearDown(self):
        # Clean up: Remove the virtual environment directory after the test
        shutil.rmtree(".venv")
        
    def test_install_in_editable_mode(self):
        # Activate the virtual environment
        activate_script = ".venv/bin/activate" if os.name == "posix" else ".venv\\Scripts\\activate"
        shell = False if os.name == "posix" else True
        
        # Commands to run
        commands = [
            f"source {activate_script}",
            "pip install -e '.[test]'"
        ]
        
        # Run the commands
        process = subprocess.Popen(["/bin/bash", "-c", " && ".join(commands)], shell=shell)
        process.communicate()
        
        # Check if the process was successful
        self.assertEqual(process.returncode, 0)

if __name__ == "__main__":
    unittest.main()
