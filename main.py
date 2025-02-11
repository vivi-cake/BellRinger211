from datetime import datetime, date, time

current = datetime.now()

class_end = time(14, 19, 0) 

current_time = current.now()

duration = datetime.combine(current, class_end) - current


print("Time remaining until class ends:", duration)
