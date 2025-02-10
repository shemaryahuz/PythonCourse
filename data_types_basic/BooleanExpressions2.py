is_true = False
is_false = True
a=is_false and (is_true or not is_false) and not (is_false and is_true)
print("a:",a)
age = 25
has_license = True
has_experience = False
is_eligible = False
b=age >= 18 and (has_license or has_experience) and not (is_eligible)
print("b:",b)
pi = 3.14159
count = 10
max_count = 15
is_greater_than_pi = pi > 3.0
is_in_range = count >= 0 and count <= max_count
c=is_greater_than_pi or is_in_range and not (count < max_count)
print("c:",c)
grade = "B"
Score = 90
score = 80
is_passing = grade == "A" or (grade == "B" and score >= 70)
is_excellent = grade == "A" and score >= 90
d=is_passing and not is_excellent
print("d:",d)
ae = 5
be = 3
ce = 2
condition1 = ae > be
condition2 = ce !=0
e=(condition1 or condition2) and (ae % ce == 0)
print("e:",e)
