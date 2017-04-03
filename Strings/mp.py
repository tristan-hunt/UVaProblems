# Uses python implementation of string-matching alg. found here:
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm

import sys

sys.stdin = open("input.txt") #Remove before submitting

def kmp_table(W):
    pos = 2
    cnd = 0

    T = [None] * len(W)
    T[0] = -1
    T[1] = 0

    # for t in T:
    #     sys.stdout.write("{} ".format(t))
    # sys.stdout.write("\n")
    while (pos < len(W)):
        # first case - substring continues
        if W[pos-1] == W[cnd]:
            T[pos] = cnd + 1
            cnd = cnd + 1
            pos = pos + 1
        # second case: it doesn't, but we can fall back
        elif cnd > 0:
            cnd = T[cnd]
        # third case: we have run out of candidates. 
        else:
            T[pos] = 0
            pos = pos + 1
    # for t in T:
    #     sys.stdout.write("{} ".format(t))
    # sys.stdout.write("\n")
    return T

def kmp_search(S, W):
    # sys.stdout.write("Comparing:\n")
    # sys.stdout.write("{}\n".format(S))
    # sys.stdout.write("{}\n".format(W))
    m = 0
    i = 0
    T = kmp_table(W)
    #print("S: {}, len_s: {}, W: {}, len_w: {}, len_t: {}".format(S, len(S), W, len(W), len(T)));

    while(m+1 < len(S)):
        if W[i] == S[m+1]:
            if i == len(W) - 1:
                return m
            i = i + 1
        else:
            if T[i] > -1:
                m= m+1 - T[i]
                i = T[i]
            else:
                m = m + 1
                i = 0
    return len(S)

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
    match = kmp_search(pattern, text)
    if match > 0:
        sys.stdout.write("S\n")
    else:
        sys.stdout.write("N\n")
	#sys.stdout.write("{}\n".format("".join([str(m) for m in match])))