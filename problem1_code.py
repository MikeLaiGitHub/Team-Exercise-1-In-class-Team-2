

def main():
	# Example function calls:
	print(determine_primes(11))  # Output: ([2, 3, 5, 7, 11], 2)
	print(determine_primes(22))  # Output: ([2, 3, 5, 7, 11, 13, 17, 19], 2)


# 	if not isinstance(n, int) or n <= 0:
# 		raise Exception("Input must be a positive integer.")

# 	# Step 1: Create an initial list of all integers in the range
# 	numbers = [True] * (n + 1)  # Using a boolean list to mark primes (True) and non-primes (False)
# 	primes = []  # List to store prime numbers

# 	# Step 2: Let p initially equal 2, the smallest prime number
# 	p = 2

# 	# Step 3: Enumerate through the multiples of p in increments of p, marking the multiples in the list
# 	while p * p <= n:
# 		if numbers[p]:  # If p is marked as prime
# 			for i in range(p * p, n + 1, p):  # Mark all multiples of p as non-prime
# 				numbers[i] = False
# 		p += 1

# 	# Step 5: Collect prime numbers from the list
# 	for i in range(2, n + 1):
# 		if numbers[i]:
# 			primes.append(i)

# 	return primes, p - 1  # p-1 represents the number of times the algorithm traversed the initial list of integers
def determine_primes(n: int) -> tuple:
    if not isinstance(n, int) or n<0:
        raise Exception("Input must be an positive integer.")
    
    # Initialize the list of boolean values, where True means "is a prime"
    primes = [True for i in range(n + 1)]
    p = 2
    count = 0

    while p * p <= n:# we start with p*p as p is already 2 and we want p to be 3. 
        # If primes[p] is not changed, then it is a prime
        if primes[p] == True:
            count += 1 
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
        # Increment the count as we traverse the list again

    # Forming the list of prime numbers
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]

    return prime_numbers, count

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
