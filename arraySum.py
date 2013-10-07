def arraySum(i):
    sum = 0;
    for j in i:
        if isinstance(j, int):
            sum += j;
        if isinstance(j, list):
            sum += arraySum(j);
    return sum;

print arraySum([1, 2, 3, 4, 5]);
print arraySum([[1, 2, 3], 4, 5]);
