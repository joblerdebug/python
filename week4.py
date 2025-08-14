def file_read_write_challenge():
    """Reads a file, modifies its content, and writes to a new file with error handling."""
    
    # Get input filename from user with error handling
    while True:
        try:
            input_filename = input("Enter the name of the file to read: ")
            
            # Read the original file
            with open(input_filename, 'r') as file:
                original_content = file.read()
            break
            
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' doesn't exist. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{input_filename}'. Try another file.")
        except IsADirectoryError:
            print(f"Error: '{input_filename}' is a directory, not a file.")
        except UnicodeDecodeError:
            print(f"Error: Couldn't decode the file '{input_filename}'. It might be a binary file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
    
    # Process the content (example modification: convert to uppercase)
    modified_content = original_content.upper()
    
    # Get output filename from user
    while True:
        output_filename = input("Enter the name for the new output file: ")
        
        if output_filename.strip() == "":
            print("Filename cannot be empty. Please try again.")
            continue
            
        try:
            # Write the modified content to a new file
            with open(output_filename, 'w') as file:
                file.write(modified_content)
            print(f"Successfully wrote modified content to '{output_filename}'")
            break
            
        except PermissionError:
            print(f"Error: You don't have permission to write to '{output_filename}'. Try another filename.")
        except IsADirectoryError:
            print(f"Error: '{output_filename}' is a directory, not a file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("=== File Read & Write Challenge with Error Handling ===")
    file_read_write_challenge()