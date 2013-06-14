#A function to sort the incomming array by only the first dimension, but having the second dimension mirror the changes
def Sort(array):
    """Will sort a given array based on the first row of values and will mirror any changes in the next one or two rows.
    Only works with 2D and 3D arrays"""
    import numpy as np
    z = 0
    #Checks the shape of the array
    if np.shape(array)[0] == 2:
        #I wanted to use a while loop
        while z < array.size/2:#I divide by 2 because array.size gives us the number of elements in both rows, not just the first row
            for q in range(array.size/2 -1):
                #start = copy(array)
                #checks if the next number is smaller than the current number
                if array[0][q] > array[0][q+1]:
                    #swaps the two values
                    temp1 = array[0][q+1]
                    array[0][q+1] = array[0][q]
                    array[0][q] = temp1
                    #swaps the two values in the second row
                    temp2 = array[1][q+1]
                    array[1][q+1] = array[1][q]
                    array[1][q] = temp2
            z += 1
    if np.shape(array)[0] == 3:
        while z < array.size/3:
            for q in range(array.size/3 -1):
                #start = copy(array)
                #same thing as above, but now it swaps for three rows
                if array[0][q] > array[0][q+1]:
                    temp1 = np.copy(array[0][q+1])
                    array[0][q+1] = array[0][q]
                    array[0][q] = temp1
                    temp2 = np.copy(array[1][q+1])
                    array[1][q+1] = array[1][q]
                    array[1][q] = temp2
                    temp3 = np.copy(array[2][q+1])
                    array[2][q+1] = array[2][q]
                    array[2][q] = temp3
            z += 1
        #print start
    return array

def CA184(xv,rl,vmax):
    """Models the movement of traffic over one interval.
    Given 2D array xv, road length rl, and max velocity vmax, moves the cars according to the STCA rules without
    random slowdowns"""
    import numpy as np
    space = True
    xvcopy = np.copy(xv)#copying the initail array in order to not change it
    xvarr = Sort(xvcopy)
    
    #adding a third row of car labels(numbered 1-number of cars) to the array
    if np.shape(xvcopy)[0] < 3:
        car_num = np.arange(1,xvcopy[0].size + 1,1)
        xvarr = np.vstack((xvarr,car_num))
    
    #implementing the rules for each car
    g = np.zeros(xvarr[0].size)#making an array for the open spaces
    first = xvarr[0][0]#storing the initial position of the first car
    for i in range(xvarr[0].size):
        
        #tells the last car to measure number of empty spaces  until the first car
        if i == (xvarr[0].size -1):
            g[i] = first -(xvarr[0][i] -rl)#using first here because the first position will have changed
            #if the car will drove off the road, moves it back to the beginning
            if (xvarr[0][i] + xvarr[1][i]) > rl:
                xvarr[0][i] = xvarr[0][i] -rl
                
        #measuring empty spaces until next car
        else:
            g[i] = xvarr[0][i+1]-xvarr[0][i]
            
        #following the rules
        if g[i] == 0:
            space = False
        else:
            space = True
        if xvarr[1][i] >= g[i]:
            xvarr[1][i] = g[i]
        if xvarr[1][i]< g[i] and xvarr[1][i]<vmax:
            xvarr[1][i] += 1
        if g[i] + xvarr[1][i] > rl:
            xvarr[0][i] -= rl
        if space:
            xvarr[0][i] += xvarr[1][i]
    
    xvarr = Sort(xvarr)#resorting the array
    return xvarr

def STCA(xv,rl, vmax, prob = 0.1, doCruise = False):
    """Models the movement of traffic over one interval.
    Given 2D array xv, road length rl, and max velocity vmax, moves the cars according to the STCA rules. 
    Has optional variale prob which changes the probability of a random slow down. By default prob is set to 0.5"""
    #follows the same process as in the CA184 model, but now has a rendom slowdown rule
    import numpy as np
    space = True
    cruise = False
    xvcopy = np.copy(xv)
    xvarr = Sort(xvcopy)
    if np.shape(xvcopy)[0] < 3:
        car_num = np.arange(1,xvcopy[0].size + 1,1)
        xvarr = np.vstack((xvarr,car_num))
    g = np.zeros(xvarr[0].size)
    for i in range(xvarr[0].size):
        if xvarr[1][i] > vmax:
            xvarr[1][i] = vmax
        if i == (xvarr[0].size -1):
            g[i] = xvarr[0][0] -(xvarr[0][i] -rl)
            if (xvarr[0][i] + xvarr[1][i]) > rl:
                xvarr[0][i] = xvarr[0][i] -rl
        else:
            g[i] = xvarr[0][i+1]-xvarr[0][i]
        if g[i] == 0:
            space = False
        else:
            space = True
        if xvarr[1][i] >= g[i]:
            xvarr[1][i] = g[i]
        if xvarr[1][i]< g[i] and xvarr[1][i]<vmax:
            xvarr[1][i] += 1
        if xvarr[1][i] == vmax and doCruise:
            cruise = True
        else:
            cruise = False
        #checks for random slowdown
        if xvarr[1][i] > 0 and (np.random.rand(1) < prob):
            if not cruise:
                xvarr[1][i] -= 1
        if g[i] + xvarr[1][i] > rl:
            xvarr[0][i] -= rl
        if space:
            xvarr[0][i] += xvarr[1][i]
    xvarr = Sort(xvarr)         
    return xvarr

def ASEP(xv,rl, vmax):
    """Models the movement of traffic over one interval.
    Given 2D array xv, road length rl, and max velocity vmax, moves the cars according to the ASEP rules. 
    Moves cars one at a time instead of simultaneously"""
    #begins the same way as the STCA or CA184 models
    import numpy as np
    space = True
    xvcopy = np.copy(xv)
    xvarr = Sort(xvcopy)
    if np.shape(xvcopy)[0] < 3:
        car_num = np.arange(1,xvcopy[0].size + 1,1)
        xvarr = np.vstack((xvarr,car_num))
    size = xvarr[0].size
    g = np.zeros(size)
    #differs here
    randArr = np.random.permutation(size)#makes an array of random numbers(0-size) with no repetitions
    #print randArr
    #loops over the randArr to move the cars randomly
    for i in randArr:
        #follows the ASEP rules
        if xvarr[1][i] > vmax:
            xvarr[1][i] = vmax
            #checks for the last car and tells it to find empy spaces from first car
            #BUT does not move the car to the beginning if it goes over the road length
        if i == (size -1):
            g[i] = xvarr[0][0] -(xvarr[0][i] -rl)
        else:
            g[i] = xvarr[0][i+1]-xvarr[0][i]
        if g[i] == 0:
            space = False
        else:
            space = True
        if xvarr[1][i] >= g[i]:
            xvarr[1][i] = g[i]
        if xvarr[1][i]< g[i] and xvarr[1][i]<vmax:
            xvarr[1][i] += 1
        if g[i] + xvarr[1][i] > rl:
            xvarr[0][i] -= rl
        if space:
            xvarr[0][i] += xvarr[1][i]
    #moves any cars that have gone over the road length to the beginning
    loopNum = 0
    for q in xvarr[0]:
        if q > rl:
            xvarr[0][loopNum] -= rl
        loopNum += 1
    xvarr = np.copy(Sort(xvarr))
    return xvarr

def Conditions(cnumb, roadLength, vmax):
    """Creates an initial conditions array given the number of cars, the road lenght, and the max velocity"""
    import numpy as np
    a = np.array([np.zeros(cnumb), np.zeros(cnumb)])
    a[0] = np.random.randint(1,roadLength, size = cnumb)
    a[1] = np.random.randint(1,vmax, size = cnumb)
    conditions = Sort(a)
    return conditions

def Running(N,func_name, arr, rl, vmax, which_car = 1, prob = 0.1, doCruise = False):
    """Runs the function func_name, N times, given initial array arr, road length rl, and max velocity vmax. Has 
    optional variables which_car that tells Running which car to follow when collecting car position data, and prob
    which is used for the STCA model.
    Returns the final array, an array of currents, an array of velocities, an array of car positions, and an array of
    the density of cars."""
    
    #creating arrays the same size as the number of steps
    import numpy as np
    dens_arr = np.zeros(N)
    v_arr = np.zeros(N)
    cur_arr = np.zeros(N)
    cpos = np.zeros(N)
    new_arr = np.copy(arr)#making a copy of arr

    #runs the simulation N times
    for q in range(N):
        
        #checks which method you want to use
        if func_name == 'CA184':
            temp = CA184(new_arr, rl, vmax)
            new_arr = np.copy(temp)
            #loop that allows the cpos value to follow a specific car
            counter = 0 
            for i in new_arr[2]:
                if i == which_car:
                    cpos[q] = new_arr[0][counter]
                counter += 1
                
        if func_name == 'STCA':
            temp = STCA(new_arr, rl, vmax, prob, doCruise)
            new_arr = np.copy(temp)
            counter = 0
            for i in new_arr[2]:
                if i == which_car:
                    cpos[q] = new_arr[0][counter]
                counter += 1
                
        if func_name == 'ASEP':
            temp = np.copy(ASEP(new_arr, rl, vmax))
            new_arr = np.copy(temp)
            counter = 0
            for i in temp[2]:
                if i == which_car:
                    cpos[q] = temp[0][counter]
                counter += 1
                
        #calculating density, average velocity, and currrent for each step and filling in their respective arrays
        density = float(new_arr.shape[1])/float(rl)
        dens_arr[q] += density
        
        v_avg = float(sum(new_arr[1])/new_arr.shape[1])
        v_arr[q] += v_avg
        
        current = density*v_avg
        cur_arr[q] += current
        
    return new_arr,cur_arr,v_arr, cpos, dens_arr

