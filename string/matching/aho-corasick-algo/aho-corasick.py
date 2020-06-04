class Trie:
	class Node :
		def __init__(self,val):
			self.val = val
			self.d = {}
			
	def __init__(self):
		self.root = self.Node("root")	
		
	def ins(self,s,no):
		cur = self.root
		prev = None
		cnt = 0
		for x in s:
			cnt+=1
			if x not in cur.d: 
				cur.d[x] = self.Node(x)
			if prev == None : 
				prev = self.root
			else : 
				prev = prev.d[x]
			cur = cur.d[x]
			cur.d["BACK"] = prev

		if no != None : 
			if "END" not in cur.d:
				cur.d["END"] = []
			cur.d["END"].append(no)
		
	
	def insert(self,s,no):
		for i in range(len(s)-1,0,-1):
			self.ins(s[i:],None)
		self.ins(s,no)
		
	def search(self,s):
		l = []
		cur = self.root
		i = 0
		while i <len(s):
			x = s[i]
			if x in cur.d : 
				cur = cur.d[x]
				i+=1
			else : 
				if "BACK" in cur.d : cur = cur.d["BACK"]
				else: 
					cur = self.root
					i+=1  
			if "END" in cur.d :
				l.append((i,cur.d["END"]))
		return l
		
					
	def p(self,node):
		if node == None : return 
		print(node.val,node.d.keys())
		for x in node.d : 
			if x != None and x!="END" and x!="BACK" and node.d[x]!=self.root : self.p(node.d[x])
			else : print(None)
			
def findSubstring(s, words):
	if len(s) == 0 or len(words) == 0 : return []
	
	trie = Trie()
	for i in range(len(words)):trie.insert(words[i],i)
	l = trie.search(s)
	# print(l)
	return l

st = "abcoopabcootyuplyuuuuuuuupgupsup"
words = ["abc","yup","uup","sup"]
res = findSubstring(st,words)
print(st)
print(res)


