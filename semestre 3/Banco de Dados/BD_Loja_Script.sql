DROP DATABASE IF EXISTS Loja;
CREATE DATABASE Loja;
USE Loja;

-- =====================================================

CREATE TABLE cliente (
    idCliente INT PRIMARY KEY AUTO_INCREMENT, 
    nome VARCHAR(100),
    email VARCHAR(50),
    usuario VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(64) NOT NULL
);

CREATE TABLE produto (
    idProduto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    descricao VARCHAR(100),
    valor DECIMAL(9,2),
    fkIdCategoria INT 
);

CREATE TABLE categoria (
    idCategoria INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    genero VARCHAR(100)
);

ALTER TABLE produto ADD CONSTRAINT fkIdCategoria
    FOREIGN KEY (fkIdCategoria)
    REFERENCES categoria (idCategoria)
    ON DELETE RESTRICT;

-- =====================================================

INSERT INTO cliente (nome, email, usuario, senha) VALUES
('Joao Santos',	'joaoS@email.com', 'joao.santos', 'e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
('Maria Campos', 'mariasC@email.com', 'maria.campos', 'e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
('Ana Lúcia Cunha', 'anaLC@email.com',  'ana.cunha', 'e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
('Luiz Pontes', 'luizP@email.com', 'l.pontes', 'e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
('Pedro Alves', 'pedroA@email.com', 'pedro.alves', 'e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
('Gabriel Pereira', 'gabrielP@email.com', 'gabriel.pereira', 'e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
('Carlos Silva', 'calosS@email.com', 'carlos.silva', 'e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
('Bianca Dantas', 'biancaD@email.com', 'bianca.dantas', 'e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
('Cristiane Rezende', 'c.rezende@email.com', 'cristiane.resende', 'e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6');

INSERT INTO categoria (nome, genero) VALUES
('Camiseta / Blusa', 'Unisex'),
('Calça', 'Unisex'),
('Jaqueta', 'Unisex'),
('Vestido', 'Feminino'),
('Calçado', 'Unisex'),
('Bermuda', 'Masculino'),
('Calçado', 'Feminino'),
('Chapéu', 'Unisex');


INSERT INTO produto ( nome, descricao, valor, fkIdCategoria) VALUES
('Camiseta Básica',    'Camiseta de algodão confortável',                 49.90, 1),
('Calça Jeans Skinny', 'Calça jeans ajustada ao corpo',                  129.90, 2) ,
('Jaqueta de Couro',   'Jaqueta sintética com acabamento premium',       199.90, 3),
('Vestido Floral',     'Vestido curto estampado floral',                  89.90, 4),
('Tênis Esportivo',    'Tênis leve ideal para corrida',                  249.90, 5),
('Blusa de Moletom',   'Moletom com capuz e bolso frontal',              159.90, 1),
('Bermuda Cargo',      'Bermuda com bolsos laterais e ajuste na cintura', 79.90, 6),
('Sandália Feminina',  'Sandália confortável com salto médio',           119.90, 7),
('Boné Snapback',      'Boné ajustável com aba reta',                     59.90, 8);


SELECT * FROM cliente;
SELECT * FROM produto;
SELECT * FROM categoria;