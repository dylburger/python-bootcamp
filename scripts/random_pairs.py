import random


def pair_generator(filename):
    """Return an iterator of random pairs from a list of numbers."""
    # Keep track of already generated pairs

    with open(filename, 'r') as f:
        students = set(f.read().splitlines())

    paired_students = set()

    while students:
        pair = random.sample(students, 2)
        paired_students.add(tuple(pair))
        students -= set(pair)
        # check for odd number
        if len(students) == 1:

            pair = random.choice(list(paired_students))
            paired_students -= {pair}
            pair = pair + (students.pop(),)
            paired_students.add(pair)
            students = 0
    return list(paired_students)


if __name__ == '__main__':
    pairs = pair_generator('attending_students.txt')

    with open('random_pairs.txt', 'w') as f:
        for pair in pairs:
            line = ', '.join(str(stud) for stud in pair)
            f.write(line + '\n')
