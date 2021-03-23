class setCoverGreedy:
	def __init__(self, U, S):
		self.resposta = []

		I = set()
		n = 0
		k = len(U)

		while(n != k):
			aux = {}
			menor = k+1

			for s in S:
				b = len(s - I)
				if b != 0:
					a = len(s) / b
					if a < menor:
						menor = a
						aux = s

			self.resposta.append(aux)
			I = I.union(aux)
			n = len(I)

	def getResposta(self):
		return self.resposta