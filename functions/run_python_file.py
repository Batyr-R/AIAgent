import subprocess
import os

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not full_path.startswith(working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'
        if not full_path.endswith("py"):
            return f'Error: "{file_path}" is not a Python file.'
        command = ["python", file_path] + args
        result = subprocess.run(command, timeout=30, capture_output=True, cwd=working_directory, text=True)
        output = f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        if result.returncode != 0:
            output += f"\nProcess exited with code {result.returncode}"
        if not result.stdout and not result.stderr:
            return "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
    return output
