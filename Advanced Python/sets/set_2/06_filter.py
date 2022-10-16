# method 1 
def gtf (n):
    if n > 4:
        return True
    else:
        return False

m = [7, 5, 2, 9, 1, 3, 6, 4, 8]        

print(list(filter(gtf, m)))

# method 2 
gts = lambda p: p>6
print(list(filter(gts, m)))
