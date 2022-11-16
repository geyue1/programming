
def even(n:int):
    result = []
    if n >=30:
        i = 30
        while i<=n:
            if i % 2==0:
                result.append(i)
            i+=1
    return result


print(even(40))