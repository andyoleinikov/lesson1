def get_summ(one, two, delimeter=' '):
	return str(one).upper()+str(delimeter)+str(two).upper()
one = input('input first ')
two = input('input second ')
delimeter = input('input delimeter ')
if delimeter:
	print(get_summ(one,two, delimeter))
else:
	print(get_summ(one,two))