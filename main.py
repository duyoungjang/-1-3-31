days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
num = ['first', 'second', 'third', 'fourth', 'fifth','sixth' ,'seventh']

def is_on_list(day):
  if day in days:
    print("Is {} on 'days' list?".format(day), day in days)


def get_x(day):
  day_num = days.index(day)
  print("The {} item in 'days' is: {}".format(
    num[day_num - 1] , day
  ))
  
def add_x(day):
  days.append(day)
  print(days)

def remove_x(day):
  days.remove(day)
  print(days)


is_on_list('Wed')
get_x('Thu')
add_x('Sat')
remove_x('Mon')