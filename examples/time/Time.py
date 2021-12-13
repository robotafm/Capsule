import time

print(time.time())

current_time = time.localtime()

print("Сейчас "+str(current_time.tm_hour)+" час(ов) "+str(current_time.tm_min)+" минут(а/ы) "+
      str(current_time.tm_mday)+"."+str(current_time.tm_mon)+"."+str(current_time.tm_year))