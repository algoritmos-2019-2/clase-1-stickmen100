print("Tablas de verdad")
X=[True,False]
Y=[True,False]
print("")
print("NOT")
print("X notX")
for m in X:
	print(str(m)+" "+str(not(m)))
print("")
print("")

print("AND")
print("X	Y	X y Y")
for m in X:
	for k in Y:
		print(str(m)+" "+(str(k))+" "+str(k and m))
print("")
print("")

print("OR")
print("X        Y       X o Y")
for m in X:
	for k in Y:
		print(str(m)+" "+(str(k))+" "+str(m or k))
