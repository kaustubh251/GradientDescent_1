import numpy as npy
import matplotlib as mplot
file = open("ex1data1.txt","rt")
data = file.read()
data1 = data.split()
N = len(data1)
x = []
y = []
for element in data1:
    ele = element.split(',')
    x.append(float(ele[0]))
    y.append(float(ele[1]))
#Calculating hypothesis
def polynomial(theta, xi):
    count = 0
    h = 0
    for element in theta:
        h += element*npy.power(xi, count)
        count += 1
    #h = theta[0] + theta[1]*xi
    return h
#Calculating cost function
def costCalculator(theta, x, y):
    m = len(x)
    count = 0
    h = 0
    cost = 0
    for element in x:
        h = polynomial(theta, element)
        cost += (h - y[count])*(h - y[count])
        count += 1
    cost = cost/(2*m)
    return cost
#Applying gradient descent algorithm
def gradDescent(theta, x, y, alpha):
    m = len(x)
    delta = 10**(-12)
    theta2 = theta
    tolerance = 10**(-6)
    maxIter = 1500
    count2 = 0
    n = len(theta)
    while count2<maxIter:
        count = 0
        while count<n:
            theta1 = theta
            #Piece below is to be used in further versions
            #thetaMdelta = theta1[count] - delta
            #theta1[count] = thetaMdelta
            #cost1 = costCalculator(theta1, x, y)
            #thetaPdelta = theta1[count] + 2*delta
            #theta1[count] = thetaPdelta
            #cost2 = costCalculator(theta1, x, y)
            #theta2[count] = theta[count] - alpha*(cost2-cost1/(2*delta))
            #Piece ends here
            derCostFun = 0
            if count==0:
                count3 = 0
                for ele in x:
                    derCostFun += (polynomial(theta1, ele) - y[count3])
                    count3+=1
                derCostFun = derCostFun/m
            else:
                count3 = 0
                for ele in x:
                    derCostFun += (polynomial(theta1, ele) - y[count3])*ele
                    count3+=1
                derCostFun = derCostFun/m
            theta2[count] = theta[count] - alpha*derCostFun
            count += 1
        theta = theta2
        count2 += 1
    return theta
print("Insert the number of parameters. Please enter two parameters as straight line is a good fit for given data.")
paramsNumber = int(input())
theta = []
i = 0
print("Insert the parameters one by one each on newline")
for i in range(paramsNumber):
    theta.append(float(input()))
print("Insert learning rate")    
alpha = float(input())
thetaFinal = gradDescent(theta, x, y, alpha)
print("The optimized parameters are:")
print(thetaFinal)
print("Insert x for which you want f_x")
Xi = float(input())
prediction = polynomial(thetaFinal, Xi)
print("The predicted f_x is:")
print(prediction)

