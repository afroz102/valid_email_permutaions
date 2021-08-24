from itertools import permutations, product


def all_email_permuter(first_name, middle_name, last_name, domain_name):
    """
    Excepts first_name, last_name and domain_name as arguments and returns a
    list of all permutations of possible mail id's.
    """
    first_name = first_name.lower()
    middle_name = middle_name.lower()
    last_name = last_name.lower()
    domain_name = domain_name.lower()

    print(f"Name: {first_name}-{middle_name}-{last_name}-{domain_name}")

    all_names = [
        [first_name, first_name[0]],
        [middle_name, middle_name[0]],
        [last_name, last_name[0]]
    ]

    # print("All Name: ", all_names)

    punctuations = ". _ ".split()

    # print("punctuations: ", punctuations)
    # cartesian product with 2 punctuations
    cartesian_prod_A = list(product(
        all_names[0],
        all_names[1],
        all_names[2],
        punctuations,
        punctuations
    ))
    print("\ncartesian_prod_A: ", cartesian_prod_A)

    # cartesian product with 2 punctuations
    cartesian_prod_B = list(product(
        all_names[0],
        all_names[1],
        all_names[2],
        punctuations
    ))

    print("\ncartesian_prod_B: ", cartesian_prod_B)

    # cartesian product without punctuations
    cartesian_prod_C = list(product(all_names[0], all_names[1], all_names[2]))

    # print("cartesian_prod_C: ", cartesian_prod_C)
    # List comprehension method
    # combinations = [s for x in cartesian_prod_A for s in permutations(
    #     x, 3) if s[0] not in punctuations if s[-1]not in punctuations]
    # print("combination 2: ", combinations)

    combinations = []

    for x in cartesian_prod_A:
        permutations_A_5 = permutations(x, 5)

        for s in permutations_A_5:
            if s[0] not in punctuations:
                if s[-1] not in punctuations:
                    combinations.append(s)

        permutations_A_4 = permutations(x, 4)

        for s in permutations_A_4:
            if s[0] not in punctuations:
                if s[-1] not in punctuations:
                    combinations.append(s)
        # print("xy: ", combinations)

        permutations_A_3 = permutations(x, 3)

        for s in permutations_A_3:
            if s[0] not in punctuations:
                if s[-1] not in punctuations:
                    combinations.append(s)
        # print("xyz: ", combinations2)

    print("combination A: ", len(combinations))
    # print("combination A: ", combinations)

    for x in cartesian_prod_B:
        permutations_A_4 = permutations(x, 4)

        for s in permutations_A_4:
            if s[0] not in punctuations:
                if s[-1] not in punctuations:
                    combinations.append(s)
        # print("xy: ", combinations)

        permutations_A_3 = permutations(x, 3)

        for s in permutations_A_3:
            if s[0] not in punctuations:
                if s[-1] not in punctuations:
                    combinations.append(s)
        # print("xyz: ", combinations2)

    print("combination B: ", len(combinations))


#     combinations.extend(["".join(s) for x in cartesian_prod_C for s in permutations(
#         x, 2) if s[0] not in punctuations if s[-1]not in punctuations])
#
#     print("combination 2: ", combinations)

    # combinations2 = []
    for x in cartesian_prod_C:
        permutations_B_3 = permutations(x, 3)

        for s in permutations_B_3:
            if s[0] not in punctuations:
                if s[-1] not in punctuations:
                    combinations.append(s)

        permutations_B_2 = permutations(x, 2)

        for s in permutations_B_2:
            if s[0] not in punctuations:
                if s[-1] not in punctuations:
                    combinations.append(s)

    print("after prod_c: ", len(combinations))

#
    combinations = ["".join(s) for s in combinations]
#
#     print("combination 3: ", combinations)
#
    combinations.extend([first_name, middle_name, last_name])
#
    print("total size: ", len(combinations))

    # # set method is used to convert any of the iterable to sequence of iterable elements with distinct elements.
    combinations = list(set(combinations))
    print("filtered length: ", len(combinations))
    sorted_combinations = sorted(combinations)

    new_comb = []
    for x in sorted_combinations:
        flag = True
        for i, j in zip(x, x[1:]):
            if i in punctuations:
                if j in punctuations:
                    flag = False
                    break

        if flag is True:
            new_comb.append(x)

    print("new_comb: ", len(new_comb))

    print(new_comb)

#
    permuted_emails = [f"{s}@{domain_name}" for s in combinations]
    # print("permuted_emails: ", permuted_emails)

    return permuted_emails


all_email_permuter("Sahir", "Ali", "Bagga", "xyz.com")
