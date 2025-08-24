def read_and_write_file():
    try:
        # Ask user for the filename
        filename = input("Enter the filename to read: ")

        # Open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Example modification: convert text to uppercase
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




        
read_and_write_file()
