import sys

def Cat(filename):
	f = open(filename, "r")
	text = f.read()
	text = text.lower()
	words = text.split()
	word_count = {}
	list_of_words = []
	for word in words:
		word_count[word] = words.count(word)
	for tuples in word_count.items():
		list_of_words.append(tuples)
	print sorted(list_of_words, key = lambda x: x[1], reverse = True)
	f.close()

def main():
	Cat(sys.argv[1])
	
	
#standard boilerplate
if __name__ == "__main__":
	main()


