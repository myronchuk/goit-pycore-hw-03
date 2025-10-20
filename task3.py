import re

def normalize_phone(phone_number):
   
    cleaned = re.sub(r'[^\d+]', '', phone_number.strip())
    if cleaned.startswith('+'):
        cleaned = '+' + re.sub(r'[^\d]', '', cleaned[1:])
        if not cleaned.startswith('+380'):
            pass
        return cleaned
    elif cleaned.startswith('380'):
        return '+{}'.format(cleaned)
    else:
        return '+38{}'.format(re.sub(r'[^\d]', '', cleaned))

raw_numbers = [
    "    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
