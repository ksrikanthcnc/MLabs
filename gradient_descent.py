####################################################################################
## PROBLEM1: Gradient Descent
## Gradient descent is a popular optimization technique to solve many
## machine learning problems. In this case, we will explore the gradient
## descent algorithm to fit a line for the given set of 2-D points.
## ref: https://tinyurl.com/yc4jbjzs
## ref: https://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/
##
##
## input: directory of faces in ./data/1_points.csv/
## function for reading points is provided
##
##
## your task: fill the following functions:
## evaluate_cost
## evaluate_gradient
## udpate_params
## NOTE: do NOT change values of 'init_params' and 'max_iterations' in optimizer
##
##
## output: cost after convergence (rmse, lower the better)
##
##
## NOTE: all required modules are imported. DO NOT import new modules.
## NOTE: references are given intline
## tested on Ubuntu14.04, 22Oct2017, Abhilash Srikantha
####################################################################################

import numpy as np
import matplotlib.pyplot as plt

def load_data(fname):
    points = np.loadtxt(fname, delimiter=',')
    y_ = points[:,1]
    # append '1' to account for the intercept
    x_ = np.ones([len(y_),2])
    x_[:,0] = points[:,0]
    # display plot
    plt.plot(x_[:,0], y_, 'ro')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    #plt.show()
    print('data loaded. x:{} y:{}'.format(x_.shape, y_.shape))
    return x_, y_

def evaluate_cost(x_,y_,params):
    pass

def evaluate_gradient(x_,y_,params):
    pass

def update_params(old_params, grad, alpha):
    pass

# initialize the optimizer
optimizer = {'init_params':np.array([4.5,2.0]) ,
             'max_iterations':10000,
             'alpha':0.00001,
             'eps':0.0000001,
             'inf':1e10}

# load data
x_, y_ = load_data("./data/1_points.csv")

try:
    # gradient descent
    params = optimizer['init_params']
    old_cost = 1e10
    for iter_ in range(optimizer['max_iterations']):
        # evaluate cost and gradient
        cost = evaluate_cost(x_,y_,params)
        grad = evaluate_gradient(x_,y_,params)
        # display
        if(iter_ % 10 == 0):
            print('iter: {} cost: {} params: {}'.format(iter_, cost, params))
        # check convergence
        if(abs(old_cost - cost) < optimizer['eps']):
            break
        # udpate parameters
        params = update_params(params,grad,optimizer['alpha'])
        old_cost = cost
except:
    cost = opts['inf']

# final output
print('SOLUTION cost at convergence: {} (lower the better)'.format(cost))
