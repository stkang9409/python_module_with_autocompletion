def main():
    if len(sys.argv) < 2:
        print("Usage: python -m your_package_name <script_path>")
        sys.exit(1)

    script_path = sys.argv[1]

    # Replace slashes with dots and remove the '.py' extension
    module_path = script_path.replace('/', '.').replace('.py', '')

    # Run the Python module
    try:
        subprocess.run(['python3', '-m', module_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running module {module_path}: {e}")
        sys.exit(1)

