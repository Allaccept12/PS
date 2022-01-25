import collections


def groupAnagram(src):
    anagram = collections.defaultdict(list)

    for word in src:
        anagram[tuple(sorted(word))].append(word)

    return anagram.values()

if __name__ == '__main__':
    print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))
