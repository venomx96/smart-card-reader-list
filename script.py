from smartcard.System import readers

def get_reader_serial_numbers():
    reader_list = readers()
    
    if len(reader_list) == 0:
        print("No card reader found.")
        return None

    try:
        # Specify the full path to the text file where you want to save the reader names.
        # Modify the path below as needed.
        file_path = "list.txt"

        with open(file_path, 'w') as file:
            for reader in reader_list:
                reader_name = str(reader)  # Convert 'PCSCReader' object to a string
                file.write("" + reader_name + "\n")
                print("Smart Card reader name:", reader_name)

        print("Reader names saved to file:", file_path)

    except Exception as e:
        print("Error saving reader names to file:", str(e))

if __name__ == "__main__":
    get_reader_serial_numbers()
