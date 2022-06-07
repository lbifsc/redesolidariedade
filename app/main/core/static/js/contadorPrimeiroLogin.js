var contador = 10;

function contar() {
    document.getElementById('contador').innerHTML = contador;
    if(contador <= 0 || contador > 10)
      return;
    contador--;
}

if(window.location.pathname != "/accounts/password_reset/")
  setInterval(contar, 1000);
