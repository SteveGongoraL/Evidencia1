import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
separador = ("°°°" * 40) + "\n"
darInicio = True

while darInicio:
    print("""\nMENU de opciones: \n\n1)- Genero de pelicula con mas Likes(plt).\n2)- Promedio de ganancia(plt).\n3)- Comparar el presupuesto(plt).
          \n4)- Pelicula con mas likes(sns).\n5)- Salir.\n """)
    datos=pd.read_csv('movies.csv')
    df=pd.DataFrame(datos)
    print(separador)
    opcion = input("¿Que operacion deseas realizar?: \n")
    if opcion == "1":
        print("Grafica para ver que genero de pelicula obtuvo mas likes en facebook.\n")
        print(separador)
        df.groupby('genres')['movie_facebook_likes'].sum().plot(kind='barh',legend='Reverse',color="green")
        plt.xlabel("Suma de likes")
        plt.show()
    elif opcion =="2":
        print("Grafica para ver el promedio de ganancias.\n")
        print(separador)
        df.gross.groupby(df.genres).mean().plot(kind='pie',cmap="Paired")
        plt.axis("equal")
        plt.ylabel("")
        plt.title("Promedio de ganancias")
        plt.show()
    elif opcion =="3":
        print("Grafica para comparar el presupuesto con la calificacion de la pelicula.\n")
        print(separador)
        df.groupby('budget')['imdb_score'].sum().plot(kind='bar',legend='Reverse',color="Black")
        plt.xlabel("Presupuesto")
        plt.ylabel("Calificación")
        plt.show()
    elif opcion =="4":
        print("Grafica de Dispercion para ver la pelicula con mas likes.\n")
        print(separador)
        sns.lmplot(x="num",y="movie_facebook_likes",data=df,fit_reg=False,hue="num",legend=False,palette="Paired")
        plt.show()
    elif opcion =="5":
        darInicio=False
    else:
        print("Debes de elegir una opción valida\n ")
else:
    print("Programa Terminado.")