import numpy
import matplotlib.pyplot

interval = [0,4]
num_of_iters = 1000
accuracy = 0.0001

def logisticmap(x,r):
    return x*r*(1-x)

start_point = numpy.random.rand()
fix,graph = matplotlib.pyplot.subplots()
fix.set_size_inches(20,13)

for r in numpy.arange(0,4+accuracy,accuracy): #to make closed interval
    trace = [start_point]
    for i in range(0,num_of_iters):
        trace.append(logisticmap(trace[i],r))
    
    graph.plot([r]*900,trace[101:], "g.", markersize=0.02)

graph.set(xlabel="r", ylabel="x", title="logistic map")
matplotlib.pyplot.show()