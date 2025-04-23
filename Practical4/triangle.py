n=0
b=1
while  n <= 9:    # Cycle ten times
    b=n+b         # Add the current value of n to b and update b
                  # This accumulates the sum of b with the current loop index n
    print(n+b)
    n=n+1         # Increase n by 1 to move to the next loop iteration
    