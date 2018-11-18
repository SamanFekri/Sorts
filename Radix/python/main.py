import copy


# just for positive number integers
def radix(numbers):
    temp = copy.deepcopy(numbers)
    dictionary = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    r = 0
    for num in temp:
        if r < len(str(abs(num))):
            r = len(str(abs(num)))

    for i in range(0, r):
        for num in temp:
            if num >= 10 ** (i + 1):
                dictionary[int(str(num)[i])].append(num)
            else:
                dictionary[0].append(num)

        temp = []
        for j in range(0, 9):
            temp.extend(dictionary[j])
        dictionary = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    return temp


if __name__ == '__main__':
    output = radix([32, 51, 546645, 2323, 34345, 6764, 763, 346, 797, 9])
    print(output)
