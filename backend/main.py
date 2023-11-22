from sheets_api import SheetsAPI

def main():
    # Create an instance of the SheetsAPI class
    sheets_api = SheetsAPI()

    # Define the range you want to read or write to
    test_range = 'Sheet1!A1:D5'  # Update this range as per your sheet's layout

    # # Example: Reading from the Sheet
    data = sheets_api.read_sheet(test_range)
    if data:
        print("Read data from the sheet:")
        for row in data:
            print(row)

    # Example: Writing to the Sheet
    # This is an example data format to write to the sheet. Update as necessary.
    values_to_write = [
        ["Date", "Activity", "Duration", "Remarks"],
        ["2023-01-01", "Running", "30", "Felt good"],
        ["2023-01-02", "Yoga", "45", "Relaxing"]
    ]
    write_result = sheets_api.write_to_sheet(test_range, values_to_write)
    if write_result:
        print("Wrote data to the sheet.")

if __name__ == '__main__':
    main()
