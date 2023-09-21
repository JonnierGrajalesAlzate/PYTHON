#crear una lista con números de fibonacci
#desde el 0 hasta el número que le pasemos

def fibonacci(num):#se crea una función llamada fibonacci que recibe como parametro (num)
    a,b =0,1#a=0 y b=1
    fibonacci_lista = [0]#la lista comenzará desde el número 0
    for i in range(num):#una iteracion que llegue hasta el valor del parametro que le dimos
        if b > num: return fibonacci_lista#una condicional en donde si b>num nos retone la lista generada
        else: 
            fibonacci_lista.append(b)#sino de lo contrario que agregue a la lista el numero generado
            a,b = b,a+b#a=b y b=a+b
res = fibonacci(20)
print(res)

