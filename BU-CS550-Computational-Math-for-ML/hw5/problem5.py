#recieved heavy help from a friend who codes in python
#sets values
EX4 = 2
EX2 = 1
EY2 = 1 
EY  = 0 

E_X2Y    = EX2 * EY           
E_X4Y2   = EX4 * EY2   

var_X2Y  = E_X4Y2 - E_X2Y**2

print("Var(X^2 * Y) = E(X^4*Y^2) - (E(X^2*Y))^2")
print(f"E(X^2*Y)  = E(X^2) * E(Y)  = {EX2} * {EY} = {E_X2Y}")
print(f"E(X^4*Y^2) = E(X^4) * E(Y^2) = {EX4} * {EY2} = {E_X4Y2}")
print(f"Var(X^2*Y) = {E_X4Y2} - {E_X2Y}^2 = {var_X2Y}")