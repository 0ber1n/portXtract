import re
import getpass

def extract_ports_from_file(content):
    # Use regular expression to find port numbers
    port_matches = re.findall(r'(\d+)/tcp\s+open\s+\w+', content)

    # Extract the port numbers and remove spaces
    port_numbers = [match.replace(" ", "") for match in port_matches]

    return port_numbers

def main():
    print("Welcome to portXtract!")
    print("Select an option:")
    print("1. Enter the path to a text file")
    print("2. Enter the contents directly")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        file_path = input("Enter the path to the text file: ")

        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print("File not found. Please make sure the file exists, and the path is correct.")
            return

    elif choice == '2':
        print("Enter the contents below (press Ctrl + D to finish input):")
        content = ''
        try:
            while True:
                line = input()
                content += line + '\n'
        except EOFError:
            pass

    else:
        print("Invalid choice. Exiting.")
        return

    try:
        port_numbers = extract_ports_from_file(content)

        if port_numbers:
            print("Port numbers:", ','.join(port_numbers))
        else:
            print("No port numbers found in the input.")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
