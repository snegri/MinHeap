import MinHeap.py

heapy = Heap()
heapy.printMenu()
a = raw_input(">>")
while a != "e":
	if a[0] == "i":
		l = a.split()
		heapy.insert(int(l[1]))
	elif a == "s":
		heapy.show()
	elif a == "p":
		print heapy.poll()
	elif a == "peek":
		print heapy.peek()
	elif a == "e":
		break
	heapy.printMenu()
	a = raw_input(">>")
print "Heap destroyed...."
exit()
