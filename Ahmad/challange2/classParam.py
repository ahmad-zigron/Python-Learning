class ClassAbc:
	name="This Is a Class Variable" 
	def __init__(self,  name):
		self.n = name 
print ClassAbc.name 
ClassAbc.name= "Class Varible Changed Here"
print ClassAbc.name
obj = ClassAbc("This Is an Instance Variable")    
print obj.name      

