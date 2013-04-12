import code

def test_sleep_in():
	result = code.sleep_in(False, True)
	assert (result == True)

def test_monkey_trouble():
	result = code.monkey_trouble(True, True)
	assert result == True
	result2 = code.monkey_trouble(False, True)
	assert result2 == False
	result3 = code.monkey_trouble(False, False)
	assert result3 == True
	
def test_sum_double():
	x = code.sum_double(4, 5)
	assert (x == 4+5)
	y = code.sum_double(3, 3)
	assert (y == 6*2)