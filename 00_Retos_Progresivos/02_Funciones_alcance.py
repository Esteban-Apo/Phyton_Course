""""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */"""
# Sin parámetros ni retorno, con uno o varios parámetros, con retorno
def with_out_parameters():
    print("Funcion numero 1")

def with_parameters(name):
    print ("Hello", name)

def with_return(a, b): 
    resultado = a + b
    return resultado
# Comprueba si puedes crear funciones dentro de funciones
def crear_multiplicador(n): #Funciónes anidadas 
    def multiplicar(x):
        return x * n  # Usa la variable de la función externa
    return multiplicar

# Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
def integrated_functions(): 
    aiter()
    all()
    anext()
    any()
    ascii()

# Pon a prueba el concepto de variable LOCAL y GLOBAL
y = 15
def local_variable(x): 
    x = 10

#Ejercicio conocido como Fizz Buzz
def printf_numbers (text_one, text_two) -> int: #se asume que se retornara un valor entero 
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0: #Valores primos de 3 y a su vez de 5
            print(text_one + text_two)
        elif number % 3 == 0:
            print(text_one)
        elif number % 5 == 0:
            print(text_two)
        else:
            print(number)
            count += 1
    return count

print(printf_numbers("esteban", "Laura"))