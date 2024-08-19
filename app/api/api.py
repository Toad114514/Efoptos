def install(name, package):
	file = open('usr/pkg/ln.list', 'w')
	name2 = file.read()
	name2.append('name')
	file.write(name2)
	file2 = open('usr/pkg/lpkg.list', 'w')
	pkg2 = file.read()
	pkg2.append(package)
	file.write(pkg2)
	pass