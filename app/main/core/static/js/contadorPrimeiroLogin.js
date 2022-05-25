var contador = 10;

function contar() {
    document.getElementById('contador').innerHTML = contador;
    if(contador == 0)
      return;
    contador--;
}

setInterval(contar, 1000);
