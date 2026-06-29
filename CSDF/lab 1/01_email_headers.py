import email
import sys

try:
    with open('email.eml') as f:
        msg = email.message_from_file(f)
except FileNotFoundError:
    print("Error: 'email.eml' file not found in the current directory.")
    sys.exit(1)
except IOError as e:
    print(f"Error reading 'email.eml': {e}")
    sys.exit(1)

parser = email.parser.HeaderParser()
headers = parser.parsestr(msg.as_string())

print('Headers Found: ')
for i in headers.items():
    print(i)

header_items = headers.items()
if len(header_items) > 6:
    x = header_items[6][-1]
    print(f'SPF and DKIM is {x}')
else:
    print('Warning: Not enough headers to extract SPF and DKIM info.')
