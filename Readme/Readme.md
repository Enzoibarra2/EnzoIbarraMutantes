# Examen Parcial 2 - Mutantes
- Nombre y Apellido: Enzo Ibarra
- Legajo: 811192
- Email: betsabemartin@gmail.com


## ¿De que va el proyecto?

El proyecto contaba en crear un programa para Magneto, el cual quiere reclutar un equipo de mutantes para combatir a las X-MENS , este es un proyecto que mercado libre ofrece como entrevista, y consiste en lo siguiente:

Crear un array de con una longitud de 6 “STRINGS” que se referian a las 6 secuencias de ADN de las personas o mutantes, los cuales son ingresados por el usuario con los siguientes requisitos:

- La cadena no podia contener mas de 6 digitos.
- Sus unicas letras debian ser “A”, “C” , “G”  y “T”

Para determinar si era un mutante o no, por lo menos debia tener 2 o mas secuencias de 4 letras, ya sea horizontal, vertical u oblicua.


## ¿Como se resolvio?

1. Se creo un Array en el cual se cargarian los datos.
    ``` 
    dna = []
    ```
2. Se verifica mediante la siguiente funcion si la cadena ingresada cumple  de tener solo los siguientes caracteres :(A, T, C o G) 

    ``` 
    def ValidarBases(lista) 
    ```

    **Codigo:**
    ``` 
    cadena = cadena.upper()

    
    for caracter in cadena:
        if caracter not in 'ATCG':
            return False


    return True
    ```

3.  En el main con un bucle for se relleno el array que invocaria a la funcion ValidarBases, verificaria si la cadena contiene 6 caracteres y recien ahi terminaria agregando al array:

    ```
    for i in range(6):
    palabra = input(f"_Ingrese secuencia del ADN N° {i + 1} (debe tener 6 letras y solo contener A, T, C, G): ")

    
    while len(palabra) != 6 or not cadena_valida(palabra):
        print("La palabra ingresada no cumple con los requisitos. Por favor, inténtelo de nuevo.")
        palabra = input(f"Ingrese la palabra {i + 1} (debe tener 6 letras y solo contener A, T, C, G): ")

    
    dna.append(palabra)
    ```

4. Mediante un if y un else  se llamaria a la funcion:
    ``` 
    def is_mutant(dna):
    ```
La cual analiza mediante bucles el array dna en todas sus posibilidades (vertical, horizontal y diagonal) de la siguiente manera:

    ```
    sumamutan=0
  
    n = len(dna)

     #-----------------------------VERIFICO VERTICALMENTE-------------------------
    
    for j in range(n):
        column = ''.join(dna[i][j] for i in range(n))
        if has_mutant_sequence(column):
            sumamutan+=1
                        
     # --------------------------VERIFICO HORIZONTALMENTE-------------------------
     
    for i in range(n):
        if has_mutant_sequence(dna[i]):
            sumamutan+=1
                       
     #----------------------------------------------------------------------------
     # ----------------------------VERIFICO DIAGONALES----------------------------
    
    for i in range(n - 3):
        for j in range(n - 3):
            diagonal = ''.join(dna[i + k][j + k] for k in range(4))
            if has_mutant_sequence(diagonal):
                sumamutan+=1
                
     #----------------------------------------------------------------------------           
     #-------------------------AHORA DIAGONALES INVERSAS--------------------------
    for i in range(3, n):
        for j in range(n - 3):
            diagonal = ''.join(dna[i - k][j + k] for k in range(4))
            if has_mutant_sequence(diagonal):
                sumamutan+=1
     #----------------------------------------------------------------------------
     #------------------VERIFICO LA CANTIDAD DE COINCIDENCIAS--------------------- 
       
    if sumamutan>=2:         
      return True
    
    return False
    
    ```
5. Para obtener si verdaderamente si la persona era mutante o no, la estructura if al final del main se veria asi : 
    ```
    if is_mutant(dna):
    print("---------------")
    print("¡Es un mutante!")
    print("---------------")
else:
    print("-----------------------------")
    print("La persona no es un mutante!.")
    print("-----------------------------")
    ```
## ¿Como puedo correrlo?

Se puede acceder desde el link de github siguienrte, clonar el repositorio y correrlo en Visual Studio code.

```
https://github.com/Enzoibarra2/EnzoIbarraMutantes.git
```
Si esto no es posible ingresar a : https://github.com/Enzoibarra2/EnzoIbarraMutantes

##  Pruebas
### Ejemplo 1
```
Ingrese secuencia del ADN N° 1 (debe tener 6 letras y solo contener A, T, C, G): attgcc
Ingrese secuencia del ADN N° 2 (debe tener 6 letras y solo contener A, T, C, G): atgttt
Ingrese secuencia del ADN N° 3 (debe tener 6 letras y solo contener A, T, C, G): agatac
Ingrese secuencia del ADN N° 4 (debe tener 6 letras y solo contener A, T, C, G): aatggc
Ingrese secuencia del ADN N° 5 (debe tener 6 letras y solo contener A, T, C, G): gcggct
Ingrese secuencia del ADN N° 6 (debe tener 6 letras y solo contener A, T, C, G): taatgc

La persona no es un mutante!.
```

### Ejemplo 2
```
  _Ingrese secuencia del ADN N° 1 (debe tener 6 letras y solo contener A, T, C, G): attgcc
_Ingrese secuencia del ADN N° 2 (debe tener 6 letras y solo contener A, T, C, G): atgttt
_Ingrese secuencia del ADN N° 3 (debe tener 6 letras y solo contener A, T, C, G): agatac
_Ingrese secuencia del ADN N° 4 (debe tener 6 letras y solo contener A, T, C, G): aatggc
_Ingrese secuencia del ADN N° 5 (debe tener 6 letras y solo contener A, T, C, G): gcggct
_Ingrese secuencia del ADN N° 6 (debe tener 6 letras y solo contener A, T, C, G): taatgc

La persona no es un mutante!.
```