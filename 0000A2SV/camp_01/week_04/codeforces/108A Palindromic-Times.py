def cutsom_str(num):
  if num < 10:return "0" + str(num)
  return str(num)
def next_palindrome(hour,minute):
  while True:
    minute += 1
    if minute == 60:minute,hour = 0, hour+1
    if hour == 24:minute,hour = 0,0
    str_hour, str_minute = cutsom_str(hour), cutsom_str(minute)
    if str_hour == str_minute[::-1]:
      return str_hour + ":" + str_minute

hour, minute = map(int,input().split(":"))
print(next_palindrome(hour,minute))