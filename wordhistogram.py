import sys
import string

# read file and words
fhand = open('text.txt')
counts = {}
words = fhand.read().split()

# create a dictionary
if len(words) == 0:
    fhand.close()
else:
    for word in words:
        translator = str.maketrans('','',string.punctuation)
        w = word.upper().translate(translator)
        if(len(w) > 0):
            counts[w] = counts.get(w, 0) + 1
    fhand.close()

# sort a dictionary reversely based on count of each word
if len(counts)!=0:
    lst = []
    for key, val in counts.items():
        newtup = (val, key)
        lst.append(newtup)
        lst = sorted(lst, reverse = True)

# count total number of words
total = 0
for cnt,label in lst:
	total += cnt

# produce a histogram
for cnt,label in lst:
    print(label.ljust(15),"\t[",sep='',end='')
    per = int(cnt)*100//total
    for i in range(0,per,5):
        print("*",sep='',end='')
    print("] ", per,"%",sep='')