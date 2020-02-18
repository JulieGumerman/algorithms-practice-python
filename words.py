from util import Stack, Queue

f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set([w.lower() for w in words])

print(word_set)
print(len(word_set))

def get_neighbors(w):
    neighbors = []

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    letter_list = list(w)
    
    for i in range(len(letter_list)):
        for letter in alphabet:
            temp_word = list(letter_list)
            temp_word[i] = letter
            new_word = "".join(temp_word)
            if new_word in word_set and  new_word != w:
                neighbors.append(new_word)
    return neighbors


def find_ladders(begin_word, end_word):
    q = Queue()

    q.enqueue([begin_word])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        w = path[-1]
        if w == end_word:
            return path
        if w not in visited:
            visited.add(w)
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return None

print(find_ladders("sail", "boat"))