'''
Note that this code is representing graph as 'map' of packages
with two sets of lists -> needed, used
I though of using an array of linked lists or multi-dimensional array to represent
index graph but realized searching for dependencies AND looking for packages dependant
on a stated package might be inefficient or require full map iteation.
'''
import package

class PackageGraph:

	def __init__(self):
		self.packages = {}

	def addPackage(name,dependencies):

		#check if package already there
		if package in self.packages:
			return False

		#make sure dependencies already exist
		for dependency in dependencies:
			if dependency not in self.packages:
				return False
		
		#iterate through dependencies and make connection to current package
		for dependency in dependencies:
			self.packages[dependencies].used_by.append(dependency)

		#if all is well, add package
		newPackage = Package(name,dependencies)
		self.packages[name] = newPackage

		return True

	def getPackage(package):
		
		#check if package is indexed
		return (package in self.packages)

	def removePackage(package):

		#check if other package depends on this
		if len(self.packages[package].used_by) > 0:
			return False

		#if not, update list of packages this depends on
		for p in self.packages[package].requires:
			tempPackage = self.packages[p]
			tempPackage.remove(p)

		#remove and return true
		del self.packages[package]

		return True



