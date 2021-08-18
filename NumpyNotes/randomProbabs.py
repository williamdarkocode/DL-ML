import math

def comp():
	deck = 52
	num_each = 4
	probab_sum = 0
	for i in range(2,10):
		probab_sum+= (num_each/deck) * ((deck-(4*i))/deck)
		print("card: {}, probability: {}".format(i,probab_sum))
	probab_sum+=math.pow(((4/52)*(4/52)),4)
	print("card: {}, probability: {}".format("J,K,Q",probab_sum))
	probab_sum+=((4/52)*(48/52))
	print("card: {}, probability: {}".format("A's (considered as 1)",probab_sum))
	return probab_sum

def indiv_probabs():
	deck = 52
	num_each = 4
	probab_sum = 0
	for i in range(10):
		probab_sum= (num_each/deck) * ((deck-(4*(i+1)))/deck)
		print("card: {}, probability: {}".format(i+1,probab_sum))
	probab_sum=math.pow(((4/52)*(4/52)),3)
	print("card: {}, probability: {}".format("J,K,Q",probab_sum))
	probab_sum=((4/52)*(48/52))
	print("card: {}, probability: {}".format("A's (considered as 1)",probab_sum))
	return probab_sum


def main():
	res = comp()
	print("The probablity of picking any card in one deck, being less than any card")
	print("Proof by higher power: ", res)
	# indiv_probabs()


if __name__ == '__main__':
	main()
