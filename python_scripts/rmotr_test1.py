def double_down(num, times_doubled):
    count = 1
    tally = num
    
    while count < times_doubled:
        print(count)
        print(tally)
        count = count + 1
        tally = num * tally
        
        
    return tally
        
        
    
x = double_down(2, 9)
print(x)