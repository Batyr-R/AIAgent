import os
def get_files_info(working_directory, directory="."):
    try:
        working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, directory))
        if not full_path.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            print("working_directory:", working_directory)
            print("full_path:", full_path)
            return f'Error: "{directory}" is not a directory'
        contents = os.listdir(full_path)
        lines = []
        for item in contents:
            item_path = os.path.join(full_path, item)
            is_dir = os.path.isdir(item_path)
            size = os.path.getsize(item_path)
            lines.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}')
    except Exception as e:
        return f'Error: {e}'
    return"\n".join(lines)
