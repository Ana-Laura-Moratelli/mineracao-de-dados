CREATE DATABASE base_empresa;

USE base_empresa;

CREATE TABLE clientes (
  codigo_cliente INT NOT NULL,
  nome_cliente VARCHAR(120) NOT NULL,
  endereco_cliente VARCHAR(200) NOT NULL,

  PRIMARY KEY (codigo_cliente)
) ENGINE=InnoDB;

CREATE TABLE produtos (
  codigo_produto INT NOT NULL,
  nome_produto VARCHAR(120) NOT NULL,
  valor_produto DECIMAL(10,2) NOT NULL,

  PRIMARY KEY (codigo_produto)
) ENGINE=InnoDB;

CREATE TABLE vendas (
  codigo_venda INT NOT NULL,
  codigo_cliente INT NOT NULL,
  codigo_produto INT NOT NULL,
  quantidade INT NOT NULL,
  data_venda DATE NOT NULL,

  PRIMARY KEY (codigo_venda),

  CONSTRAINT fk_vendas_clientes
    FOREIGN KEY (codigo_cliente)
    REFERENCES clientes (codigo_cliente)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT fk_vendas_produtos
    FOREIGN KEY (codigo_produto)
    REFERENCES produtos (codigo_produto)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

INSERT INTO `clientes` (`codigo_cliente`, `nome_cliente`, `endereco_cliente`) VALUES
  (1, 'Maria', 'Rua aaa'),
  (2, 'Ana', 'Rua bbb'),
  (3, 'Paula', 'Rua ccc'),
  (4, 'Paulo', 'Rua ddd'),
  (5, 'José', 'Rua eee'),
  (6, 'João', 'Rua fff'),
  (7, 'Laís', 'Rua ggg'),
  (8, 'Eduarda', 'Rua hhh'),
  (9, 'Carolina', 'Rua iii'),
  (10, 'Carlos', 'Rua jjj');

INSERT INTO `produtos` (`codigo_produto`, `nome_produto`, `valor_produto`) VALUES
  (1, 'Arroz', 20),
  (2, 'Feijão', 15),
  (3, 'Macarrão', 10),
  (4, 'Pó de Café', 35),
  (5, 'Sabão em Pó', 25),
  (6, 'Suco', 7),
  (7, 'Refrigerante', 9),
  (8, 'Água Mineral', 3),
  (9, 'Pão de Forma', 13),
  (10, 'Shampoo', 30);

INSERT INTO `vendas` (`codigo_venda`, `codigo_cliente`, `codigo_produto`, `quantidade`, `data_venda`) VALUES
  (1, 1, 5, 2, '2026-03-01'),
  (2, 1, 9, 1, '2026-03-02'),
  (3, 1, 10, 3, '2026-03-03'),
  (4, 1, 1, 1, '2026-03-04'),
  (5, 2, 1, 2, '2026-03-05'),
  (6, 2, 2, 4, '2026-03-06'),
  (7, 3, 7, 1, '2026-03-07'),
  (8, 4, 8, 5, '2026-03-08'),
  (9, 4, 9, 2, '2026-03-09'),
  (10, 4, 10, 1, '2026-03-10'),
  (11, 5, 4, 1, '2026-03-11'),
  (12, 6, 6, 2, '2026-03-12'),
  (13, 7, 10, 1, '2026-03-13'),
  (14, 8, 3, 4, '2026-03-14'),
  (15, 8, 6, 2, '2026-03-15'),
  (16, 8, 10, 1, '2026-03-16'),
  (17, 9, 9, 3, '2026-03-17'),
  (18, 9, 10, 2, '2026-03-18'),
  (19, 10, 3, 1, '2026-03-19'),
  (20, 10, 4, 5, '2026-03-20');

SELECT
  v.codigo_venda,
  c.nome_cliente,
  p.nome_produto,
  v.quantidade,
  v.data_venda,
  (v.quantidade * p.valor_produto) AS total
FROM vendas v
JOIN clientes c ON c.codigo_cliente = v.codigo_cliente
JOIN produtos p ON p.codigo_produto = v.codigo_produto
ORDER BY v.codigo_venda;