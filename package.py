class Package:

	def __init__(self,name):
		self.name = name

		#current packages dependencies
		self.requires = []

		#other packages that depend upon this package
		self.used_by = []

	def addDependencies(self, dependencies):

		for dependency in dependencies: 

			#check if dependency already was added
			if dependency in self.requires: return False
			else: self.requires.append(dependency)
		
		return True

	def addUsedBy(self, used):

		#check if package forward use-case was already aded
		if used in self.used_by:
			return False
		else:
			self.requires.append(used)
			return True