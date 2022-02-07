def find_min_coins(v, arr):
    res = []
    i = 0 
    arr.sort(reverse=True)
    while i < len(arr) and v > 0 :
        if arr[i] <= v :
            x = v//arr[i]
            temp = [arr[i]]*x
            res = res + temp
            v = v%arr[i]
        i+=1
    return res        
