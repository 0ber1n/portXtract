import re

def extract_ports_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expression to find port numbers
    port_matches = re.findall(r'(\d+)/tcp\s+open\s+\w+', content)

    # Extract the port numbers and remove spaces
    port_numbers = [match.replace(" ", "") for match in port_matches]

    return port_numbers

def main():
    file_path = input("Enter the path to the text file: ")

    try:
        port_numbers = extract_ports_from_file(file_path)

        if port_numbers:
            print("Port numbers:", ','.join(port_numbers))
        else:
            print("No port numbers found in the file.")

    except FileNotFoundError:
        print("File not found. Please make sure the file exists, and the path is correct.")

if __name__ == "__main__":
    main()
