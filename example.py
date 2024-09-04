import os

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def get_environment_variable(var_name):
    """Gets the value of an environment variable."""
    return os.getenv(var_name)

def process_user_input(user_input):
    """Processes user input by executing a system command."""
    os.system(f'echo {user_input}')

if __name__ == "__main__":
    file_content = read_file("example.txt")
    if file_content:
        print(f"File content: {file_content}")
    
    secret_key = get_environment_variable("SECRET_KEY")
    if secret_key:
        print(f"Secret Key: {secret_key}")
    
    user_input = input("Enter a command: ")
    process_user_input(user_input)
