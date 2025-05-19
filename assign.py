import re

# Email validation
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

# URL validation
def is_valid_url(url):
    pattern = r'^https?://(?:[\w\-]+\.)+[a-z]{2,6}(?:/[\w\-./?%&=]*)?$'
    return re.match(pattern, url) is not None

# Phone number validation
def is_valid_phone(phone):
    pattern = r'^(\(\d{3}\)\s|\d{3}[-.])\d{3}[-.]\d{4}$'
    return re.match(pattern, phone) is not None

# Currency amount validation
def is_valid_currency(amount):
    pattern = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$'
    return re.match(pattern, amount) is not None

# Example usage
test_data = {
    "emails": [
        "user@example.com",
        "firstname.lastname@company.co.uk",
        "bad-email@"
    ],
    "urls": [
        "https://www.example.com",
        "https://subdomain.example.org/page",
        "htp://wrong.url"
    ],
    "phones": [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "4567890"
    ],
    "currencies": [
        "$19.99",
        "$1,234.56",
        "$123456.78"
    ]
}

# Testing all fields
for email in test_data["emails"]:
    print(f"Email '{email}' is valid? {is_valid_email(email)}")

for url in test_data["urls"]:
    print(f"URL '{url}' is valid? {is_valid_url(url)}")

for phone in test_data["phones"]:
    print(f"Phone '{phone}' is valid? {is_valid_phone(phone)}")

for currency in test_data["currencies"]:
    print(f"Currency '{currency}' is valid? {is_valid_currency(currency)}")

