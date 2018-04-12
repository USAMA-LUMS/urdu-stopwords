"""Read the raw urdu stop word list and sorted it"""

lines = set(open('raw.txt', 'r'))
lines = sorted(lines)

print("Total raw stop words count {}".format(len(lines)))


def chunk_it(seq, num):
    """
    Converted list into multiple sub list
    Args:
        seq: list
        num: integer

    Returns:
        list
    """
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


# Printing the Urdu stop words lists
for line in sorted(lines):
    print(line.strip())

lists = chunk_it(lines, 17)

for word_list in lists:
    string_print = ""
    for line in word_list:
        string_print = string_print + " " + line.strip()

    print(string_print)
    string_print = ""
