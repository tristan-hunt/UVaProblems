# Uses python implementation of string-matching alg. found here:
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm

import sys

sys.stdin = open("input.txt") #Remove before submitting

def alphabet_index(c):
    """
    Returns the index of the given character in the English alphabet, counting from 0.
    """
    return ord(c.lower()) - 97 # 'a' is ASCII character 97

def match_length(S, idx1, idx2):
    """
    Returns the length of the match of the substrings of S beginning at idx1 and idx2.
    """
    if idx1 == idx2:
        return len(S) - idx1
    match_count = 0
    while idx1 < len(S) and idx2 < len(S) and S[idx1] == S[idx2]:
        match_count += 1
        idx1 += 1
        idx2 += 1
    return match_count

def fundamental_preprocess(S):
    """
    Returns Z, the Fundamental Preprocessing of S. Z[i] is the length of the substring 
    beginning at i which is also a prefix of S. This pre-processing is done in O(n) time,
    where n is the length of S.
    """
    if len(S) == 0: # Handles case of empty string
        return []
    if len(S) == 1: # Handles case of single-character string
        return [1]
    z = [0 for x in S]
    z[0] = len(S)
    z[1] = match_length(S, 0, 1)
    for i in range(2, 1+z[1]): # Optimization from exercise 1-5
        z[i] = z[1]-i+1
    # Defines lower and upper limits of z-box
    l = 0
    r = 0
    for i in range(2+z[1], len(S)):
        if i <= r: # i falls within existing z-box
            k = i-l
            b = z[k]
            a = r-i+1
            if b < a: # b ends within existing z-box
                z[i] = b
            else: # b ends at or after the end of the z-box, we need to do an explicit match to the right of the z-box
                z[i] = a+match_length(S, a, r+1)
                l = i
                r = i+z[i]-1
        else: # i does not reside within existing z-box
            z[i] = match_length(S, 0, i)
            if z[i] > 0:
                l = i
                r = i+z[i]-1
    return z

def bad_character_table(S):
    """
    Generates R for S, which is an array indexed by the position of some character c in the 
    English alphabet. At that index in R is an array of length |S|+1, specifying for each
    index i in S (plus the index after S) the next location of character c encountered when
    traversing S from right to left starting at i. This is used for a constant-time lookup
    for the bad character rule in the Boyer-Moore string search algorithm, although it has
    a much larger size than non-constant-time solutions.
    """
    if len(S) == 0:
        return [[] for a in range(26)]
    R = [[-1] for a in range(26)]
    alpha = [-1 for a in range(26)]
    #sys.stdout.write("Generate R for S:{} ".format(S))

    for i, c in enumerate(S):
        alpha[alphabet_index(c)] = i
        for j, a in enumerate(alpha):
            R[j].append(a)
    #sys.stdout.write("R: {}\n".format(R))
    return R

def good_suffix_table(S):
    """
    Generates L for S, an array used in the implementation of the strong good suffix rule.
    L[i] = k, the largest position in S such that S[i:] (the suffix of S starting at i) matches
    a suffix of S[:k] (a substring in S ending at k). Used in Boyer-Moore, L gives an amount to
    shift P relative to T such that no instances of P in T are skipped and a suffix of P[:L[i]]
    matches the substring of T matched by a suffix of P in the previous match attempt.
    Specifically, if the mismatch took place at position i-1 in P, the shift magnitude is given
    by the equation len(P) - L[i]. In the case that L[i] = -1, the full shift table is used.
    Since only proper suffixes matter, L[0] = -1.
    """
    L = [-1 for c in S]
    N = fundamental_preprocess(S[::-1]) # S[::-1] reverses S
    N.reverse()
    for j in range(0, len(S)-1):
        i = len(S) - N[j]
        if i != len(S):
            L[i] = j
    return L

def full_shift_table(S):
    """
    Generates F for S, an array used in a special case of the good suffix rule in the Boyer-Moore
    string search algorithm. F[i] is the length of the longest suffix of S[i:] that is also a
    prefix of S. In the cases it is used, the shift magnitude of the pattern P relative to the
    text T is len(P) - F[i] for a mismatch occurring at i-1.
    """
    F = [0 for c in S]
    Z = fundamental_preprocess(S)
    longest = 0
    for i, zv in enumerate(reversed(Z)):
        longest = max(zv, longest) if zv == i+1 else longest
        F[-i-1] = longest
    return F

def string_search(P, T):
    """
    Implementation of the Boyer-Moore string search algorithm. This finds all occurrences of P
    in T, and incorporates numerous ways of pre-processing the pattern to determine the optimal 
    amount to shift the string and skip comparisons. In practice it runs in O(m) (and even 
    sublinear) time, where m is the length of T. This implementation performs a case-insensitive
    search on ASCII alphabetic characters, spaces not included.
    """
    if len(P) == 0 or len(T) == 0 or len(T) < len(P):
        return []

    matches = []

    # Preprocessing
    R = bad_character_table(P)
    L = good_suffix_table(P)
    F = full_shift_table(P)

    k = len(P) - 1      # Represents alignment of end of P relative to T
    previous_k = -1     # Represents alignment in previous phase (Galil's rule)
    while k < len(T):
        i = len(P) - 1  # Character to compare in P
        h = k           # Character to compare in T
        while i >= 0 and h > previous_k and P[i] == T[h]:   # Matches starting from end of P
            i -= 1
            h -= 1
        if i == -1 or h == previous_k:  # Match has been found (Galil's rule)
            matches.append(k - len(P) + 1)
            k += len(P)-F[1] if len(P) > 1 else 1
        else:   # No match, shift by max of bad character and good suffix rules
            char_shift = i - R[alphabet_index(T[h])][i]
            if i+1 == len(P):   # Mismatch happened on first attempt
                suffix_shift = 1
            elif L[i+1] == -1:   # Matched suffix does not appear anywhere in P
                suffix_shift = len(P) - F[i+1]
            else:               # Matched suffix appears in P
                suffix_shift = len(P) - L[i+1]
            shift = max(char_shift, suffix_shift)
            previous_k = k if shift >= i+1 else previous_k  # Galil's rule
            k += shift
    return matches

def intervalize(notes, strlen):
    """
    We want the shortest of the distance between note[i] and note[i+1] going
    both up and down the keyboard.
    """

    if str(type(notes)) == "<class 'str'>":
        notes = notes.split()
    assert(str(type(notes)) == "<class 'list'>")

	# Step 1: Convert each note to its semitone:
    semitones = {"A": 1, "A#": 2, "Bb": 2, "B": 3, "B#": 4, "Cb": 3, "C": 4, "C#": 5, "Db": 5, "D": 6, "D#": 7, "Eb": 7, "E": 8, "E#": 9, "Fb": 8, "F": 9, "F#": 10, "Gb": 10, "G":11, "G#": 12, "Ab": 12}	 
    #sys.stdout.write("{}\n".format([x for x in notes]))

    for i in range(0, strlen-1):
        n1 =semitones[notes[i]]
        n2 = semitones[notes[i+1]]
        dist = n2-n1
        if dist < 0:
            dist = dist + 12
        #sys.stdout.write("{}:{}--> {}:{}= {}\n".format(notes[i], n1, notes[i+1], n2, dist))
        notes[i] = dist
    
    notes.pop()
    #sys.stdout.write("{}\n".format([x for x in notes]))

    # Fun fact: In French, musical notes are relative
    notes = [chr(i+97) for i in notes] 
    notes = "".join([str(note) for note in notes])
    return notes

def ltoi(letters):
    letters = [ord(c)-115 for c in letters]
    return letters


def load():
    line = next(sys.stdin).split()
    while(line[0] != '0' and line[1] != '0'):
        song_length = int(line[0])
        snippet_length = int(line[1])
        song = next(sys.stdin).split()
        snippet = next(sys.stdin).split()

		# Convert song and snippet to a string of intervals:
		#sys.stdout.write("Song: {}\n".format(song))
        song = intervalize(song, song_length)
		#sys.stdout.write("Interval of Song: {}\n".format(song))
		
		#sys.stdout.write("Snippet: {}\n".format(snippet))
        snippet = intervalize(snippet, snippet_length)
		#sys.stdout.write("interval of snippet: {}\n".format(snippet))


        yield(snippet, song)
        line = next(sys.stdin).split()

for (pattern, text) in load():
    sys.stdout.write("Comparing:\n")
    sys.stdout.write("{}\n".format(text))
    sys.stdout.write("{}\n".format(pattern))
    match = string_search(pattern, text)
    if len(match) > 0:
        sys.stdout.write("S\n")
    else:
        sys.stdout.write("N\n")
	#sys.stdout.write("{}\n".format("".join([str(m) for m in match])))