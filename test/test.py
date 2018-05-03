from russellcapping import RussellCapping

test = RussellCapping()
data, mc, weigh = test.russell_capping()
for z in data:
    print(z, '\t' + str(data[z]), sep='\n')
print(mc, weigh)