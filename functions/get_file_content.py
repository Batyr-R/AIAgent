import os
def get_file_content(working_directory, file_path):
    try:
        working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not full_path.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(full_path, "r") as f:
            max_char = 10000
            file_content_string = f.read(max_char)
            if len(file_content_string) > max_char:
                file_content_string = f'{file_content_string}[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f'Error: {e}'
    return file_content_string
