def walk(hours,distance):
 distance = 0 
  for i in range(hours):
    x = random.randint(1,2)
    q.put(x)
  print(q)
  for i in range(hours):
    q_get = q.get()
    if q_get == 1:
      distance += 1	
    elif q_get ==2:
      distance -= 1 
  print(distance)

  


import random
import queue 
q = queue.Queue()
distance = 0
walk(1,distance)
walk(4,distance)
walk(9,distance)
