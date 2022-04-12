# # using time.time() functions
import time
# initial=time.time()
# k=1
# while(k<145):
#     print("this is the time for time checkup")
#     k+=1
# print ("while loop ran in",time.time()-initial,"seconds.")


# time.localtime() function (unstructured tuple form)
# local_time=time.localtime()
# print (local_time)


# time.asctime(time.localtime()) function (structured readable form)
# Time=time.asctime(time.localtime(time.time()))
# print(Time)


# time.sleep() function.
k=1
while(k<5):
    time.sleep(3)
    print("this is the time for time checkup")
    k+=1

print ("sleeping while loop")
