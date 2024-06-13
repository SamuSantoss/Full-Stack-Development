CREATE DATABASE InformacoesPessoais;

USE InformacoesPessoais;

CREATE TABLE Pessoas (
    ID INT PRIMARY KEY,
    NomeCompleto VARCHAR(100),
    Idade INT,
    Genero VARCHAR(10),
    Nacionalidade VARCHAR(50),
    Email VARCHAR(100),
    EstadoCivil VARCHAR(20),
    NomePai VARCHAR(100),
    NomeMae VARCHAR(100)
);

INSERT INTO Pessoas (ID, NomeCompleto, Idade, Genero, Nacionalidade, Email, EstadoCivil, NomePai, NomeMae)
VALUES
(1, 'João Silva', 30, 'Masculino', 'Brasileira', 'joao.silva@email.com', 'Solteiro', 'Carlos Silva', 'Maria Silva'),
(2, 'Ana Pereira', 25, 'Feminino', 'Brasileira', 'ana.pereira@email.com', 'Casada', 'José Pereira', 'Clara Pereira'),
(3, 'Carlos Souza', 40, 'Masculino', 'Brasileira', 'carlos.souza@email.com', 'Divorciado', 'Roberto Souza', 'Lúcia Souza');

UPDATE Pessoas
SET NomeCompleto = 'Ana Clara Pereira', Idade = 26, Nacionalidade = 'Portuguesa', Email = 'ana.clara.pereira@email.com'
WHERE ID = 2;

SELECT * FROM Pessoas;

DELETE FROM Pessoas
WHERE ID = 3;

SELECT * FROM Pessoas