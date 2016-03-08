class Package:

	def __init__(self,name,dependencies):
		self.name = name

		#current packages dependencies
		self.requires = []

		#other packages that depend upon this package
		self.used_by = []

	def addDependency(self, dep):

		#check if dependency already was added
		if dep in self.requires:
			return False
		else:
			self.requires.append(dep)
			return True

	def addUsedBy(self, used):

		#check if package forward use-case was already aded
		if used in self.used_by:
			return False
		else:
			self.requires.append(used)
			return True