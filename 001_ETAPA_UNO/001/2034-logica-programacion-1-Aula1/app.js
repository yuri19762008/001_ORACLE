//ADIVINA EL NUMERO SECRETO

let numeroMaximo = 10;
// variables y condicionales
let numeroSecreto = Math.floor(Math.random() * numeroMaximo) + 1; // numero aleatorio entre 1 y 10
//let numeroSecreto = 5;
let numeroUsuario = 0;
let intentos = 1;
//let palabraVeces ='vez';
let maximosIntentos = 3;


while (numeroUsuario != numeroSecreto) {
  let numeroUsuario = parseInt(prompt(`Me indicas un numero entre 1 y ${numeroMaximo}  por favor:`));

  console.log(typeof(numeroUsuario));

  if (numeroUsuario == numeroSecreto) {
    alert(`Acertaste el numero que es : ${numeroSecreto}. lo hiciste en ${intentos} ${intentos == 1 ? 'vez' : 'veces'}`); // operador ternario para mostrar la palabra vez o veces
  } else {
    if (numeroUsuario > numeroSecreto) {
      alert("El numero que ingresaste es mayor al numero secreto");
    } else {
      alert("El numero que ingresaste es menor al numero secreto");
    }
    // Incrementa el valor de intentos
    // intentos = intentos + 1;
    // intentos += 1;
    intentos++;
    
    //palabraVeces = 'veces';
    if (intentos > maximosIntentos) {
        alert(`Lo siento llegaste al numero maximo de ${maximosIntentos} intentos`);
        break;
  }}}




/*
// 1. Muestra una alerta con el mensaje "¡Bienvenida y bienvenido a nuestro sitio web!"
alert("¡Bienvenida y bienvenido a nuestro sitio web!");

// 2. Declara una variable llamada nombre y asígnale el valor "Lua".
let nombre = "Lua";

// 3. Crea una variable llamada edad y asígnale el valor 25.
let edad = 25;

// 4. Establece una variable numeroDeVentas y asígnale el valor 50.
let numeroDeVentas = 50;

// 5. Establece una variable saldoDisponible y asígnale el valor 1000.
let saldoDisponible = 1000;

// 6. Muestra una alerta con el texto "¡Error! Completa todos los campos".
alert("¡Error! Completa todos los campos");

// 7. Declara una variable llamada mensajeDeError y asígnale el valor "¡Error! Completa todos los campos". 
//    Ahora muestra una alerta con el valor de la variable mensajeDeError.
let mensajeDeError = "¡Error! Completa todos los campos";
alert(mensajeDeError);

// 8. Utiliza un prompt para preguntar el nombre del usuario y almacénalo en la variable nombre.
nombre = prompt("Por favor, ingresa tu nombre:");

// 9. Pide al usuario que ingrese su edad usando un prompt y almacénala en la variable edad.
edad = parseInt(prompt("Por favor, ingresa tu edad:"));

// 10. Ahora, si la edad es mayor o igual a 18, muestra una alerta con el mensaje 
//     "¡Puedes obtener tu licencia de conducir!".
if (edad >= 18) {
    alert("¡Puedes obtener tu licencia de conducir!");
}


// calculos de promedio
let cantidadNumeros = prompt('Ingrese la cantidad de números para el cálculo del promedio:');
let suma = 0;
let contador = cantidadNumeros;

while(contador > 0){
    let numero = parseInt(prompt('Ingrese el numero:'));
    suma += numero;
    contador--;
}

let promedio = suma / cantidadNumeros;
alert(`El promedio de los números ingresados es: ${promedio}`);
console.log(promedio);


// 1. Crea un contador que comience en 1 y vaya hasta 10 usando un bucle 'while'. Muestra cada número.
let contador1 = 1;
while (contador1 <= 10) {
    console.log(contador1); // Muestra el número en la consola
    contador1++; // Incrementa el contador
}

// 2. Crea un contador que comience en 10 y vaya hasta 0 usando un bucle 'while'. Muestra cada número.
let contador2 = 10;
while (contador2 >= 0) {
    console.log(contador2); // Muestra el número en la consola
    contador2--; // Decrementa el contador
}

// 3. Crea un programa de cuenta regresiva. Pide un número y cuenta desde 0 hasta ese número utilizando un bucle 'while'.
let numeroRegresivo = parseInt(prompt("Ingresa un número para la cuenta regresiva:"));
let i = numeroRegresivo;
while (i >= 0) {
    console.log(i); // Muestra el número en la consola
    i--; // Decrementa el número
}

// 4. Crea un programa de cuenta progresiva. Pide un número y cuenta desde 0 hasta ese número utilizando un bucle 'while'.
let numeroProgresivo = parseInt(prompt("Ingresa un número para la cuenta progresiva:"));
let j = 0;
while (j <= numeroProgresivo) {
    console.log(j); // Muestra el número en la consola
    j++; // Incrementa el número
}
    */
