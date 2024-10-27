id = [i for i in range(1,11)]
algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
id_algoritm = []

for id_, algoritm_ in zip(id , algoritm):
    id_algoritm.append(f"{id_} % {algoritm_}")

f = open('algoritm.csv','w',encoding='utf-8')
for i in range(len(id_algoritm)):
    f.write(id_algoritm[i]+'\n')