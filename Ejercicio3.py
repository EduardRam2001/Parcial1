import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "precio"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM IVA;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM IVA')
    conexion.commit()



def main():
    print("Ingrese el precio")
    Valor5=False
    while (not Valor5):
        try:
            Valor5=True
            pre=float(input())
        except ValueError:
            print("Ingrese de nuevo el precio")
    sinIVA=pre/1.12
    IVA=sinIVA*0.12
    
    print("El precio del producto sin IVA es: Q","{:.2f}".format(sinIVA))
    print("La cantidad de IVA es de: Q" ,"{:.2f}".format(IVA))
    print("\n")
        
    cursor.execute("INSERT INTO IVA(precio,sin_IVA,iva) VALUES(%s,%s,%s);" ,(pre,sinIVA,IVA))
    conexion.commit()
    
    



def pedirnumero():
    Valor=False
    num=0
    while (not Valor):
        try:
            Valor=True
            num=int(input())
        except ValueError:
            print("Por favor seleccion una opcion correcta")
    return num


salir2= False
while not salir2:
    print("--------MENÚ-----------------")
    print("1. Ingresar Precio")
    print("2. Ver registro")
    print("3. Elimar datos")
    print("4. Salir")
    print("-----------------------------")
    print("Ingrese una opción")

    opcion=pedirnumero()

    if opcion==1:
        main()
    elif opcion==2:
        Histprial()
    elif opcion==3:
        Borradatos()
    elif opcion==4:
        salir2=True
    else:
        print("Por favor ingrese un número que este en el menú \n")

cursor.close()
conexion.close()  

print("ADIOS :)")