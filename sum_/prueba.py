from itertools import product
import os
import time

def sumt(cadena, tam):

	loadBar = input('[?] Activate LoadBar? s/n: ')
	if loadBar == 's':
		endsW = input('   [?] Ends with: ')
		rund = int(input('   [?] Round: '))
	print('[+] Starting process.')
	tme = time.time()
	num = tam
	tot = len(cadena)**num
	caracteres = list(cadena)
	results = []
	for c in product(caracteres, repeat=tam):
	
		res = 0
		for i in range(num):
			if c[i] == '-':
				res -= i+1
			else:
				res += i+1
		results.append(res)
		if loadBar == 's':
			if str(len(results)).endswith(endsW):
				porc = round((len(results)/tot)*100, rund)
				print('   [+] {} / {}   \t| {}%'.format(len(results), tot, porc))
	tme = round(time.time() - tme, 1)
	print('[+] Action completed in {} seconds. Dumping results to a dictionary...'.format(tme))
	resDic = {}
	for i in results:
		try:
			resDic[i]+=1
		except:
			resDic[i]=1

	if input('[+] Completed, show dictionary? ({} items) s/n: '.format(len(resDic))) == 's':
		print('\n')
		for i in resDic:
			print('{} \t-->\t {}'.format(i, resDic[i]))
		print('\n\n')

	if input('[?] Save info in a .txt file? s/n: ') == 's':
		while True:
			name = input('   [+] Select a filename for the file: ')
			if name.endswith('.txt') == False:
				print("   [-] Filename must end in '.txt'.")
			else:
				break
		wn = open('{}'.format(name), 'w')
		wn.write('Log generated with ALS combinatorial Porgram...\n')
		wn.write('Num: {}\t\tPossibilities: {}\n\n'.format(num, 2**num))
		a = 0
		for i in resDic:
			a += 1
			wn.write('[{}]  {}\t\t-->\t{}.\n'.format(a, i, resDic[i]))

		print('[+] Task completed, saved on {}.'.format(name))

def main():
	if True:
		os.system('cls')
		print('[+] Combinatorial program \n[+] By ALS')
		num = int(input('[?] Num: '))
		if input('[?] The output will have {} items, do you want to continue? s/n: '.format(2**num)) == 's':
			sumt('-+', num)
		else:
			main()

	#except Exception as e:
	else:
		input('[-] Exception ocurred: {}.\nEnter to exit. '.format(e))


if __name__ == "__main__":
	main()
	