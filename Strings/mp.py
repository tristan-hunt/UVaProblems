# /* UVa problem: 11837.py
#  * Musical Plagiarism
#  * Topic: Strings
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *   Given two melodies, decide if the second melody can be found,
#  *   in any key, in the first
#  * Solution Summary:
#  *  Step 1- Translate notes to intervals, convert to strings. 
#  *  Use KMP pattern-matching algorithm to quickly compare the strings
#  *  
#  * Used Resources:
#  * Uses python implementation of string-matching alg. found here:
#  * http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

import sys

def intervalize(notes, strlen):
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

# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
 
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
 
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            return 1
            #print "Found pattern at index " + str(i-j)
            j = lps[j-1]
 
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return(0)
 
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
 
    lps[0] # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]==pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1



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
    match = KMPSearch(pattern, text)
    if match == 1:
        sys.stdout.write("S\n")
    else:
        sys.stdout.write("N\n")
	#sys.stdout.write("{}\n".format("".join([str(m) for m in match])))