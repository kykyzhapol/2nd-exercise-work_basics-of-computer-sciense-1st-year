import math
mass = int(input())*0.453592
leg = int(input())*0.0254
print(math.ceil((mass/(leg**2))*100)/100)