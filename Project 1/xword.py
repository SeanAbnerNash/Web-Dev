with open('Words.txt') as wordsf:
    words = wordsf.readlines()

def find_words(length, letters):
    """Find words of a certain length which contain
       the specified positional letters."""
    results = set()
    for w in words:
        w = w.lower().strip()
        if len(w) == length:
            got_one = True
            for loc, let in letters.items():
                if w[loc-1] != let:
                    got_one = False
            if got_one:
                results.add(w)
    return sorted(results)


def suggest(hint_string):
    """Take the hint_string and return the possible words."""
    n_letters = len(hint_string)
    known_letters = {}
    for n, letter in enumerate(hint_string.lower()):
        if letter != '-':
            known_letters[n+1] = letter
    return find_words(n_letters, known_letters)
