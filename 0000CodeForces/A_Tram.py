n = int(input())
current_passengers = max_passengers =0
for i in range(n):
    leave_n_enter = list(map(int,input().split()))
    current_passengers += leave_n_enter[1]-leave_n_enter[0]
    max_passengers = max(max_passengers,current_passengers)
print(max_passengers)