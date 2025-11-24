//VARIÁVEIS
let jogo;
let imgFundo;
let ship1Img;
let ship2Img;

let somMoeda;
let somPowerUp;

let musicaFundo; 

//tempos
const POWER_SPAWN_INTERVAL = 7000;
const SPECIAL_COIN_INTERVAL = 5000;
const POWER_DURATION_MS = 5000;

function preload() {
  imgFundo = loadImage("fundo.jpg");
  ship1Img = loadImage("ship1.png");
  ship2Img = loadImage("ship2.png");
  
  somMoeda = loadSound("moeda.mp3");
  somPowerUp = loadSound("powerup.mp3");

  musicaFundo = loadSound("musica.mp3");
}

//CLASSES

//Jogador
class Jogador {
  constructor(x, y, imagem, angulo) {
    this.x = x;
    this.y = y;
    this.r = 20;
    this.angle = radians(angulo);
    this.speed = 140;

    this.sprite = imagem;

    this.trail = [];

    this.pointMult = 1;
    this.speedMult = 1;
    this.effectEnd = {};
  }

  atualizar(dt, teclaFrente, teclaDir, teclaEsq) {

    this._expireEffects();

    if (keyIsDown(teclaDir)) this.angle += 5 * dt;
    if (keyIsDown(teclaEsq)) this.angle -= 5 * dt;
    if (keyIsDown(teclaFrente)) {
      this.x += cos(this.angle) * this.speed * this.speedMult * dt;
      this.y += sin(this.angle) * this.speed * this.speedMult * dt;
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
    // RASTRO
    noStroke();
    for (let p of this.trail) {
      fill(255, 165, 0, p.alpha);
      circle(p.x, p.y, this.r * 0.5);
      p.alpha -= 10;
    }

    // NAVE IMAGEM
    push();
    translate(this.x, this.y);
    rotate(this.angle + PI / 2); //nave apontando pra frente
    imageMode(CENTER);
    if (this.sprite) image(this.sprite, 0, 0, 50, 50);
    else {
      fill(200);
      stroke(0);
      triangle(0, -18, -12, 12, 12, 12);
    }
    pop();
  }

  aplicarEfeito(nome, duracaoSegundos) {
    const agora = millis();
    this.effectEnd[nome] = agora + duracaoSegundos * 1000;

    if (nome === "2xpoints") {
      this.pointMult = 2;
    } else if (nome === "2xspeed") {
      this.speedMult = 2;
    }
  }

  _expireEffects() {
    const agora = millis();
    for (let nome in this.effectEnd) {
      if (this.effectEnd[nome] <= agora) {
        // expira efeito
        if (nome === "2xpoints") this.pointMult = 1;
        if (nome === "2xspeed") this.speedMult = 1;
        delete this.effectEnd[nome];
      }
    }
  }
}

//Moeda
class Moeda {
  constructor(valor = 1) {
    this.x = random(40, width - 40);
    this.y = random(40, height - 40);
    this.r = 18;
    this.anim = 0;
    this.valor = valor;
    this.color = (this.valor === 2) ? color(180, 0, 180) : color(255, 215, 0);
  }

  reposicionar() {
    this.x = random(40, width - 40);
    this.y = random(40, height - 40);
  }

  desenhar() {
    this.anim += 0.1;
    let pulso = sin(this.anim) * 4;
    noStroke();
    fill(this.color);
    circle(this.x, this.y, this.r * 2 + pulso);
    if (this.valor === 2) {
      fill(255);
      textSize(12);
      textAlign(CENTER, CENTER);
      text("2", this.x, this.y);
    }
  }
}

//PowerUp
class PowerUp {
  constructor(type) {
    this.type = type;
    this.x = random(50, width - 50);
    this.y = random(80, height - 50);
    this.r = 18;
    this.anim = random(0, TWO_PI);
  }

  desenhar() {
    this.anim += 0.12;
    push();
    translate(this.x, this.y);
    const pulso = 1 + 0.08 * sin(this.anim);
    scale(pulso);
    noStroke();
    if (this.type === "2xpoints") fill(0, 200, 0);
    else if (this.type === "2xspeed") fill(0, 150, 255);
    circle(0, 0, this.r * 2);
    fill(255);
    textAlign(CENTER, CENTER);
    textSize(12);
    text(this.type === "2xpoints" ? "2x" : "2v", 0, 0);
    pop();
  }
}

// game
class Game {
  constructor() {
    this.estado = "menu";
    this.timer = 60;
    this.lastTime = millis();

    this.ponto1 = 0;
    this.ponto2 = 0;

    this.moedas = [ new Moeda(1) ];
    this.specialCoins = [];

    this.jog1 = new Jogador(250, 250, ship1Img, 180);
    this.jog2 = new Jogador(450, 250, ship2Img, 0);

    // powerups
    this.powerUps = [];

    // timers
    this.lastPowerSpawn = millis();
    this.lastSpecialCoinSpawn = millis();
  }

  reiniciar(modo) {
    this.estado = modo;
    this.timer = 60;
    this.lastTime = millis();
    this.ponto1 = 0;
    this.ponto2 = 0;

    this.moedas = [ new Moeda(1) ];
    this.specialCoins = [];

    this.jog1 = new Jogador(250, 250, ship1Img, 180);
    this.jog2 = new Jogador(450, 250, ship2Img, 0);

    this.powerUps = [];
    this.lastPowerSpawn = millis();
    this.lastSpecialCoinSpawn = millis();
  }

  atualizarTimer() {
    if (millis() - this.lastTime >= 1000) {
      this.timer--;
      this.lastTime = millis();
    }
    textSize(24);
    textAlign(CENTER)
    fill("white");
    text("Tempo: " + this.timer, width / 2, 30);

    if (this.timer <= 0) this.estado = "fim";
  }

  colisaoComMoedas(jog, index) {

    for (let i = this.moedas.length - 1; i >= 0; i--) {
      const m = this.moedas[i];
      if (dist(jog.x, jog.y, m.x, m.y) < jog.r + m.r) {
        const ganhos = m.valor * (jog.pointMult || 1);
        if (index === 1) this.ponto1 += ganhos;
        if (index === 2) this.ponto2 += ganhos;
        
        somMoeda.play();
        
        this.moedas[i].reposicionar();
      }
    }

    for (let i = this.specialCoins.length - 1; i >= 0; i--) {
      const m = this.specialCoins[i];
      if (dist(jog.x, jog.y, m.x, m.y) < jog.r + m.r) {
        const ganhos = m.valor * (jog.pointMult || 1);
        if (index === 1) this.ponto1 += ganhos;
        if (index === 2) this.ponto2 += ganhos;

        somMoeda.play();
        
        this.specialCoins.splice(i, 1);
      }
    }
  }

  desenharPontuacao() {
    fill("orange");
    rect(20, 15, 100, 25);
    fill(255);
    textSize(14);
    textAlign(LEFT);
    text("Player 1: " + this.ponto1, 25, 28);

    if (this.estado === "jogo2") {
      fill("orange");
      rect(width - 110, 15, 100, 25);
      fill(255);
      textAlign(RIGHT);
      text("Player 2: " + this.ponto2, width - 25, 28);
    }
  }

  //TELAS
  telaMenu() {
    background(imgFundo);
    textAlign(CENTER);
    fill(255);
    textSize(40);
    text("BALLS GAME RETURNS:\n Deluxe edition™", width / 2, 130);

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
    text("Criado por: Gustavão cray cray", width / 2, 200);
    text("Um dos jogos mais esperados deste ano retorna \nmaior, melhor e mais forte, concorrente a GOTY\n BALLS GAME\n feito para um projeto da PUCPR", width / 2, 240);

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
    text("Player 1: " + this.ponto1, width / 2, 230);
    text("Player 2: " + this.ponto2, width / 2, 260);

    text("Pressione ENTER para voltar ao menu", width / 2, 350);
  }

  maybeSpawnPowerUps() {
    const agora = millis();
    if (agora - this.lastPowerSpawn >= POWER_SPAWN_INTERVAL) {

      const tipos = ["2xpoints", "2xspeed"];
      const t = random(tipos);
      this.powerUps.push(new PowerUp(t));
      this.lastPowerSpawn = agora;
    }
  }

  maybeSpawnSpecialCoins() {
    const agora = millis();
    if (agora - this.lastSpecialCoinSpawn >= SPECIAL_COIN_INTERVAL) {

      this.specialCoins.push(new Moeda(2));
      this.lastSpecialCoinSpawn = agora;
    }
  }

  checkPowerCollisions() {
    for (let i = this.powerUps.length - 1; i >= 0; i--) {
      const pu = this.powerUps[i];

      let colidiu = false;
      
      if (dist(pu.x, pu.y, this.jog1.x, this.jog1.y) < pu.r + this.jog1.r) {
        if (pu.type === "2xpoints") this.jog1.aplicarEfeito("2xpoints", 5);
        else if (pu.type === "2xspeed") this.jog1.aplicarEfeito("2xspeed", 10);
        colidiu = true;
      }
      
      if (this.estado === "jogo2" && dist(pu.x, pu.y,           this.jog2.x, this.jog2.y) < pu.r + this.jog2.r) {
        if (pu.type === "2xpoints") this.jog2.aplicarEfeito("2xpoints", 5);
        else if (pu.type === "2xspeed") this.jog2.aplicarEfeito("2xspeed", 10);
        colidiu = true;
      }

      if (colidiu) {
        somPowerUp.play();
        
        this.powerUps.splice(i, 1);
      }
    }
  }

  //LOOP PRINCIPAL
  desenhar() {
    let dt = deltaTime / 1000;

    background(imgFundo);

    if (this.estado === "menu") return this.telaMenu();
    if (this.estado === "sobre") return this.telaSobre();
    if (this.estado === "fim") return this.telaFim();

    this.atualizarTimer();

    this.maybeSpawnPowerUps();
    this.maybeSpawnSpecialCoins();


    for (let pu of this.powerUps) pu.desenhar();
    for (let sc of this.specialCoins) sc.desenhar();

    // Jogo 1 jogador
    if (this.estado === "jogo1") {
      this.jog1.atualizar(dt, UP_ARROW, RIGHT_ARROW, LEFT_ARROW);
      this.jog1.desenhar();

      for (let m of this.moedas) m.desenhar();
      for (let sc of this.specialCoins) sc.desenhar();

      this.colisaoComMoedas(this.jog1, 1);

      this.checkPowerCollisions();

      this.desenharPontuacao();
      return;
    }

    // Jogo 2 jogadores
    if (this.estado === "jogo2") {
      this.jog1.atualizar(dt, UP_ARROW, RIGHT_ARROW, LEFT_ARROW);

      this.jog2.atualizar(dt, 87, 68, 65); 
      this.jog1.desenhar();
      this.jog2.desenhar();

      for (let m of this.moedas) m.desenhar();
      for (let sc of this.specialCoins) sc.desenhar();

      this.colisaoComMoedas(this.jog1, 1);
      this.colisaoComMoedas(this.jog2, 2);

      this.checkPowerCollisions();

      this.desenharPontuacao();
    }
  }
}

//funcões
function setup() {
  createCanvas(700, 500);
  jogo = new Game();
  
  musicaFundo.setLoop(true);
}

function mouseClicked() {
  if (musicaFundo.isLoaded() && !musicaFundo.isPlaying()) {
    musicaFundo.play();
  }
}

function draw() {
  jogo.desenhar();
}

function keyPressed() {
  if (musicaFundo.isLoaded() && !musicaFundo.isPlaying()) {
      musicaFundo.play();
  }
  
  if (jogo.estado === "menu") {
    if (key === "1") jogo.reiniciar("jogo1");
    if (key === "2") jogo.reiniciar("jogo2");
    if (key === "s" || key === "S") jogo.estado = "sobre";
  }

  if (jogo.estado === "sobre" && keyCode === ENTER) {
    jogo.estado = "menu";
  }
  
  if (jogo.estado === "fim" && keyCode === ENTER) {
    jogo.estado = "menu";
  }
}