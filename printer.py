#import os
#def printer(filename_):
#    os.startfile("your path " + filename_,"print")
#your server pc needs to be a windows machine
import os
import win32api
import win32print

def print_file(file_path, printer_name):
    try:
        # Open the file to be printed
        file_handle = open(file_path, "rb")

        # Get the default printer's handle
        printer_handle = win32print.OpenPrinter(printer_name)

        # Start a print job
        job_info = win32print.StartDocPrinter(printer_handle, 1, ("Print Job", None, "RAW"))

        # Start a new page in the print job
        win32print.StartPagePrinter(printer_handle)

        # Read and send the file content to the printer
        data = file_handle.read()
        win32api.WritePrinter(printer_handle, data)

        # End the page and print job
        win32print.EndPagePrinter(printer_handle)
        win32print.EndDocPrinter(printer_handle)

    except Exception as e:
        print(f"Error printing: {e}")

    finally:
        # Close the file and printer handles
        file_handle.close()
        win32print.ClosePrinter(printer_handle)

if __name__ == "__main__":
    # Specify the file path and printer name
    file_to_print = "C:\\path\\to\\your\\file.txt"
    printer_name = "Your_Printer_Name"

    # Call the print function
    print_file(file_to_print, printer_name)

