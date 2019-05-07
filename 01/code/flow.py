# flow

def flow(x0, t0, iteration, dt):
    xs = np.array([x0])
    ts = np.array([t0])
    
    for i in range(iteration):
        xi = xs[i]
        ti = ts[i]
        xs = np.append(xs, xi + logistic(xi, a)*dt)
        ts = np.append(ts, ti + dt)
    return xs, ts