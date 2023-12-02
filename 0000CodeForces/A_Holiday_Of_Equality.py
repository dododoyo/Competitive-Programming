input()
citizens_welfare = list(map(int,input().split()))
maximum_welfare = max(citizens_welfare);
minimum_charge = 0;
for each_welfare in citizens_welfare:
  minimum_charge += maximum_welfare-each_welfare;
print(minimum_charge)
