package main

import (
	"fmt"
	"log"
	"math/big"
	"net/http"
)

func main() {
	http.HandleFunc("/", fibonacciServer)
	http.ListenAndServe(":80", nil)
}

func fibonacci(n *big.Int) *big.Int {
	// Initialize two big ints with the first two numbers in the sequence.
	a := big.NewInt(0)
	b := big.NewInt(1)
	i := big.NewInt(0)

	for i.Cmp(n) < 1 {
		// Compute the next Fibonacci number, storing it in a.
		a.Add(a, b)
		// Swap a and b so that b is the next number in the sequence.
		a, b = b, a

		// bump num iterations
		i.Add(i, big.NewInt(1))
	}

	return a
}

func fibonacciServer(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()
	whichFibonacciNumber, present := query["which-fibonacci"]
	if !present || len(whichFibonacciNumber) == 0 {
		fmt.Println("which-fibonacci param not present")
	}

	i := new(big.Int)
	_, err := fmt.Sscan(whichFibonacciNumber[0], i)
	if err != nil {
		log.Println("error scanning value which-fibonacci:", err)
	}

	fibonacciNumber := fibonacci(i)
	fmt.Fprintf(w, "The %d fibonacci number is %d", i, fibonacciNumber)
}
