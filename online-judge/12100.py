#12/09/2019 dd/mm/yyyy

def checkList(job, listJobs):
    for j in listJobs:
        if int(j) > int(job):
            return False
    return True


cases = int(input())

listOutputs = []

for i in range(cases):
    nm = input()
    listNM = nm.split()
    lenJobs = int(listNM[0])
    posMyJob = int(listNM[1])
    jobs = input()
    listJobs = jobs.split()
    count = 0

    while True:
        if posMyJob == 0:
            job = listJobs.pop(0)
            check = checkList(job, listJobs)
            if not(check):
                listJobs.append(job)
                posMyJob = len(listJobs) - 1
            else:
                count += 1
                listOutputs.append(count)
                break
        else:
            job = listJobs.pop(0)
            check = checkList(job, listJobs)
            posMyJob -= 1
            if not(check):
                listJobs.append(job)
            else:
                count += 1
                

for output in listOutputs:
    print(str(output))
    