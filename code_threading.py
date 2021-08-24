from permutations import email_permuter
# from itertools import permutations
from validate_email import validate_email
# import requests

import time


import concurrent.futures  # for threading


# For tracking time
t1 = time.perf_counter()

# validate_email(email_address='sahilraza102@gmail.com'check_format=True, check_blacklist=True, check_dns=True, dns_timeout=10, check_smtp=True, smtp_timeout=10, smtp_helo_host='my.host.name', smtp_from_address='my@from.addr.ess', smtp_debug=False)
# is_valid = validate_email(email_address='sahilraza102@gmail.com')


def validate_user_email(email):
    is_valid = validate_email(email)
    print(f"{email} >>>>>>> {is_valid}")
    print(time.perf_counter())


# email_list = [
#     'sahilraza102@gmail.com',
#     'sahil000102@gmail.com',
#     'sahil001102@gmail.com',
#     'sahil002102@gmail.com',
#     'sahil003102@gmail.com',
# ]

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(validate_user_email, email_list)


# print("Valid ?: ",is_valid)


# Permutations

# Get all permutations of [1, 2, 3]


# Specify the first name, last name and domain name
# first_name = "Pratik"
# last_name = "Dani"
# domain_name = "gmail.com"
# first_name = "Shivam"
# last_name = "Mittal"
# domain_name = "idearise.co"
first_name = "Shahbaz"
last_name = "Haidar"
domain_name = "idearise.co"

permuted_emails = email_permuter.all_email_permuter(
    first_name=first_name,
    last_name=last_name,
    domain_name=domain_name
)

print(permuted_emails)

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')


result = [
    'pratik.dani@gmail.com', 'dani.pratik@gmail.com',
    'pratik_dani@gmail.com', 'dani_pratik@gmail.com',
    'pratik-dani@gmail.com', 'dani-pratik@gmail.com',
    'pratik.d@gmail.com', 'd.pratik@gmail.com',
    'pratik_d@gmail.com', 'd_pratik@gmail.com',
    'pratik-d@gmail.com', 'd-pratik@gmail.com',
    'p.dani@gmail.com', 'dani.p@gmail.com',
    'p_dani@gmail.com', 'dani_p@gmail.com',
    'p-dani@gmail.com', 'dani-p@gmail.com',
    'p.d@gmail.com', 'd.p@gmail.com', 'p_d@gmail.com',
    'd_p@gmail.com', 'p-d@gmail.com', 'd-p@gmail.com',
    'pratikdani@gmail.com', 'danipratik@gmail.com',
    'pratikd@gmail.com', 'dpratik@gmail.com', 'pdani@gmail.com',
    'danip@gmail.com', 'pd@gmail.com', 'dp@gmail.com',
    'pratik@gmail.com', 'dani@gmail.com'
]

result2 = [
    'shivam.mittal@idearise.co', 'mittal.shivam@idearise.co',
    'shivam_mittal@idearise.co', 'mittal_shivam@idearise.co',
    'shivam-mittal@idearise.co', 'mittal-shivam@idearise.co',
    'shivam.m@idearise.co', 'm.shivam@idearise.co',
    'shivam_m@idearise.co', 'm_shivam@idearise.co',
    'shivam-m@idearise.co', 'm-shivam@idearise.co',
    's.mittal@idearise.co', 'mittal.s@idearise.co',
    's_mittal@idearise.co', 'mittal_s@idearise.co',
    's-mittal@idearise.co', 'mittal-s@idearise.co',
    's.m@idearise.co', 'm.s@idearise.co', 's_m@idearise.co',
    'm_s@idearise.co', 's-m@idearise.co', 'm-s@idearise.co',
    'shivammittal@idearise.co', 'mittalshivam@idearise.co',
    'shivamm@idearise.co', 'mshivam@idearise.co',
    'smittal@idearise.co', 'mittals@idearise.co',
    'sm@idearise.co', 'ms@idearise.co', 'shivam@idearise.co',
    'mittal@idearise.co'
]
