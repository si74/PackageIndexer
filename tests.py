import package
from packageGraph import PackageGraph

#one-off file to quickly test the package node class and package class
if __name__ == "__main__":

	#instantiate packageGraph
	graph = PackageGraph()

	assert(graph.numPackages() == 0), "empty graph should be created"

	assert(graph.addPackage('monkey','banana') == False), "package whose dependency doesn't exist should not have been added"

	assert(graph.addPackage('banana') == True), "should have been able to add this package"
	
	assert(graph.numPackages() == 1), "1 package should have been added"

	assert(graph.addPackage('monkey',['banana']) == True), "dependencies in place, why isn't this working"

	assert(graph.numPackages() == 2), "There should be 2 packages"

	assert(graph.addPackage('banana') == False), "Can't add same package twice"

	assert(len(graph.packages['banana'].used_by) == 1), "banana used by 1 other package"

	assert(len(graph.packages['monkey'].requires) == 1), "package just being used by 1 more package"

	#these packages should be found
	assert(graph.getPackage('banana') == True), "this package should exist"

	assert(graph.getPackage('monkey') == True), "this package should exist"

	assert(graph.removePackage('banana') == False), "Shouldn't be possible without removing monkey"

	assert(graph.removePackage('monkey') == True), "Should be possible"

	assert(len(graph.packages['banana'].used_by) == 0), "now used by nothing"

	assert(graph.addPackage('banana') == False), 'cant add duplicate package'

	assert(graph.addPackage('monkey',['banana']) == True), "dependencies in place, why isn't this working"

	assert(graph.addPackage('bonobo',['banana']) == True), "dependencies in place, why isn't this working"

	assert(len(graph.packages['banana'].used_by) == 2), "now used by 2 things"

	#instantiate package and test