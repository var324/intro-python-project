import matplotlib.pyplot as plt
import numpy as np

def main(x,y,f):
    print(" The square is 8 units sided.")
    print(" The circle is radiated at 4 units.")
    print( " side of square = 2 x radius of the circle ")
    print (" x-y is the range, and f is the frequency of range of x-y, main(x,y,f)")
    for n in range(x,y+1,f):
        pi_value = 4 * (pi(n)/n)
        print(pi_value,n)




def pi(n):
    #generate random numbers, make a list of them and plot them 
    x_r = np.random.uniform(-4, 4, n) 
    y_r = np.random.uniform(-4, 4, n)
    
    x = np.round(x_r,2)
    y = np.round(y_r,2)
    
    circle = []
    square = []
    
    #figure out if the random numbers x,y together are within the circle or the square
    for i in range(n):
        r_calc = np.sqrt(x[i]**2 + y[i]**2)
        r = np.round(r_calc,2)
        if r<=4:
            circle.append(r)
        else:
            square.append(r)
    # making a plot area 
    plt.figure(figsize=(6,6))
    plt.axhline(0, color='black', linewidth=1) 
    plt.axvline(0, color='black', linewidth=1)
    
    plt.xticks(np.arange(-6, 6, 1))
    plt.yticks(np.arange(-6, 6, 1))
    plt.grid(True, which='both', linestyle='-', linewidth=0.5)
    
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    
    # making a square, and plotting it
    square_x = [4, -4, -4, 4, 4]
    square_y = [4, 4, -4, -4, 4]
    plt.plot(square_x, square_y, color='blue', linewidth=2)
    
    #making a circle, and plotting it
    circle = plt.Circle((0, 0), 4, color='red', fill=False, linewidth=2)
    plt.gca().add_patch(circle)
            
    #final touche' ( labels, plot show ) 
    plt.scatter(x, y, color='red', label='Random points')
    plt.xlabel("X-axis (units)")
    plt.ylabel("Y-axis (units)")
    plt.title("Pi")
    plt.axis('equal')
    plt.show()

    return len(circle)
