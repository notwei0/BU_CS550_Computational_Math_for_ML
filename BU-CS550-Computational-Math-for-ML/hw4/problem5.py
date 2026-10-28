import numpy as np

#expanding along row 2
#outside help from a tutor who helped me with the problems by hand and helped me translate it into code
print("expanding along row 2:")
print("  = -(-2)*|4, 0; -8, 0| + (7)*|-3, 0; 5, 0| - (6)*|-3, 4; 5, -8|")
print("  = 2*(4*0 - 0*(-8)) - 7*((-3)*0 - 0*5) - 6*((-3)*(-8) - 4*5)")
print("  = 2*(0) - 7*(0) - 6*(24 - 20)")
print("  = 0 - 0 - 24 = -24")
 
# expanding along row 3
print("expanding along row 3:")
print("  = (5)*|4, 0; 7, 6| - (-8)*|-3, 0; -2, 6| + (0)*(...)")
print("  = 5*(4*6 - 0*7) + 8*((-3)*6 - 0*(-2)) + 0")
print("  = 5*(24) + 8*(-18)")
print("  = 120 - 144 = -24")
 
#expanding along column 1
print("expanding along column 1:")
print("  = (-3)*|7, 6; -8, 0| - (-2)*|4, 0; -8, 0| + (5)*|4, 0; 7, 6|")
print("  = -3*(7*0 - 6*(-8)) + 2*(4*0 - 0*(-8)) + 5*(4*6 - 0*7)")
print("  = -3*(48) + 2*(0) + 5*(24)")
print("  = -144 + 0 + 120 = -24")
 
# d) expanding along column 2
print("expanding along column 2:")
print("  = -(4)*|-2, 6; 5, 0| + (7)*|-3, 0; 5, 0| - (-8)*|-3, 0; -2, 6|")
print("  = -4*((-2)*0 - 6*5) + 7*((-3)*0 - 0*5) + 8*((-3)*6 - 0*(-2))")
print("  = -4*(-30) + 7*(0) + 8*(-18)")
print("  = 120 + 0 - 144 = -24")

A = np.array([[-3,  4, 0],
              [-2,  7, 6],
              [ 5, -8, 0]])

print(f"det(A) = {np.linalg.det(A):.4f}")
