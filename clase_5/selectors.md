# Selectores CSS relevantes

## 1. Selectores básicos

- **Universal**  
  
  * { margin: 0; padding: 0; box-sizing: border-box; }
 
  Aplica la regla a **todos** los elementos del documento. 

- **Por etiqueta (tipo)**  

  body { font-family: Arial, sans-serif; }
  p { line-height: 1.5; }
  
  Afecta a todas las etiquetas de ese tipo (`body`, `p`, `h1`, etc.). 

- **Por clase**  
  
  .contenedor_calculadora { width: 80vw; }
  .numbers { border: 1px solid #000; }
  
  Se aplica a todos los elementos que tengan `class="..."`. 

- **Por id**  
  
  #contenedor_calculadora { background-color: #ccc; }
  
  Afecta al elemento con ese `id` (debe ser único en la página). 

## 2. Combinadores (selectores de relación)

- **Descendiente (espacio)**  
  
  #contenedor_calculadora p { color: white; }
  
  Selecciona todos los `p` que estén dentro de `#contenedor_calculadora`, sin importar el nivel. 

- **Hijo directo (`>`)**  
  
  form > label { font-weight: bold; }
  
  Solo los `label` que son hijos directos de `form`. 

- **Hermano adyacente (`+`)**  

  input[type="radio"] + label { margin-right: 10px; }
  
  Selecciona el `label` que viene justo después del `input` radio. 

## 3. Selectores de atributo

- **Por atributo y valor**  
  
  input[type="number"] { width: 100px; }
  input[name="operacion"] { cursor: pointer; }
  
  Aplica estilos a elementos según sus atributos HTML. 

## 4. Pseudoclases comunes

- **Interacción**  

  button:hover { background-color: #0275d8; }
  input:focus { outline: 2px solid #0275d8; }
  
  `:hover` cuando el mouse está encima, `:focus` cuando el elemento tiene foco. 

- **Estado de enlaces (para referencia)**  
  
  a:link { color: blue; }
  a:visited { color: purple; }
  a:active { color: red; }
  
  Diferentes estados de un enlace. 

## 5. Selectores combinados útiles en formularios

- **Etiqueta + clase**  
  
  button.primary { background-color: #0275d8; color: white; }
  
  Solo botones que además tengan la clase `primary`. 

- **Múltiples clases en un mismo elemento**  
  
  .numbers.operacion { font-weight: bold; }
  
  Elementos que tienen **las dos** clases: `numbers` y `operacion`. 

  | Tipo                | Sintaxis / Ejemplo                           | Qué selecciona                                                 |
|---------------------|----------------------------------------------|----------------------------------------------------------------|
| Universal           | * { ... }`                                  | Todos los elementos del documento                             |
| Tipo (etiqueta)     | p { ... }`                                  | Todas las etiquetas `<p>`                                     |
| Clase               | .contenedor { ... }`                        | Elementos con `class="contenedor"`                            |
| ID                  | #principal { ... }`                         | Elemento con `id="principal"` (único)                         |
| Descendiente        | #contenedor p { ... }`                      | Cualquier `<p>` dentro de `#contenedor`                       |
| Hijo directo        | ul > li { ... }`                            | `<li>` que son hijos directos de `<ul>`                       |
| Hermano adyacente   | h2 + p { ... }`                             | Primer `<p>` justo después de un `<h2>`                       |
| Hermanos generales  | h2 ~ p { ... }`                             | Todos los `<p>` después de un `<h2>` (mismo padre)            |
| Atributo            | input[type="text"] { ... }`                 | `input` cuyo `type` es `"text"`                               |
| Atributo contiene   | a[href*="https"] { ... }`                   | Enlaces cuyo `href` contiene `"https"`                        |
| Atributo empieza    | a[href^="https://"] { ... }`                | Enlaces cuyo `href` empieza por `"https://"`                  |
| Atributo termina    | a[href$=".pdf"] { ... }`                    | Enlaces cuyo `href` termina en `.pdf`                         |
| Pseudoclase :hover  | button:hover { ... }`                       | Elemento cuando el mouse está encima                          |
| Pseudoclase :focus  | input:focus { ... }`                        | Elemento con foco (teclado/cursor)                            |
| Pseudoclase :active | a:active { ... }`                           | Enlace mientras se hace clic                                  |
| Estado enlaces      | a:link`, `a:visited`                        | Enlaces normales y ya visitados                               |
| :first-child        | li:first-child { ... }`                     | Primer hijo `<li>` de su padre                                |
| :last-child         | li:last-child { ... }`                      | Último hijo `<li>` de su padre                                |
| :nth-child()        | tr:nth-child(2n) { ... }`                   | Hijos en posiciones concretas (pares, impares, etc.)          |
| :not()              | input:not([type="submit"]) { ... }`         | Elementos que **no** cumplen el selector dentro de `:not()`   |
| Pseudoelemento ::before | p::before { content: "★ "; }`          | Contenido “falso” antes del contenido real del elemento       |
| Pseudoelemento ::after  | p::after { content: " ▾"; }`           | Contenido “falso” después del contenido real del elemento     |
| Pseudoelemento ::first-line | p::first-line { ... }`             | Primera línea visual de un párrafo                            |
| Pseudoelemento ::first-letter | p::first-letter { ... }`         | Primera letra del párrafo                                     |