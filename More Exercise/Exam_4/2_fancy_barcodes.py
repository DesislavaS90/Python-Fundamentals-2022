import re

count_of_barcodes = int(input())

for i in range(count_of_barcodes):
    barcode = input()
    pattern = r'(@[#]{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@[#]{1,})'
    result = re.match(pattern, barcode)

    if result:
        digit_pattern = r'\d+'
        digit = re.findall(digit_pattern, result.group())
        if digit:
            print(f"Product group: {''.join(digit)}")
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')


# Each line must not contain anything else but a valid barcode. A barcode is valid when:
# It is surrounded by a "@" followed by one or more "#"
# It is at least 6 characters long (without the surrounding "@" or "#")
# It starts with a capital letter
# It contains only letters (lower and upper case) and digits
# It ends with a capital letter

# Examples of valid barcodes: @###Che46sE@##, @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##
# Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#

# Next, you have to determine the product group of the item from the barcode. The product group is obtained by concatenating all the digits found in the barcode. If there are no digits present in the barcode, the default product group is "00".
# Examples:
# @#FreshFisH@# -> product group: 00
# @###Brea0D@### -> product group: 0
# @##Che4s6E@## -> product group: 46
