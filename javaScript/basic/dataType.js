let str = "texto o cadenas de texto";
let num = 1234; // no need "comillas" para numeros
let float = 1.5; // en javaScript no necesitas identificar los float.
let boolean = "true or false not need to be in capital letter";

// .js no lee numeros fracionales 1/4 pero puedes usarlos

/* Metodos para trabajar con textos:

innerText: .innerText property can be used to change the text of HTML elements.
           Devuelve o establece el texto visible de un elemento. 
           muestra el .js pero no contextual
           Solo texto visible, respeta el CSS que oculta elementos.

textContent: Devuelve o establece el contenido textual completo del elemento.
             Todo el texto, incluso el oculto, como espacios cuando usas " - "
             que dejas espacios con este metodo los lee de la forma contextual
             que lo hisiste.

innerHTML: Todo el contenido HTML interno.

outerHTML: El contenido HTML, incluyendo el elemento en sí mismo.

value: El valor en los elementos de formulario.

*/
/* Simbolos y sus Nombres

    () = parentesis / parentheses
    {} = Llaves / Braces o Curly Brackets
    [] = Corchetes / Brackets
    

*/

/* El uso de === triple equals es para que el resultado sea estricto lo que quieres
    si usas doble == funciona pero puede confundir con str y numeros. */
