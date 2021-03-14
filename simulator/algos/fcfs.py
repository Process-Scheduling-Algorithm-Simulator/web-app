def getCompletionTime(n,arrivalTime,testbt,completionTime,startTime,length):
    arrivalTime.sort()
    time = arrivalTime[0][0]
    for i in range(n):
        index = arrivalTime[i][1]
        if arrivalTime[i][0] > time:
            time = arrivalTime[i][0] + testbt[index]
            startTime.append([index,arrivalTime[i][0]])
            length.append([index,testbt[index]])
        else:
            startTime.append([index,time])
            time += testbt[index]
            length.append([index,testbt[index]])
        completionTime[index] = time
 
 
def getTurnAroundTime(n,turnAroundTime,completionTime,testat):
    for i in range(n):
        turnAroundTime[i] = completionTime[i] - testat[i]


def getWaitingTime(n,waitingTime,turnAroundTime,burstTime):
    for i in range(n):
        waitingTime[i] = turnAroundTime[i] - burstTime[i][0]


def fcfs(processName, arrivalTime,testat, burstTime, testbt, completionTime, turnAroundTime, waitingTime, priority) :
    startTime = []
    length = []
    getCompletionTime(n,arrivalTime,testbt,completionTime,startTime,length)
    getTurnAroundTime(n,turnAroundTime,completionTime,testat)
    getWaitingTime(n,waitingTime,turnAroundTime,burstTime)