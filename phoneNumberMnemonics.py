def phoneNumberMnemonics(phoneNumber):
	currentMnemonic = ['0'] * len(phoneNumber)
	mnomonicsFound = []
	
	helper(0, phoneNumber, currentMnemonic, mnomonicsFound)
	return mnomonicsFound

def helper(idx, phoneNumber, currentMnemonic, mnomonicsFound):
	if idx == len(phoneNumber): # base case
		mnemonic = ''.join(currentMnemonic) # O(n)
		mnomonicsFound.append(mnemonic) 
	else: 
		digit = phoneNumber[idx]
		letters = mapping[digit]
		for letter in letters:
			currentMnemonic[idx] = letter
			helper(idx + 1, phoneNumber, currentMnemonic, mnomonicsFound)

mapping = {	
	'0':['0'],
	'1':['1'],
	'2':['a', 'b', 'c'],
	'3':['d', 'e', 'f'],
	'4':['g', 'h', 'i'],
	'5':['j', 'k', 'l'],
	'6':['m', 'n', 'o'],
	'7':['p', 'q', 'r', 's'],
	'8':['t', 'u', 'v'],
	'9':['w', 'x', 'y', 'z'],
}