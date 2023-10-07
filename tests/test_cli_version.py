import pytest
import subprocess


@pytest.fixture
def run_cli_command():
    # This fixture runs the CLI command and captures its output
    def run_command():
        # Run the CLI command and capture its output
        result = subprocess.run(["python", "-m", "src.interviewkit.cli", "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        return result
    
    return run_command


class TestCLIVersion():
    
    def test_version_option(self, run_cli_command):
        result = run_cli_command()

        assert result.returncode == 0

        # Check if the version number is correct
        assert f"HistoryAIToolKit: 0.0.1" in result.stdout