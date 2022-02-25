import statistics as st
import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "NOTAS"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM nota;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM nota')
    conexion.commit()



def main():
    NOTAS=[]
    Valor5=False
    print("Ingrese la nota")
    while (not Valor5):
        try:
            Valor5=True
            nota=int(input())
        except ValueError:
            print("Ingrese de nuevo la nota")
    corr=False
    contador=0
    while (not corr):
        NOTAS.append(nota)
        if contador>3:
            corr=True
        else:
            print("Ingrese la nota")
            try:
                nota=int(input())
            except ValueError:
                print("Ingrese de nuevo el precio")
        contador=contador+1
    lu=str(NOTAS)
    
    media=st.mean(NOTAS)
    mediana=st.median(NOTAS)
    moda=st.mode(NOTAS)
    rango=max(NOTAS, key=int)-min(NOTAS, key=int)
    desvia=st.stdev(NOTAS)
    varianza=st.variance(NOTAS)

    print("La media es:",media)
    print("La mediana es:",mediana)
    print("La moda es:",moda)
    print("El rango es",rango)
    print("La desviación estándar es:",desvia)
    print("La varianza es:",varianza)

    cursor.execute("INSERT INTO nota(notas,media,mediana,moda,rango,des_estandar,varianza) VALUES(%s,%s,%s,%s,%s,%s,%s);" ,(lu,media,mediana,moda,rango,desvia,varianza))
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
    print("1. Ingresar notas")
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