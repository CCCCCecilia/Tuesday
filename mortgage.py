
P = 5 * 10**6
print(P)
r = 0.05
r = r / 12
n = 20 * 12 
print(n)
A = r*P*((1+r)**n)/(((1+r)**n)-1)
print(A)
month = 1
Outstanding = P
# outstanding is changing, so as principal and interest.
print('month \t Instalment \t Interest \t Principal \t Outstanding')
Interest_amount = 0 

while month <= 240:
    Interest = Outstanding * r
    Principal = A - Interest
    Outstanding = Outstanding - Principal
    row = '{0:04d} \t {1:.2f} \t {2:.2f} \t {3:.2f} \t {4:.2f}'.format(month, A, Interest, Principal, Outstanding)
    print(row)
    month = month+1
    Interest_amount = Interest + Interest_amount

print(Interest_amount)







