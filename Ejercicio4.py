import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "numero"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM Num;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM Num')
    conexion.commit()



def main():
    print("Ingresar Numero")
    Valor=False
    num=0
    est=''
    while (not Valor):
        try:
            Valor=True
            num=int(input())
        except ValueError:
            print("Por favor ingrese un numero)
    if num%2 == 0:
        est= 'Es Compuesto'
        print("El numero ",num, "es compuesto")
    else:
        est='Es Primo'
        print("El numero ",num,"Es primo")
    
    cursor.execute("INSERT INTO NUM(numero,estado) VALUES(%s,%s);" ,(num,est))
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
    print("1. Ingresar numero")
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