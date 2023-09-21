#CREANDO CONJUNTOS CON EL "set"
conjunto = set(["jonnier", "grajales", 21])

#METIENDO UN CONJUNTO DENTRO DE OTRO CONJUNTO
conjunto_1 = frozenset(["jonnier", "grajales"])
conjunto_2 ={conjunto_1, "erika", "alzate"}

#CREANDO CONJUNTOS NORMALONGOS
conjunto_normal = {"jonnier", "grajales", 21}

#teoria de conjuntos
conjuto_padre = {1,3,5,7}
conjunto_hijo ={2,4,5,8}

#issubset es conjuntohijo es un subconjunto de conjuntopadre
resultado = conjunto_hijo.issubset(conjuto_padre)#true

#issuperset es conjuntopadre es un superconjunto de conjuntohijo
resultado2 = conjuto_padre.issuperset(conjunto_hijo)#true

#verificar si hay un numero en comun 
res = conjunto_hijo.isdisjoint(conjuto_padre)#sale false ya que todos son distinct

#imprimir
print(res)