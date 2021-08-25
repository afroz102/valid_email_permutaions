import concurrent.futures  # for threading
import time
from validate_email import validate_email


def generate_pattern(first_name='',  middle_name='', last_name='', domain=''):
    first_initial = ''
    if len(first_name) > 0:
        first_initial = first_name[0]

    last_initial = ''
    if len(last_name) > 0:
        last_initial = last_name[0]

    middle_initial = ''
    if len(middle_name) > 0:
        middle_initial = middle_name[0]

    patterns = []
    patterns.append(first_name)
    patterns.append(last_name)
    patterns.append(first_name+last_name)
    patterns.append(last_name+first_name)
    patterns.append(first_initial+last_name)

    if len(middle_name) > 0 and middle_name != "":
        patterns.append(middle_name)
        patterns.append(first_name+middle_name+last_name)
        patterns.append(first_initial+middle_initial+'.'+last_name)
        patterns.append(first_initial+'.'+middle_initial+'.'+last_name)

    patterns.append(first_name+'.'+last_name)
    patterns.append(first_initial+'.'+last_name)
    patterns.append(first_name+last_initial)
    patterns.append(first_name+'.'+last_initial)
    patterns.append(first_initial+last_initial)
    patterns.append(first_initial+'.'+last_initial)

    patterns.append(first_name+'_'+last_name)
    patterns.append(last_name+'.'+first_name)
    patterns.append(last_name+first_initial)
    patterns.append(last_name+'.'+first_initial)
    patterns.append(last_initial+first_name)
    patterns.append(last_initial+'.'+first_name)
    patterns.append(last_initial+first_initial)
    patterns.append(last_initial+'.'+first_initial)

    if len(middle_name) > 0 and middle_name != "":
        patterns.append(first_initial+middle_initial+last_name)
        patterns.append(first_name+middle_initial+last_name)
        patterns.append(first_name+'.'+middle_initial+'.'+last_name)
        patterns.append(first_name+'.'+middle_name+'.'+last_name)
        patterns.append(first_initial+middle_initial+'_'+last_name)
        patterns.append(first_name+'_'+middle_initial+'_'+last_name)
        patterns.append(first_name+'_'+middle_name+'_'+last_name)

    patterns.append(first_name+'_'+last_name)
    patterns.append(first_initial+'_'+last_name)
    patterns.append(first_name+'_'+last_initial)
    patterns.append(last_name+'_'+first_name)
    patterns.append(last_name+'_'+first_initial)
    patterns.append(last_initial+'_'+first_name)
    patterns.append(last_initial+'_'+first_initial)

    # if len(domain) > 0:
    #     for pattern_index in range(len(patterns)):
    #         patterns[pattern_index] = patterns[pattern_index]+'@'+domain
    patterns = list(set(patterns))
    permuted_emails = [f"{s}@{domain}" for s in patterns]

    return permuted_emails


# email_list = generate_pattern('shivam', '', 'mittal', 'idearise.co')
# email_list = generate_pattern('shahbaz', '', 'haidar', 'idearise.co')


# For tracking time
# t1 = time.perf_counter()


def validate_user_email(email):
    is_valid = validate_email(email)
    # print(f"{email} >>>>>>> {is_valid}")
    # print(time.perf_counter())
    return {"email": email, "is_valid": is_valid}


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(validate_user_email, email)
#                for email in email_list]
#
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())


# t2 = time.perf_counter()
#
# print(f'Finished in {t2-t1} seconds')
