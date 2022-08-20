list = 1, 2, 3, 2, 5, 6, 0, 1, 2, 6, 3 #can be replaced with any list including words/letters as long as its in the same format
print("Mode of List A is % s" % (max(set(list), key = list.count)))
input('press enter to exit')
