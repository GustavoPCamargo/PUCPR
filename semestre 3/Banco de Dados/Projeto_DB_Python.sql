DROP DATABASE IF EXISTS DB_PYTHON;
CREATE DATABASE DB_PYTHON;
USE DB_PYTHON;

CREATE TABLE `usuario` (
  `ID_Usuario` INT NOT NULL PRIMARY KEY,
  `Nome` varchar(100) NOT NULL,
  `Celular` varchar(20) NOT NULL,
  `Login` varchar(50) DEFAULT NULL,
  `Senha` varchar(64) DEFAULT NULL,
  UNIQUE KEY `Login_UNIQUE` (`Login`)
) ;

INSERT INTO `usuario` (ID_Usuario, Nome, Celular, Login, Senha) VALUES 
(1, 'José da Silva','(41) 99999-1234','jose.silva','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
(2, 'Maria dos Anjos','(41) 98888-1234','maria.anjos','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
(3, 'Gabriela Duarte Alves','(41) 977777-1234','g.alves','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
(4,'Olivia Oliveira Santos','(41) 91234-1234','oli.oliveira','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
(5, 'Camila Andrade P. Alves','(41) 81234-1234','camila.andrade','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
(6, 'Daniela Dutra','(41)98765-1234','d.dutra','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
(7, 'Manoel Estevão','(41) 97777-1111','m.estavao','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
(8, 'Ricardo Alencar','(41)8765-1234','ricardo.alencar','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
(9, 'Estela Lorena','(41)98765-1234','e.lorena','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
(10, 'Vitor Frank','(41)95432-1234','vitor.f','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6'),
(11, 'Zelia Amaro','(41)96555-6789','zelia.a','e06b1afd38ddb78b3f87842adc69bd243286f24c7b4ba9c94aaedf366fa064e6');

SELECT * FROM usuario;