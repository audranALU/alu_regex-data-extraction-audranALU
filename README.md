# alu_regex-data-extraction-audranALU

Regex Validator – Python Script
Welcome to this simple yet handy Python script designed to validate common data formats using Regular Expressions (regex). If you're dealing with email addresses, URLs, phone numbers, or currency values and want a quick way to check their validity, this script has got you covered.

What It Does
This script uses Python’s re module to validate:

Emails (e.g. user@example.com)

URLs (e.g. https://www.example.com)

Phone Numbers (e.g. (123) 456-7890, 123-456-7890, etc.)

Currency Amounts (e.g. $1,234.56)

It also includes a test suite with sample inputs and prints whether each example is valid or not.

File Overview
assign.py

is_valid_email(email) – Checks if an email address is valid.

is_valid_url(url) – Checks if a URL is valid.

is_valid_phone(phone) – Checks if a US-style phone number is valid.

is_valid_currency(amount) – Checks if a currency string follows the $X,XXX.XX format.

A sample dictionary test_data with various examples.

For-loops that run validations on the test data and print out results.

How to Run
Make sure you have Python installed (3.x).

Clone this or download the file.

Open a terminal and run:

bash
Copy
Edit
python assign.py
You'll see output showing which entries passed or failed validation

 Notes
This script is a good starting point, but regex patterns can be tricky. Feel free to modify or expand based on your needs (e.g., adding international phone formats).

Want to use this in another app? Just import the validation functions and use them wherever needed.

Author
Made with focus and a touch of fun by Aurdan Ndayisenga – musician and software engineer in the making


