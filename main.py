from tqdm import trange
from math import ceil

def fib(amount):
	a, b = 0,1
	amt = 0
	for i in trange(amount):
		if a == 1:
			amt += 1
		if not (a == 1 and amt == 2):
			yield a
		a, b = b, a+b

def fibl(amount):
	return list(fib(amount))

def main():
	i = input('How many fibonacci numbers do you want? Integers only')
	i = int(i)
	f = fibl(i)
	if len(f) > 100:
		s = 0
		for i in range(ceil(len(f)/100)):
			print(f[s:s+100])
			input('Continue?')
			s += 100
	else:
		print(f)
			

if __name__ == '__main__':
	main()
