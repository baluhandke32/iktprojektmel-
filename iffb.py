inventions=[]
f=open("ipariforradalom.txt","r",encoding="utf-8")
for sor in f:
    kislista=sor[:-1].split(";")
    inventions.append(kislista)
f.close()

