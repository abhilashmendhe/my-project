def fibonnaci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    a,b = 0, 1
    
    for _ in range(2, n):
        sum = a + b
        a = b
        b = sum 
    
    return b

if __name__ == "__main__":

    print(f"1 -> {fibonnaci(1)}")
    print(f"2 -> {fibonnaci(2)}")
    print(f"3 -> {fibonnaci(3)}")
    print(f"4 -> {fibonnaci(4)}")
    print(f"5 -> {fibonnaci(5)}")
