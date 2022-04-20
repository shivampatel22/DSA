def activitySelection(s, f, n):
    """accepts arrays-start times and finish times of activities a1,a2,a3....an
        assume that activites are sorted monotonically increasing by finish times"""
    sol = [(s[0], f[0])]
    currentActivity = 1
    while currentActivity < n:
        if isCompatible(sol[-1][1], s[currentActivity]):
            sol.append((s[currentActivity], f[currentActivity]))
        currentActivity += 1
    return sol

def isCompatible(recentActivityFinish, currentActivityStart):
    return currentActivityStart >= recentActivityFinish 

if __name__ == '__main__':
    s = [1,3,0,5,3,5,6,8,8,2,12]
    f = [4,5,6,7,9,9,10,11,12,14,16]
    print(activitySelection(s, f, 11))
    #time - O(n) if f is sorted
    #     - O(nlogn) if f is not sorted
