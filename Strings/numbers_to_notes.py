import sys
semitones = {"A": 1, "A#": 2, "Bb": 2, "B": 3, "B#": 4, "Cb": 3, "C": 4, "C#": 5, "Db": 5, "D": 6, "D#": 7, "Eb": 8, "E": 9, "E#": 10, "Fb": 9, "F": 10, "F#": 11, "Gb": 11, "G": 12, "G#": 13, "Ab": 13}
semitones = {y:x for x, y in semitones.items()}
sys.stdin = open("input.txt")
def load():
    string = ""
    for i in range(0, 30):
        num = int(next(sys.stdin))
        c = semitones[num]
        string = string + " " + c
    yield(string)

for c in load():
    sys.stdout.write("{}\n".format(c))