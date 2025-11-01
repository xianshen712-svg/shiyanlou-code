for a in range(100):
	a=a+1
	if a<10 and a%7 == 0:
		continue
	elif a>9:
		if a%10 == 7:
			continue
		elif a//10 == 7:
			continue
		elif a%7 == 0:
			continue
		else:
			print("{}\n".format(a))
	else:
		print("{}\n".format(a))
