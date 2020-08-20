"""
This program submits a list of security ticker symbols to a specific
URL and uses the retrieved information to create a CSV file containing
the security ticker symbols with their respective current prices,
52-week high price, and 52-week low price.
"""

# Import modules to obtain date and time, create a CSV file and read
# and write to it, retrieve a webpage, and perform searches using
# regular expressions
import datetime, csv, urllib.request, re

# Define the create_csv_file() function
def create_csv_file():
    """
    This function creates a filename for a CSV file, creates the CSV
    file, and writes a header row.
    """

    # Provide a base for the filename
    filename_base = "Security_Prices_"
    # Generate the current year, month, day, hour, minute, and seconds
    # in a string format
    current_date_and_time = datetime.datetime.today().strftime("%Y-%m-%d-%H%M-%S")
    # Generate a filename for the CSV file
    filename = filename_base + current_date_and_time + ".CSV"
    # Create a CSV file using the filename and create a header row
    with open(filename, "w", newline="") as csv_file:
        symbols_and_prices = csv.writer(csv_file, dialect="excel")
        symbols_and_prices.writerow(["SECURITY",
                                     "LAST",
                                     "52-WK H",
                                     "52-WK L"])
    return filename

# Create the update_csv_file() function
def update_csv_file(symbol_list_submitted, filename):
    """
    This function receives a list of security ticker symbols and a
    filename and then:

    1. Appends the list of security ticker symbols to a base URL.

    2. Submits the URL and retrieves the webpage.

    3. Using regular expressions, searches for:

       a. The ticker symbol,
       b. The current price,
       c. The 52-week high price, and
       d. The 52-week low price

       and creates a list for each of these four information elements.

    4. Generates a value for the lengthe of each created list that
       will later be compared to each other to help ensure the
       integrity of the lists.

    5. Appends the list information to an existing CSV file.
    """

    # Provide an URL base for ticker symbol submissions
    url_base = "https://www.cnbc.com/quotes/?symbol="
    # Append ticker symbols to the URL base
    for symbol in symbol_list_submitted:
        url_base = url_base + symbol + ","
    # Remove the last comma
    url = url_base[:-1]
    # How does the URL to be submitted look?
    print("Submitting and retrieving: {}".format(url))
    print()
    # Submit the URL
    web_page_content = urllib.request.urlopen(url)
    # Iterate on the returned results
    for line in web_page_content:
        # Decode for the local character set and remove extraneous
        # white space
        line.decode().strip()
        # Search for the information contained in a <script>
        if "var symbolInfo = [" in str(line):
            # Get the ticker symbol from the returned information
            symbol_list = re.findall(r'\"symbol\":\"([A-Z]+)\"', str(line))
            # Generate a check figure to make sure all of the lists
            # are the same length
            list_len_1 = len(symbol_list)
            # Get the current price for the ticker symbol
            current_price_list = re.findall(r'\"values\":\{\"A\":\"([0-9]+\.[0-9]+)\"', str(line))
            # Generate a check figure to make sure all of the lists
            # are the same length
            list_len_2 = len(current_price_list)
            # Get the 52-week low for the ticker symbol
            year_low_list = re.findall(r'\"yrloprice\":\"([0-9]+\.[0-9]+)\"', str(line))
            # Generate a check figure to make sure all of the lists
            # are the same length
            list_len_3 = len(year_low_list)
            # Get the 52-week high for the ticker symbol
            year_high_list = re.findall(r'\"yrhiprice\":\"([0-9]+\.[0-9]+)\"', str(line))
            # Generate a check figure to make sure all of the lists
            # are the same length
            list_len_4 = len(year_high_list)
            # Check whether each list is the same length
            if (list_len_1 ==
                list_len_2) and (list_len_3 ==
                                 list_len_4) and (list_len_1 ==
                                                  list_len_4):
                print("SUCCESS! The created lists are equal length.")
            else:
                print("ERROR! The created lists are NOT equal length.")
            print()
    # Append the ticker symbol information to an existing CSV file
    with open(filename, "a", newline="") as csv_file:
        symbols_and_prices = csv.writer(csv_file, dialect="excel")
        for iteration in range(len(symbol_list_submitted)):
            symbols_and_prices.writerow([symbol_list[iteration],
                                         float(current_price_list[iteration]),
                                         float(year_high_list[iteration]),
                                         float(year_low_list[iteration])])

# Call the create_csv_file() function to create a filename for the CSV
# file and create the CSV file
filename = create_csv_file()
# The first of six lists that will be submitted
symbol_list_a = ["VTI", "VOO", "VTV", "VUG", "VO", "VOE", "VOT", "VB",
                 "VBR", "VBK", "VXUS", "VEA", "VWO", "VSS", "VGT",
                 "VHT", "VNQ", "BND", "VCSH", "VCIT", "VCLT"]
# Submit the filename and first list to the update_csv_file()
# function to update the CSV file
update_csv_file(symbol_list_a, filename)
# The second of six lists that will be submitted
symbol_list_b = ["SPTM", "SPLG", "SPYV", "SPYG", "SPMD", "MDYV",
                 "MDYG", "SPSM", "SLYV", "SLYG", "SPDW", "EFV",
                 "EFG", "SPEM", "GWX", "USRT", "HAUZ", "SPAB",
                 "IAGG", "SPSB", "SPIB", "SPLB", "HYLB"]
# Submit the filename and second list to the update_csv_file()
# function to update the CSV file
update_csv_file(symbol_list_b, filename)
# The third of six lists that will be submitted
symbol_list_c = ["SWTSX", "SCHB", "VIIIX", "SWPPX", "SWLVX", "SCHV",
                 "SWLGX", "SCHG", "SWMCX", "SCHM", "MDYV", "MDYG",
                 "SWSSX", "SCHA", "SLYV", "SLYG", "SWISX", "SCHF",
                 "SCHE", "SCHC", "FNDF", "FNDE", "FNDC", "SCHH",
                 "RWX", "SWAGX", "SCHZ", "SWSBX", "SCHO", "SCHJ",
                 "SCHR", "SCHI", "SWRSX", "SCHP", "SPTL", "SCHQ"]
# Submit the filename and third list to the update_csv_file()
# function to update the CSV file
update_csv_file(symbol_list_c, filename)
# The fourth of six lists that will be submitted
symbol_list_d = ["VTSAX", "VTI", "VFIAX", "VOO", "VIMAX", "VO",
                 "VSMAX", "VB", "VTIAX", "VXUS", "VTMGX", "VEA",
                 "VEMAX", "VWO", "VSS", "VGSLX", "VNQ", "VHT", "VGT",
                 "VASGX", "VBTLX", "BND", "VWEHX"]
# Submit the filename and fourth list to the update_csv_file()
# function to update the CSV file
update_csv_file(symbol_list_d, filename)
# The fifth of six lists that will be submitted
symbol_list_e = ["FZROX", "FSKAX", "FNILX", "FXAIX", "FLCOX",
                 "FSPGX", "FZIPX", "FSMAX", "FSMDX", "FSSNX",
                 "FZILX", "FTIHX", "FSGGX", "FSPSX", "FPADX",
                 "FSRNX", "FXNAX", "FNSOX", "FUAMX", "FNBGX",
                 "FIPDX"]
# Submit the filename and fifth list to the update_csv_file()
# function to update the CSV file
update_csv_file(symbol_list_e, filename)
# The last of six lists that will be submitted
symbol_list_f = ["FXAIX", "FSMAX", "FSPSX", "DFEMX", "CSRSX",
                 "VBTIX", "SPHIX"]
# Submit the filename and last list to the update_csv_file()
# function to update the CSV file
update_csv_file(symbol_list_f, filename)
