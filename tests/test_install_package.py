import subprocess
import sys
import pytest
import shutil

@pytest.fixture
def create_venv(tmp_path):
    venv_dir = tmp_path / ".venv"
    subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
    yield venv_dir  
    shutil.rmtree(venv_dir)  


def test_install_in_editable_mode(create_venv):
    activate_script = create_venv / "bin" / "activate" if sys.platform != "win32" else create_venv / "Scripts" / "activate"
    shell = False if sys.platform != "win32" else True
    
   
    commands = [
        f"source {activate_script}",
        "pip install -e '.[test]'"
    ]
    
    
    process = subprocess.Popen(["/bin/bash", "-c", " && ".join(commands)], shell=shell)
    process.communicate()
    
    
    assert process.returncode == 0, "Installation in editable mode failed"

