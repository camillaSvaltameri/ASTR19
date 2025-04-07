
def equation(x):
	result = x**3 + 8
	return result


def main():
	n = 9
	if equation(n) > 27:
		print("YAY!")
	print(equation(n))



if __name__ == "__main__":
	main()
