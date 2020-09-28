x = float(input('Digite o valor em metros que deseja converter para cm e mm:  '))
cm = x*100
mm = x*1000
print('Para {}m você terá {}cm e {}mm.'.format(x, cm, mm))
print('A medida de {}m corresponde a: \n{}Km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format((x), (x/1000), (x/100), (x/10), (x*10), (x*100),(x*1000)))