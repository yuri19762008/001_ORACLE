// Array para almacenar los nombres de los amigos
let amigos = [];
// Array para almacenar las parejas sorteadas
let historialSorteos = [];

// Función para añadir un amigo a la lista
function agregarAmigo() {
    const inputAmigo = document.getElementById('amigo');
    const nombreAmigo = inputAmigo.value.trim();

    // Validación para que solo se ingresen textos (letras y espacios)
    const soloLetras = /^[a-zA-Z\s]+$/;

    if (nombreAmigo !== '') {
        if (soloLetras.test(nombreAmigo)) {
            amigos.push(nombreAmigo);
            actualizarListaAmigos();
            inputAmigo.value = ''; // Limpiar el campo de texto después de añadir
        } else {
            alert('Por favor, ingrese solo letras y espacios.');
        }
    } else {
        alert('Por favor, escribe un nombre.');
    }
}

// Función para actualizar la lista de amigos en el DOM
function actualizarListaAmigos() {
    const listaAmigos = document.getElementById('listaAmigos');
    listaAmigos.innerHTML = '';

    amigos.forEach((amigo) => {
        const li = document.createElement('li');
        li.textContent = amigo;
        listaAmigos.appendChild(li);
    });
}

// Función para realizar el sorteo de amigo secreto
function sortearAmigo() {
    if (amigos.length < 3) {
        alert('Debes añadir al menos tres amigos para realizar el sorteo.');
        return;
    }

    const resultado = document.getElementById('resultado');
    resultado.innerHTML = '';

    let amigosCopy = [...amigos];
    let sorteados = [];
    let intentos = 0;

    while (sorteados.length < amigos.length && intentos < 100) {
        sorteados = [];
        amigosCopy = [...amigos];
        let parejasTemporales = [];

        amigos.forEach((amigo) => {
            let posibles = amigosCopy.filter(a => a !== amigo);
            let amigoSorteado = null;

            if (posibles.length > 0) {
                const indiceSorteado = Math.floor(Math.random() * posibles.length);
                amigoSorteado = posibles[indiceSorteado];
            }

            if (amigoSorteado && !parejasTemporales.includes(`${amigo} → ${amigoSorteado}`) && !parejasTemporales.includes(`${amigoSorteado} → ${amigo}`)) {
                sorteados.push(`${amigo} → ${amigoSorteado}`);
                parejasTemporales.push(`${amigo} → ${amigoSorteado}`);
                amigosCopy = amigosCopy.filter(a => a !== amigoSorteado);
            }
        });

        if (sorteados.length === amigos.length && !historialSorteos.includes(JSON.stringify(parejasTemporales))) {
            historialSorteos.push(JSON.stringify(parejasTemporales));
        } else {
            sorteados = [];
        }
        intentos++;
    }

    sorteados.forEach((sorteo) => {
        const li = document.createElement('li');
        li.textContent = sorteo;
        resultado.appendChild(li);
    });

    if (intentos >= 100) {
        alert('No fue posible realizar un sorteo sin repeticiones. Intenta de nuevo.');
    }
}
