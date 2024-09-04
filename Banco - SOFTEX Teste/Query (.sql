CREATE DATABASE IF NOT EXISTS banco;

USE banco;

CREATE TABLE IF NOT EXISTS dados (
    id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    data_criacao DATE,
    saldo INT

);

CREATE TABLE IF NOT EXISTS extrato (
    id INT,
    nome VARCHAR(255),
    data_criacao DATE,
    saldo INT

);

