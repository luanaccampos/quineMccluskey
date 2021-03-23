class setCoverPd:
	def __init__(self, U, S):
		self.S = S
		self.pd = {}
		self.n = len(U)
		self.resposta = []

		k = len(S)
		for i in range(0, k):
			self.pd[i] = {}

		self.cover(0, frozenset(), k)
		self.answer(0, frozenset(), k)

	def cover(self, i, s, n):
		if len(s) == self.n:
			return 0

		if i == n:
			return 0x3f3f3f3f

		if self.pd[i].get(s) != None:
			return self.pd[i][s]

		aux = s.union(self.S[i])

		x = self.cover(i+1, s, n)
		y = 1 + self.cover(i+1, aux, n)

		self.pd[i][s] = min(x, y)

		return min(x, y)

	def answer(self, i, s, n):
		if i == n:
			return

		if i == n-1:
			self.resposta.append(self.S[i])
			return

		aux = s.union(self.S[i])

		a = b = 0x3f3f3f3f

		if self.pd[i+1].get(s) != None:
			a = self.pd[i+1][s]

		if self.pd[i+1].get(aux) != None:
			b = 1 + self.pd[i+1][aux]

		if a <= b:
			self.answer(i+1, s, n)
		else:
			self.resposta.append(self.S[i])
			self.answer(i+1, aux, n)

	def getResposta(self):
		return self.resposta