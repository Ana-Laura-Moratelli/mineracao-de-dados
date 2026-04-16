CREATE DATABASE loja_pet
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE loja_pet;

CREATE TABLE clientes (
  id_cliente INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nome       VARCHAR(120) NOT NULL,
  email      VARCHAR(180) NOT NULL,
  cidade     VARCHAR(80)  NOT NULL,
  estado     CHAR(2)      NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_cliente),
  UNIQUE KEY uk_clientes_email (email)
) ENGINE=InnoDB;

CREATE TABLE produtos (
  id_produto INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nome       VARCHAR(140) NOT NULL,
  categoria  VARCHAR(60)  NOT NULL,
  preco      DECIMAL(10,2) NOT NULL,
  ativo      TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (id_produto),
  KEY idx_produtos_categoria (categoria),
  CHECK (preco >= 0)
) ENGINE=InnoDB;

CREATE TABLE pedidos (
  id_pedido   BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_cliente  INT UNSIGNED NOT NULL,
  data_pedido DATE NOT NULL,
  status      VARCHAR(20) NOT NULL,  -- Pago, Enviado, Cancelado
  canal       VARCHAR(20) NOT NULL,  -- Site, WhatsApp, Marketplace
  frete       DECIMAL(10,2) NOT NULL DEFAULT 0,
  PRIMARY KEY (id_pedido),
  KEY idx_pedidos_cliente (id_cliente),
  KEY idx_pedidos_data (data_pedido),
  CONSTRAINT fk_pedidos_clientes
    FOREIGN KEY (id_cliente)
    REFERENCES clientes (id_cliente)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CHECK (frete >= 0)
) ENGINE=InnoDB;

CREATE TABLE itens_pedido (
  id_item     BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_pedido   BIGINT UNSIGNED NOT NULL,
  id_produto  INT UNSIGNED NOT NULL,
  quantidade  INT NOT NULL,
  preco_unit  DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id_item),
  KEY idx_itens_pedido (id_pedido),
  KEY idx_itens_produto (id_produto),
  CONSTRAINT fk_itens_pedidos
    FOREIGN KEY (id_pedido)
    REFERENCES pedidos (id_pedido)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT fk_itens_produtos
    FOREIGN KEY (id_produto)
    REFERENCES produtos (id_produto)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CHECK (quantidade > 0),
  CHECK (preco_unit >= 0)
) ENGINE=InnoDB;

INSERT INTO clientes (nome, email, cidade, estado) VALUES
('Ana Souza', 'ana.souza@email.com', 'São José dos Campos', 'SP'),
('Bruno Lima', 'bruno.lima@email.com', 'Taubaté', 'SP'),
('Carla Ferreira', 'carla.ferreira@email.com', 'Jacareí', 'SP'),
('Diego Alves', 'diego.alves@email.com', 'Campinas', 'SP'),
('Elaine Rocha', 'elaine.rocha@email.com', 'São Paulo', 'SP'),
('Felipe Santos', 'felipe.santos@email.com', 'Guarulhos', 'SP'),
('Gabriela Nunes', 'gabriela.nunes@email.com', 'Sorocaba', 'SP'),
('Henrique Costa', 'henrique.costa@email.com', 'Santos', 'SP'),
('Isabela Martins', 'isabela.martins@email.com', 'São José dos Campos', 'SP'),
('João Pereira', 'joao.pereira@email.com', 'Ribeirão Preto', 'SP');

INSERT INTO produtos (nome, categoria, preco) VALUES
('Ração Premium Cães 10kg', 'Ração', 189.90),
('Ração Premium Gatos 10kg', 'Ração', 179.90),
('Petisco Dental 200g', 'Petiscos', 29.90),
('Shampoo Hipoalergênico 500ml', 'Higiene', 39.90),
('Areia Sanitária 4kg', 'Higiene', 24.90),
('Brinquedo Mordedor', 'Brinquedos', 19.90),
('Coleira Ajustável', 'Acessórios', 34.90),
('Tapete Higiênico 30un', 'Higiene', 49.90);

INSERT INTO pedidos (id_cliente, data_pedido, status, canal, frete) VALUES
(1, '2026-01-03', 'Pago', 'Site', 18.00),
(2, '2026-01-05', 'Enviado', 'WhatsApp', 12.00),
(3, '2026-01-06', 'Pago', 'Site', 15.00),
(4, '2026-01-08', 'Cancelado', 'Marketplace', 0.00),
(5, '2026-01-10', 'Enviado', 'Site', 22.00),
(6, '2026-01-12', 'Pago', 'WhatsApp', 10.00),
(7, '2026-01-14', 'Pago', 'Site', 18.00),
(8, '2026-01-16', 'Enviado', 'Marketplace', 25.00),
(9, '2026-01-18', 'Pago', 'Site', 14.00),
(10,'2026-01-20', 'Pago', 'WhatsApp', 9.00),
(1, '2026-02-02', 'Enviado', 'Site', 18.00),
(2, '2026-02-03', 'Pago', 'Marketplace', 20.00),
(3, '2026-02-05', 'Pago', 'Site', 15.00),
(4, '2026-02-07', 'Enviado', 'WhatsApp', 11.00),
(5, '2026-02-09', 'Cancelado', 'Site', 0.00),
(6, '2026-02-11', 'Pago', 'Site', 16.00),
(7, '2026-02-12', 'Enviado', 'Marketplace', 24.00),
(8, '2026-02-15', 'Pago', 'WhatsApp', 8.00),
(9, '2026-02-18', 'Pago', 'Site', 14.00),
(10,'2026-02-20', 'Enviado', 'Site', 19.00);

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unit) VALUES
(1, 1, 1, 189.90), (1, 3, 2, 29.90),
(2, 5, 3, 24.90),  (2, 6, 1, 19.90),
(3, 2, 1, 179.90), (3, 8, 1, 49.90),
(4, 7, 1, 34.90),  (4, 6, 2, 19.90),
(5, 1, 1, 189.90), (5, 4, 1, 39.90),
(6, 3, 4, 29.90),  (6, 6, 1, 19.90),
(7, 8, 2, 49.90),  (7, 5, 2, 24.90),
(8, 2, 1, 179.90), (8, 7, 1, 34.90),
(9, 1, 1, 189.90), (9, 3, 1, 29.90),
(10,6, 2, 19.90),  (10,5, 1, 24.90),
(11,1, 1, 189.90), (11,8, 1, 49.90),
(12,2, 1, 179.90), (12,3, 3, 29.90),
(13,4, 2, 39.90),  (13,5, 2, 24.90),
(14,7, 1, 34.90),  (14,6, 3, 19.90),
(15,8, 1, 49.90),  (15,3, 2, 29.90),
(16,1, 1, 189.90), (16,5, 4, 24.90),
(17,2, 1, 179.90), (17,8, 2, 49.90),
(18,3, 2, 29.90),  (18,6, 2, 19.90),
(19,4, 1, 39.90),  (19,7, 2, 34.90),
(20,1, 1, 189.90), (20,3, 1, 29.90);

SELECT
  p.id_pedido,
  p.data_pedido,
  p.status,
  p.canal,
  c.nome AS cliente,
  SUM(i.quantidade * i.preco_unit) AS subtotal_itens,
  p.frete,
  (SUM(i.quantidade * i.preco_unit) + p.frete) AS total_pedido
FROM pedidos p
JOIN clientes c ON c.id_cliente = p.id_cliente
JOIN itens_pedido i ON i.id_pedido = p.id_pedido
GROUP BY p.id_pedido, p.data_pedido, p.status, p.canal, c.nome, p.frete
ORDER BY p.id_pedido;