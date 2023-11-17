from sympy import *

def df(f,x):
    ''' Derivative of a given function f(x)
    
    Parameters
    ----------------
    f: function
        Function f(x) for which f'(x) is to be found.
    x: variable
        Variable of differentiation
    
    Returns
    ----------------
    function
        Function f'(x) for the given f(x)
    '''
    return diff(f,x)
def newton(f,x0:int,epsilon,max_iter:int):
    '''Approximate solution of f(x)=0 by Newton Raphson Method.
    
    Parameters
    ----------------
    f : function
        Function for which we are trying to approximate the solution at f(x)=0
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations
    
    Returns
    ----------------
    integer
        Solution for f(x) = 0 as obtained by the Newton Raphson Method
    '''
    xn =  x0
    ddx = df(f,x)
    for n in range(0, max_iter):
        fxn = f.subs(x, xn)
        if abs(fxn) < epsilon:
            print("Solution found after ", n, "iterations.")
            return xn
        dfxn = ddx.subs(x,xn)
        if dfxn == 0:
            print("Zero Derivative, no solution found.")
            return None
        xn = xn - fxn/dfxn
    print("Maximum Iterations exceeded. No solutions found.")
    return None

x = symbols('x')
f=0
degree = int(input("Enter the degree of the function: "))
for n in range(0, degree+1):
    c = float(input("Enter the coefficients: "))
    f = f + c*x**(degree-n)
print(f, " is the expression")
prec = int(input("Enter the precision required: "))
decPrecision = prec
prec = 10**(0-prec)
sol = newton(f,1,prec,10)
print("The solution according to Newton Raphson's approximation is\nx = ", round(sol, decPrecision))