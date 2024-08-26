CREATE TABLE IF NOT EXISTS gerenciador_tarefas (
    id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(255),
    data_criacao DATE,
    data_conclusao DATE,
    autor VARCHAR(100)
);

INSERT INTO gerenciador_tarefas (descricao, data_criacao, data_conclusao, autor) 
VALUES
('ASHUDHUASDHUAS', '2024-08-22', '2025-09-24', 'Holando'),
('KJDGFNJDFJGDF', '2023-09-24', '2026-10-23', 'HolANDINHA');