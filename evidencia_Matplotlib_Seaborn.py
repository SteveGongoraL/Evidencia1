import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
separador = ("°°°" * 40) + "\n"
darInicio = True

while darInicio:
    print("""\nMENU de opciones: \n\n1)- Genero de pelicula con mas Likes(plt).\n2)- Promedio de ganancia(plt).\n3)- Promedio de Likes(plt).\n4)- Comparar el presupuesto(plt).
          \n5)- Pelicula con mas likes(sns).\n6)- Comparar ganacias(sns).\n7)- Comparar generos(sns).\n8)- Comparar los likes por año(sns).\n9)- Comprobar likes agrupado en clasificacion(sns).
          \n10)- Salir.\n """)
    datos=pd.read_csv('movies.csv')
    df=pd.DataFrame(datos)
    print(separador)
    opcion = input("¿Que operacion deseas realizar?: \n")

    if opcion == "1":
        print("Grafica para ver que genero de pelicula obtuvo mas likes en facebook\n")
        print(separador)
        df.groupby('genres')['movie_facebook_likes'].sum().plot(kind='barh',legend='Reverse',color="green")
        plt.xlabel("Suma de likes")
        plt.show()
    elif opcion =="2":
        print("Grafica para ver el promedio de ganancias \n")
        print(separador)
        df.gross.groupby(df.genres).mean().plot(kind='pie',cmap="Paired")
        plt.axis("equal")
        plt.ylabel("")
        plt.title("Promedio de ganancias")
        plt.show()
    elif opcion =="3":
        print("Grafica para ver en promedio que genero obtuvo mas likes en facebook\n")
        print(separador)
        df.groupby('genres')['movie_facebook_likes'].mean().plot(kind='line',legend='Reverse',color="Purple")
        plt.xlabel("Promedio de likes")
        plt.show()
    elif opcion =="4":
        print("Grafica para comparar el presupuesto con la calificacion de la pelicula\n")
        print(separador)
        df.groupby('budget')['imdb_score'].sum().plot(kind='bar',legend='Reverse',color="Black")
        plt.xlabel("Presupuesto")
        plt.ylabel("Calificación")
        plt.show()
    elif opcion =="5":
        print("Grafica de Dispercion para ver la pelicula con mas likes.")
        print(separador)
        sns.lmplot(x="num",y="movie_facebook_likes",data=df,fit_reg=False,hue="num",legend=False,palette="Paired")
        plt.show()
    elif opcion =="6":
        print("Grafica para comparar ganancias con la calificacion de la pelicula")
        print(separador)
        g=sns.lmplot(x="gross",y="imdb_score",data=df,palette="Set1")
        plt.show()
    elif opcion =="7":
        print("Grafica para comparar generos con los likes de facebook, calificacion y ganancias")
        print(separador)
        nuevo=df[["genres","movie_facebook_likes","gross","imdb_score"]]
        sns.set(style="ticks",color_codes=True)
        g=sns.pairplot(nuevo,hue="genres",palette="Spectral")
        plt.show()
    elif opcion =="8":
        print("Graficas para comparar los likes por año de cada pelicula")
        print(separador)
        g=sns.lmplot(x="imdb_score",y="movie_facebook_likes",data=df,hue="num",col="title_year",aspect=.4,x_jitter=0.1)
        plt.show()
    elif opcion =="9":
        print("Grafica para comparar la clasificacion de la pelicula con likes y ganancias")
        print(separador)
        g=sns.lmplot(x="gross",y="movie_facebook_likes",hue="content_rating",data=df,palette="Set1")
        plt.show()
    elif opcion =="10":
        darInicio=False
    else:
        print("Debes de elegir una opción valida\n ")
else:
    print("Programa Terminado.")