import copy


def find_index_of_mismatch(patternList):
    low_index = 0
    high_index = len(patternList) - 1

    while low_index < high_index:
        if patternList[low_index] != patternList[high_index]:
            return low_index
        else:
            low_index += 1
            high_index -= 1

    return None


def find_possible_palindrome_using_index(patternList, index):
    newPatternRemoveLowIndex = copy.deepcopy(patternList)
    del newPatternRemoveLowIndex[index]
    if newPatternRemoveLowIndex == list(reversed(newPatternRemoveLowIndex)):
        return newPatternRemoveLowIndex

    else:
        newPatternRemoveHighIndex = copy.deepcopy(patternList)
        del newPatternRemoveHighIndex[len(patternList) - index - 1]
        if newPatternRemoveHighIndex == list(reversed(newPatternRemoveHighIndex)):
            return newPatternRemoveHighIndex

    return None


def find_new_palindrome_from_palindrome(patternList):
    newPalindrome = None
    index = 0

    while newPalindrome is None:
        newPalindrome = find_possible_palindrome_using_index(patternList, index)
        if newPalindrome is not None:
            break

        index += 1
        if index >= (len(patternList)):
            break

    return newPalindrome


def find_palindrome(pattern):
    if pattern is None:
        return None
    if type(pattern) is not tuple:
        return None
    if len(pattern) < 3:
        return None

    patternList = list(pattern)
    mismatchIndex = find_index_of_mismatch(patternList)

    # The input pattern is not already a palindrome
    if mismatchIndex is not None:
        newPalindrome = find_possible_palindrome_using_index(patternList, mismatchIndex)
    else:
        newPalindrome = find_new_palindrome_from_palindrome(patternList)

    if newPalindrome is None:
        return None
    else:
        return (tuple)(newPalindrome)
