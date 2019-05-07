# approx

def approx(x_min, x_max, iteration):
    x1 = x_min
    x2 = x_max
    x3s = np.array([x2])
    
    for i in range(iteration):
        x3 = (x1 + x2) / 2
        
        y1s = np.sign(f(x1, r))
        y2s = np.sign(f(x2, r))
        y3s = np.sign(f(x3, r))
        
        if y1s * y3s < 0:
            x2 = x3
        elif y2s * y3s < 0:
            x1 = x3
        else:
            break
        
        x3s = np.append(x3s, x3)
    return (x1 + x2) / 2