// ---------------------- VARIÁVEIS GLOBAIS ----------------------
let jogo;
let imgFundo;
let ship1Img;
let ship2Img;

// ---------------------- PRÉ-CARREGAMENTO DAS IMAGENS ----------------------
function preload() {
  imgFundo = loadImage("fundo.jpg");
  ship1Img = loadImage("ship1.png"); // jogador 1
  ship2Img = loadImage("ship2.png"); // jogador 2
}

// ---------------------- CLASSES PRINCIPAIS ----------------------

// ---- Classe Jogador ----
class Jogador {
  constructor(x, y, imagem, angulo) {
    this.x = x;
    this.y = y;
    this.r = 20;
    this.angle = radians(angulo);
    this.speed = 140;

    this.sprite = imagem; // <<< imagem da nave

    this.trail = [];
  }

  atualizar(dt, teclaFrente, teclaDir, teclaEsq) {
    if (keyIsDown(teclaDir)) this.angle += 3 * dt;
    if (keyIsDown(teclaEsq)) this.angle -= 3 * dt;
    if (keyIsDown(teclaFrente)) {
      this.x += cos(this.angle) * this.speed * dt;
      this.y += sin(this.angle) * this.speed * dt;
    }

    this.x = constrain(this.x, this.r, width - this.r);
    this.y = constrain(this.y, this.r, height - this.r);

    this.adicionarRastro();
  }

  adicionarRastro() {
    this.trail.push({ x: this.x, y: this.y, alpha: 255 });
    if (this.trail.length > 20) this.trail.shift();
  }

  desenhar() {
    // Rastro
    noStroke();
    for (let p of this.trail) {
      fill(255, 255, 255, p.alpha);
      circle(p.x, p.y, this.r * 1.3);
      p.alpha -= 10;
    }

    // NAVE COM IMAGEM
    push();
    translate(this.x, this.y);
    rotate(this.angle + PI / 2); // Ajuste para a nave ficar apontando pra frente
    imageMode(CENTER);
    image(this.sprite, 0, 0, 50, 50); // tamanho da sprite
    pop();
  }
}

// ---- Classe Moeda ----
class Moeda {
  constructor() {
    this.x = random(40, width - 40);
    this.y = random(40, height - 40);
    this.r = 18;
    this.anim = 0;
  }

  reposicionar() {
    this.x = random(40, width - 40);
    this.y = random(40, height - 40);
  }

  desenhar() {
    this.anim += 0.1;
    let pulso = sin(this.anim) * 4;

    noStroke();
    fill(255, 215, 0);
    circle(this.x, this.y, this.r * 2 + pulso);
  }
}

// ---- Classe Game ----
class Game {
  constructor() {
    this.estado = "menu";
    this.timer = 60;
    this.lastTime = millis();

    this.ponto1 = 0;
    this.ponto2 = 0;

    this.moeda = new Moeda();

    this.jog1 = new Jogador(250, 250, ship1Img, 180);
    this.jog2 = new Jogador(450, 250, ship2Img, 0);
  }

  reiniciar(modo) {
    this.estado = modo;
    this.timer = 60;
    this.lastTime = millis();
    this.ponto1 = 0;
    this.ponto2 = 0;

    this.moeda.reposicionar();

    this.jog1 = new Jogador(250, 250, ship1Img, 180);
    this.jog2 = new Jogador(450, 250, ship2Img, 0);
  }

  atualizarTimer() {
    if (millis() - this.lastTime >= 1000) {
      this.timer--;
      this.lastTime = millis();
    }
    textSize(24);
    fill(0);
    text("Tempo: " + this.timer, width / 2, 30);

    if (this.timer <= 0) this.estado = "fim";
  }

  colisao(jog, index) {
    if (dist(jog.x, jog.y, this.moeda.x, this.moeda.y) < jog.r + this.moeda.r) {
      this.moeda.reposicionar();
      if (index === 1) this.ponto1++;
      if (index === 2) this.ponto2++;
    }
  }

  desenharPontuacao() {
    fill("orange");
    rect(20, 10, 90, 25);
    rect(width - 110, 10, 90, 25);

    fill(255);
    textSize(14);
    textAlign(LEFT);
    text("P1: " + this.ponto1, 25, 28);

    textAlign(RIGHT);
    text("P2: " + this.ponto2, width - 25, 28);
  }

  // ---------- TELAS ----------
  telaMenu() {
    background(imgFundo);
    textAlign(CENTER);
    fill(255);
    textSize(40);
    text("JOGO DE COLETA", width / 2, 130);

    textSize(24);
    text("1 - 1 Jogador", width / 2, 230);
    text("2 - 2 Jogadores", width / 2, 270);
    text("S - Sobre", width / 2, 310);
  }

  telaSobre() {
    background(imgFundo);
    fill(255);
    textAlign(CENTER);

    textSize(36);
    text("SOBRE", width / 2, 120);

    textSize(20);
    text("Criado por: Seu Nome Aqui", width / 2, 200);
    text("Exemplo para projeto escolar", width / 2, 240);

    textSize(18);
    text("Pressione ENTER para voltar", width / 2, 380);
  }

  telaFim() {
    background(imgFundo);
    fill(255);
    textAlign(CENTER);

    textSize(36);
    text("FIM DE JOGO", width / 2, 130);

    textSize(24);
    text("Jogador 1: " + this.ponto1, width / 2, 230);
    text("Jogador 2: " + this.ponto2, width / 2, 260);

    text("Pressione ENTER para voltar ao menu", width / 2, 350);
  }

  // ---------- LOOP PRINCIPAL ----------
  desenhar() {
    let dt = deltaTime / 1000;

    background(imgFundo);

    if (this.estado === "menu") return this.telaMenu();
    if (this.estado === "sobre") return this.telaSobre();
    if (this.estado === "fim") return this.telaFim();

    this.atualizarTimer();

    if (this.estado === "jogo1") {
      this.jog1.atualizar(dt, UP_ARROW, RIGHT_ARROW, LEFT_ARROW);
      this.jog1.desenhar();
      this.moeda.desenhar();
      this.colisao(this.jog1, 1);
      this.desenharPontuacao();
      return;
    }

    if (this.estado === "jogo2") {
      this.jog1.atualizar(dt, UP_ARROW, RIGHT_ARROW, LEFT_ARROW);
      this.jog2.atualizar(dt, 87, 68, 65);
      this.jog1.desenhar();
      this.jog2.desenhar();
      this.moeda.desenhar();
      this.colisao(this.jog1, 1);
      this.colisao(this.jog2, 2);
      this.desenharPontuacao();
    }
  }
}

// ---------------------- P5 FUNÇÕES ----------------------
function setup() {
  createCanvas(700, 500);
  jogo = new Game();
}

function draw() {
  jogo.desenhar();
}

function keyPressed() {
  if (jogo.estado === "menu") {
    if (key === "1") jogo.reiniciar("jogo1");
    if (key === "2") jogo.reiniciar("jogo2");
    if (key === "s" || key === "S") jogo.estado = "sobre";
  }

  if (jogo.estado === "sobre" && keyCode === ENTER) jogo.estado = "menu";
  if (jogo.estado === "fim" && keyCode === ENTER) jogo.estado = "menu";
}
