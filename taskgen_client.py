import time

print("Calling the taskgen service...")
file = open("task-pipe.txt", "w")
file.write("gen") # call the service by writing "gen"
file.close()

time.sleep(5) # wait for service to respond

filled_file = open("task-pipe.txt", "r")
tasks = filled_file.read()
print("Taskgen service returned: ")
print(tasks)
filled_file.close()