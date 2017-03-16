import sys

def load():
	while(1):
		num_events = int(next(sys.stdin))
		if num_events != 0:
			events = next(sys.stdin).split()
			events = [int(e) for e in events]
			yield(events)
		else:
			break

case = 1
for events in load():
	pos = 0 
	neg = 0
	for e in events:
		if e == 0:
			neg = neg + 1
		else:
			pos = pos + 1
	sys.stdout.write("Case {}: {}\n".format(case, pos-neg))
	case = case + 1