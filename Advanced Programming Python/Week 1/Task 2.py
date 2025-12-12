salaries = []
salaries.extend(map(int, input().split()))

print(max(salaries) - min(salaries))