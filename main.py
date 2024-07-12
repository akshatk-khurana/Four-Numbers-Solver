from helper import operators, op_sorted, add_brackets, remove_brackets


all_combos = []
def find_combos(level, current, nums, target):
    if level == 4:
        for i in nums:
            j = str(current)+str(i)

            valid = True

            if '/0' in j:
                valid = False

            if valid:
                if eval(j) == float(target):
                    exists = False
                    ops = [current[1], current[3], current[5]]
                    if ops == ['+']*3 or ops == ['*']*3:
                        if op_sorted(ops[0], j) in all_combos:
                            exists = True
                    if not exists:
                        if j not in all_combos:
                            all_combos.append(j)

                for l in add_brackets(j):
                    removed = remove_brackets(l)
                    try:
                        if removed not in all_combos and eval(removed) == float(target):
                            all_combos.append(removed)
                    except:
                        continue
    else:
        for i in nums:
            curr_nums = nums.copy()
            curr_nums.remove(i)
            for j in operators:
                k = str(current) + str(i) + j
                find_combos(level+1, k, curr_nums, target)

while True:
    all_combos = []
    target = int(input('Target to make: ', ))
    numbers = list(input('Numbers: '))

    find_combos(1, '', numbers, target)
    if len(all_combos) == 0:
        print('\nNo solutions found.')
    else:
        print('\nNumber of solutions found: ', len(all_combos))
        print('Solutions found: ', *all_combos, sep='\n')

    if input('Continue? [y/n]: ') == 'n':
        break