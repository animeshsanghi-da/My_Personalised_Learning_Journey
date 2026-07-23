def heading(title):
    print(f"\n{'=' * 40}\n{title}\n{'-' * 40}")

def note(message):
    print(f"(Note: {message})\n{'-' * 40}")


heading("1. Extracting Dates and Codes from Log Files")
log_entry = "2026-04-23_ERROR_502_SERVER_TIMEOUT"
date = log_entry[:10]           
error_code = log_entry[17:20]   
print(f"Date: {date}, \nCode: {error_code}")


heading("2. Cleaning Currency and Percentage Data (Trimming)")
note("Often you need to strip off currency symbols or percentage signs to convert to floats")
revenue_str = "$1,250,000.00"
clean_revenue = revenue_str[1:] 
print(f"Clean Revenue: {clean_revenue}")

margin_str = "45.5%"
clean_margin = margin_str[:-1]  
print(f"Clean Margin: {clean_margin}")


heading("3. Extracting File Extensions (Negative Slicing)")
note("Useful when processing directories of raw data")
filename = "Q1_Financial_Report.csv"
extension = filename[-4:]       
file_basename = filename[:-4]   
print(f"Basename: {file_basename}")
print(f"Extension: {extension}")


heading("4. Parsing Structured Identifiers")
note("Standardized IDs (like Product IDs or Transaction IDs) often hold categorical data")
transaction_id = "US-CA-90210-TXN8842"
country = transaction_id[0:2]   
state = transaction_id[3:5]     
zip_code = transaction_id[6:11] 
print(f"Country: {country}, \nState: {state}, \nZip Code: {zip_code}")


heading("5. Fixed-Width Data Extraction")
note("Older database exports often use strict character counts instead of commas")
fw_record = "1001John Doe  Sales     $55000"
emp_id = fw_record[0:4].strip()     
name = fw_record[4:14].strip()      
dept = fw_record[14:24].strip()     
salary = fw_record[24:].strip()     
print(f"ID: {emp_id}, \nName: {name}, \nDept: {dept}, \nSalary: {salary}")


heading("6. Truncating Text for Dashboards/Visualizations")
note("Long categorical names can ruin dashboard layouts")
product_desc = "Ergonomic Office Chair with Lumbar Support"
short_desc = product_desc[:15] + "..." 
print(f"Shortened Description: {short_desc}")


heading("7. Extracting Domain from Email Addresses (Using find + slice)")
email = "analyst@datainsights.com"
at_symbol_index = email.find('@')
domain = email[at_symbol_index + 1:] 
print(f"Domain: {domain}")


heading("8. Time-Series Downsampling Simulation (Stepping)")
note("While usually done on lists or arrays, stepping represents taking every Nth data point")
sensor_data_string = "123456789"
downsampled = sensor_data_string[::3] 
print(f"Downsampled Data: {downsampled}")