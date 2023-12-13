def main():
    # Define the pm function
    pm_function = """
pm() {
    # Replace slashes with dots and remove the '.py' extension
    module_path=$(echo "$1" | sed 's/\//./g' | sed 's/\\.py$//')
    # Run the Python module
    python3 -m "$module_path"
}
"""

    # Determine which shell configuration file to use
    shell_config_file = '~/.zshrc' if os.path.exists(os.path.expanduser('~/.zshrc')) else '~/.bashrc'
    shell_config_file_path = os.path.expanduser(shell_config_file)

    # Check if pm function already exists
    with open(shell_config_file_path, 'r') as file:
        if ' pm()' in file.read():
            print(f"Error: 'pm' function already exists in {shell_config_file}")
            sys.exit(1)

    # Append the pm function to the shell configuration file
    with open(shell_config_file_path, 'a') as file:
        file.write(pm_function)

    print(f"'pm' function added to {shell_config_file}. Please run 'source {shell_config_file}' to activate it.")
