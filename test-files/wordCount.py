

def exercise_2():
    with open('Hamlet.txt', 'r') as f:
        lines = 0
        words = 0
        characters = 0
        for line in f.readlines():
            characters += len(line)
            lines += 1
            if line == '':
                continue
            line.strip()
            words_unfiltered = line[:-1].split(' ')
            for word in words_unfiltered:
                if word == '':
                    continue
                words += 1

        print(f'There are {lines} lines')
        print(f'The file has {words} words')
        print(f'The file is {characters} bytes/characters')  # Each character is 1 byte!
        print(characters)


def exercise_3():
    special_chars = ['(', ')', '!', '.', ';', ',', '?', ':']
    with open('Hamlet.txt', 'r') as f:
        words = set()
        for line in f.readlines():
            line.strip()
            if line[-1] == '\n':
                line = line[:-1]
            words_unfiltered = line.split()
            for word in words_unfiltered:
                word = word.lower()
                for special_char in special_chars:
                    if special_char in word:
                        word = word.replace(special_char, '')
                words.add(word)
        print('There are', len(words), 'words')


def exercise_4():
    special_chars = ['(', ')', '!', '.', ';', ',', '?', ':']
    with open('Hamlet.txt', 'r') as f:
        words = {}
        for line in f.readlines():
            line.strip()
            if line[-1] == '\n':
                line = line[:-1]
            words_unfiltered = line.split()
            for word in words_unfiltered:
                word = word.lower()
                for special_char in special_chars:
                    if special_char in word:
                        word = word.replace(special_char, '')
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1

        keys = []
        values = []
        for key, value in words.items():
            keys.append(key)
            values.append(value)

        for i in range(20):
            common_word = keys[values.index(max(values))]
            common_count = max(values)
            print(f"{i + 1}: Word '{common_word}' used {common_count} times")
            values.remove(common_count)
            keys.remove(common_word)


def exercise_5():
    special_chars = ['(', ')', '!', '.', ';', ',', '?', ':', '\n',
                     '[', ']', ' ', '', "'", '"', '-', '&', '1']
    # BETTER TO MAKE THIS PART A REGEX, and then REGEX REPLACE!!!
    with open('Hamlet.txt', 'r') as f:
        characters = set()
        for line in f.readlines():
            line.strip()
            for character in line:
                if character in special_chars:
                    continue
                character = character.lower()
                characters.add(character)

        print(characters)
