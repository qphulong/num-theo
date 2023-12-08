1) Summation over Divisor ( note bằng tiếng việt nha Sry :(()
Note: n=Mul(p_i^e^i) (i từ 1->r)
Tính các hàm:
	1. 1(n) = 1 
	2. I(n) = 1 if n=1; I(n) = 0 if n>1
	3. Mobius(n) = 0 if exists i >= 2 ; (-1)^r otherwise
Áp dụng:
	1. hàm tổng các ước nguyên dương của n (brute force suggested)
	2. Factorize integer : 4.1 có


2) Quadratic Residues and Square Root:


3) Chapter 5
Sàng nguyên tố eratosthenes - tìm tất cả các số nguyên tố <= n

4) Applications
	Side functions:
		1. Factorize interger: Brute force suggested
		2. Repeated Squaring: 3.4
	Diffie-Hellman
		1. Find Zp* generator: 11.1
		2. Discrete logarithms in Zp*: choose one of: 
			- 11.2.2
			- 11.2.4 (space-wise improvement of 11.2.2)
			- 11.2.3 + 12.2.4 (difficult)
		3. Diffie-Hellman problem: 11.3
			Sol: Given A, B, and g, find k
				x = log_g(A)
				k = B^x
	QR (quadratic residuosity)
		1. Legendre symbol: theorem 12.1 (i) + Repeated Squaring
		2. Jacobi symbol: 12.3
		3. Test if a's quadratic residuosity mod n: 12.4
			Sol: integer a, positive integer n
				if Jacobi(a, n) == -1 
					return false
				factors = factorize(n)
				for factor, order in factors
					if order odd and Legendre(a, factor) == -1 return false
				return true
		4. QR problem: Let n in the form pq (both are primes, p = q = 3 mod 4) and B = (-1)^b A^2 (A in Zn*, b in [0, 1])
			Given n and B, find b
			Other word: distinguis (Zn*)^2 from Ker Jn
			Sol: 
				# Don't need Jacobi check as it already in Ker Jn
				factors = factorize(n)
				for factor in factors
					if Legendre(a, factor) == -1 return false
				return true
			Note: 
				Factorize and Legendre may cost A LOT of time when p, q are big
				Factorize can be implement by binary search for this case as the number of factors is only 2
	RSA: 
		generate 2 big prime p, q, let n = pq. Choose e > 1, gcd(e, phi(n) = (p - 1)(q - 1)) = 1, tuple (n, e) is public key
		d = e^-1 mod phi(n) is private key
		Enscript: B = A^e
		Descript: A = B^d
		1. Generate random prime: 9.4
		2. Encoder, Decoder: use Repeated Squaring
		3. Hack: factorize n, calculate d, and Descript the mesage
			3.a. Calculate modular inverse: base on extended Euclidean algorithm
			
		
		

