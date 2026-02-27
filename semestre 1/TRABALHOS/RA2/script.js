const form = document.getElementById('cadastroForm');
const btnSalvar = document.getElementById('btnSalvar');
const listaUsuarios = document.getElementById('listaUsuarios');

//inputs
const nome = document.getElementById('nome');
const email = document.getElementById('email');
const senha = document.getElementById('senha');
const confirmaSenha = document.getElementById('confirmaSenha');
const termos = document.getElementById('termos');
const telefone = document.getElementById('telefone');

//erros
const erroNome = document.getElementById('erroNome');
const erroEmail = document.getElementById('erroEmail');
const erroSenha = document.getElementById('erroSenha');
const erroConfirmaSenha = document.getElementById('erroConfirmaSenha');
const erroTermos = document.getElementById('erroTermos');

//validação
form.addEventListener('input', validarFormulario);

function validarFormulario() {
  let valido = true;

  //nome
  if (nome.value.trim().length < 3) {
    erroNome.textContent = "Nome deve ter pelo menos 3 caracteres";
    valido = false;
  } else erroNome.textContent = "";

  //e-mail
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email.value)) {
    erroEmail.textContent = "E-mail inválido";
    valido = false;
  } else erroEmail.textContent = "";

  //senha
  const senhaRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
  if (!senhaRegex.test(senha.value)) {
    erroSenha.textContent = "Senha deve ter 8 ou mais caracteres com letras e números";
    valido = false;
  } else erroSenha.textContent = "";

  //confirma senha
  if (confirmaSenha.value !== senha.value || confirmaSenha.value === "") {
    erroConfirmaSenha.textContent = "Senhas não são iguais";
    valido = false;
  } else erroConfirmaSenha.textContent = "";

  //termos
  if (!termos.checked) {
    erroTermos.textContent = "Você deve aceitar os termos";
    valido = false;
  } else erroTermos.textContent = "";

  btnSalvar.disabled = !valido;
}

//máscara telefone
telefone.addEventListener('input', () => {
  let valor = telefone.value.replace(/\D/g, '');
  if (valor.length > 11) valor = valor.slice(0, 11);

  if (valor.length > 6) {
    telefone.value = `(${valor.slice(0,2)}) ${valor.slice(2,7)}-${valor.slice(7)}`;
  } else if (valor.length > 2) {
    telefone.value = `(${valor.slice(0,2)}) ${valor.slice(2)}`;
  } else {
    telefone.value = valor;
  }
});

//envio
form.addEventListener('submit', (e) => {
  e.preventDefault();

  const li = document.createElement('li');
  li.textContent = `${nome.value} - ${email.value}`;
  listaUsuarios.appendChild(li);

  form.reset();
  btnSalvar.disabled = true;
});
