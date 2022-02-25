import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Dados"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM datos;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM datos')
    conexion.commit()


def dados():
    salir= False
    while not salir:
        print("Lanzar los dados")

        print("Resultado del primer dado")
        Valor=False
        dado1=0
        while (not Valor):
            try:
                Valor=True
                dado1=int(input())
            except ValueError:
                print("Ingrese de nuevo el numero del dado")
        Valor1=False
        dado2=0
        print("Resultado del segundo dado")
        while (not Valor1):
            try:
                Valor1=True
                dado2=int(input())
            except ValueError:
                print("Ingrese de nuevo el numero del dado")
        res=''
        if dado1+dado2==8:
            print("Usted ha ganado")
            salir=True
            res='A ganado'
        elif dado1+dado2==7:
            print("Usted ha perdido")
            salir=True
            res='A perdio'
        elif dado1+dado2<7 or dado1+dado2>8:
            print("Vueva a tirar de nuevo")
            res='Nada'
            cursor.execute("INSERT INTO datos(dado1,dado2,estado) VALUES(%s,%s,%s);" ,(dado1,dado2,res))
            conexion.commit()

    cursor.execute("INSERT INTO datos(dado1,dado2,estado) VALUES(%s,%s,%s);" ,(dado1,dado2,res))
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
    print("1. Lanzar dados")
    print("2. Ver registro")
    print("3. Elimar datos")
    print("4. Salir")
    print("-----------------------------")
    print("Ingrese una opción")

    opcion=pedirnumero()

    if opcion==1:
        dados()
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
