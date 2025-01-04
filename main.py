import numpy as np
lst = [0,1,2,3,4,5,6,7,8]
def calculate(lst):
    n, m = 3, 3
    if n*m != len(lst):
        ValueError: 'List must contain nine numbers.'
    else:
        arr = np.array(lst)
        res = arr.reshape(n,m)
        # print(res)

    calculations = {
                    'mean': [],
                    'variance': [],
                    'standard deviation': [],
                    'max': [],
                    'min': [],
                    'sum': []    
                    }

    calculations.update({
    "mean": [
        list(res.mean(axis=0)),  
        list(res.mean(axis=1)),
        res.mean()              
    ]
})
    calculations.update({
    "variance": [
        list(res.var(axis=0)),  
        list(res.var(axis=1)),
        res.var()              
    ]
})
    calculations.update({
    "standard deviation": [
        list(res.std(axis=0)),  
        list(res.std(axis=1)),
        res.std()              
    ]
})
    calculations.update({
    "max": [
        list(res.max(axis=0)),  
        list(res.max(axis=1)),
        res.max()              
    ]
})
    calculations.update({
    "min": [
        list(res.min(axis=0)),  
        list(res.min(axis=1)),
        res.min()              
    ]
})
    calculations.update({
    "sum": [
        list(res.sum(axis=0)),  
        list(res.sum(axis=1)),
        res.sum()              
    ]
})




    return calculations



