def sln(n):
   
    if n <= 1:
        return -1
  
    def only_odd_digits(num):
        return all(int(digit) % 2 == 1 for digit in str(num))
    
    start = n - 1
    if start % 2 == 0:
        start -= 1
    
    
    for num in range(start, 0, -2):
        if only_odd_digits(num):
            return num
    
    return -1

def sln_optimized(n):
   
    if n <= 1:
        return -1
    
    prev = n - 1
    
   
    if all(int(digit) % 2 == 1 for digit in str(prev)):
        return prev
    
   
    digits = list(str(prev))
    length = len(digits)
    
   
    found_even = False
    for i in range(length):
        if int(digits[i]) % 2 == 0: 
            found_even = True
            
           
            if int(digits[i]) > 1:
                digits[i] = str(int(digits[i]) - 1)
            else: 
                j = i - 1
                while j >= 0:
                    if int(digits[j]) > 1:
                        digits[j] = str(int(digits[j]) - 2 if int(digits[j]) % 2 == 1 else int(digits[j]) - 1)
                        break
                    else:
                        digits[j] = '9'
                        j -= 1
                
                if j < 0:  
                    return int('9' * (length - 1)) if length > 1 else -1
                
                digits[i] = '9'
            
            
            for k in range(i + 1, length):
                digits[k] = '9'
            
            break
    

    if not found_even:
        return prev
    

    result = int(''.join(digits))
    

    if all(int(digit) % 2 == 1 for digit in str(result)):
        return result
    

    return sln(result)

def main():
    
    n = int(input())
    result = sln_optimized(n)
    if result == -1:
        print("0")
    else:
        print(result)

if __name__ == "__main__":
    main()