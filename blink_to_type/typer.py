# typing.py
import time, sys

# Use in place of print() function
def typingPrint(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
