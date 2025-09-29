let g = 45;
let obj;
let obj2
let obj3
function setup() {
  createCanvas(700, 500);
  obj = {
    r: 20,
    x: 250,
    y: 250,
    color: { fill: "green", stroke: "black" },
    angle: radians(180), //radianos
    speed: 100,
  };
   obj2 = {
    r: 20,
    x: 450,
    y: 250,
    color: { fill: "red", stroke: "black" },
    angle: radians(0), //radianos
    speed: 100,
  };
  obj3 = {
    x: random(20, 330),
    y: random(20, 480),
    r: 20,
    ponto: 0,
    ponto2: 0,
    color: { fill: "gold", stroke: "black" },
  };
}
function desenhar3(moeda, bola, bola2){
  let xp = 20
  let yp = 10
  let xp2 = 610
  
  fill("orange")
  rect(xp, yp, 70, 20)
  rect(xp2, yp, 70, 20)
  fill("white")
  text(`pontos: ${moeda.ponto}`, xp+5, yp+14)
  text(`pontos: ${moeda.ponto2}`, xp2+5, yp+14)
  
  const lado1 = (moeda.x-bola.x);
  const lado2 = (moeda.y-bola.y);
  const h = sqrt(lado1*lado1+lado2*lado2);
  fill(moeda.color.fill)
  circle(moeda.x, moeda.y, moeda.r*2)
  if (h < moeda.r){
    moeda.x = random(50, 300)
    moeda.y = random(50, 350)
    moeda.ponto += 1
  }
  const lado21 = (moeda.x-bola2.x);
  const lado22 = (moeda.y-bola2.y);
  const h2 = sqrt(lado21*lado21+lado22*lado22);
  fill(moeda.color.fill)
  circle(moeda.x, moeda.y, moeda.r*2)
  if (h2 < moeda.r){
    moeda.x = random(50, 300)
    moeda.y = random(50, 350)
    moeda.ponto2 += 1
  }
}
function desenhar(bola) {
  fill(bola.color.fill);
  circle(bola.x, bola.y, bola.r*2);
  let s = deltaTime / 1000
  let xl = cos(bola.angle) * 20 + bola.x;
  let yl = sin(bola.angle) * 20 + bola.y;
  line(bola.x, bola.y, xl, yl);
    if (keyIsDown(RIGHT_ARROW)){
    bola.angle +=3 * s
  }
  if (keyIsDown(LEFT_ARROW)){
    bola.angle -=3 * s
  }
}
function desenhar2(bola) {
  fill(bola.color.fill);
  stroke(bola.color.stroke);
  circle(bola.x, bola.y, 40);
  let s = deltaTime / 1000
  let xl = cos(bola.angle) * 20 + bola.x;
  let yl = sin(bola.angle) * 20 + bola.y;
  line(bola.x, bola.y, xl, yl);
    if (keyIsDown(68)){
    bola.angle +=3 * s
  }
  if (keyIsDown(65)){
    bola.angle -=3 * s
  }
}
function andar(bola, s) {
    const y = sin(bola.angle) * bola.speed * s;
    const x = cos(bola.angle) * bola.speed * s;
    bola.x += x;
    bola.y += y;
}
function draw() {
  const s = deltaTime / 1000;
  background(220);
  desenhar(obj);
  desenhar2(obj2)
  desenhar3(obj3, obj, obj2)
  if (keyIsDown(UP_ARROW)){
    andar(obj, s)
  }
  if (keyIsDown(87)){
    andar(obj2, s)
  }
}
