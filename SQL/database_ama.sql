-- drop database database_ama;
-- SET GLOBAL FOREIGN_KEY_CHECKS = 0;
create database if not exists database_ama;
use database_ama;

-- criacao de tabelas
create table categoria (
    id int primary key unique not null auto_increment,
    descricao varchar(45)
);
create table entidades (
    id int primary key not null auto_increment,
    cnpj varchar(14) unique not null,
    nome varchar(90) not null,
    nomeFantasia varchar(45) not null,
    telefone varchar(24) unique not null,
    email varchar(90) unique not null,
    endereco varchar(90) not null
);
create table representante (
    id int primary key unique not null auto_increment,
    entidades_id int not null,
    nome varchar(90) not null,
    cpf varchar(11) unique not null,
    endereco varchar(90) not null,
    observacao varchar(90)
);
create table log (
    id int primary key unique not null auto_increment,
    usuario_id int not null,
    logData date not null,
    logHora time not null,
    tabela varchar(24) not null,
    registro int not null,
    operacao varchar(45) not null
);
create table papel (
    id int primary key unique not null auto_increment,
    descricao varchar(45)
);
create table usuario (
    id int primary key unique not null auto_increment,
    representante_id int not null,
    papel_id int not null,
    login varchar(45) unique not null,
    senha varchar(45) unique not null
);
create table lista (
    id int primary key unique not null auto_increment
);
create table lista_itens (
    id int primary key unique not null auto_increment,
    lista_id int not null,
    itens_id int not null,
    quantidade int not null
);
create table itens (
    id int primary key unique not null auto_increment,
    categoria_id int not null,
    descricao varchar(45) not null
);
create table familia (
    id int primary key unique not null auto_increment,
    nomeChefeFamilia varchar(90) not null,
    cpfChefeFamilia varchar(11) not null,
    enderecoChefeFamilia varchar(90) not null
);
create table integranteFamilia (
    id int primary key unique not null auto_increment,
    familia_id int not null,
    nome varchar(90) not null,
    cpf varchar(11) unique not null
);
create table movimentos (
    id int primary key unique not null auto_increment,
    lista_id int not null,
    usuario_id int not null,
    familia_id int not null,
    dataMovimento date not null,
    horaMovimento time not null,
    justificativa varchar(45)
);

 -- criacao de relacionamentos
alter table representante
add foreign key (entidades_id)
references entidades(id);

alter table itens
add foreign key (categoria_id)
references categoria(id);

alter table lista_itens
add foreign key (itens_id)
references itens(id);

alter table lista_itens
add foreign key (lista_id)
references lista(id);

alter table Log
add foreign key (usuario_id)
references usuario(id);

alter table usuario
add foreign key (papel_id)
references papel(id);

alter table usuario
add foreign key (representante_id)
references representante(id);

alter table integranteFamilia
add foreign key (familia_id)
references familia(id);

alter table movimentos
add foreign key (lista_id)
references lista(id);

alter table movimentos
add foreign key (usuario_id)
references usuario(id);

alter table movimentos
add foreign key (usuario_id)
references usuario(id);

alter table movimentos
add foreign key (familia_id)
references familia(id);

 -- insercao de dados
insert entidades
(id, cnpj, nome, nomeFantasia, telefone, email, endereco)
values
(1,'12345678910111', 'teste one', 'teste 1', '12345678', 'teste1@teste.com', 'rua teste, 123'),
(2,'23456789101112', 'teste two', 'teste 2', '23456789', 'teste2@teste.com', 'rua teste, 234'),
(3,'34567891011121', 'teste three', 'teste 3', '34567890', 'teste3@teste.com', 'rua teste, 345'),
(4,'45678910111213', 'teste four', 'teste 4', '45678901', 'teste4@teste.com', 'rua teste, 456'),
(5,'56789101112131', 'teste five', 'teste 5', '56789012', 'teste5@teste.com', 'rua teste, 567');

insert representante
(id, entidades_id, nome, cpf, endereco, observacao)
values
(1,1,'one', '12345678901', 'one house, 1', 'nenhuma'),
(2,2,'two', '23456789012', 'two house, 2', 'nenhuma'),
(3,3,'three', '34567890123', 'three house, 3', 'nenhuma'),
(4,4,'four', '45678901234', 'four house, 4', 'nenhuma'),
(5,5,'five', '56789012345', 'five house, 5', 'nenhuma'),
(6,0,'six', '67890123456', 'six house, 6', 'nenhuma');

insert categoria
(id, descricao)
values
(1,'cesta basica'),
(2,'remedio'),
(3,'alimento perecivel'),
(4,'alimento nao perecivel');

insert itens
(id, categoria_id, descricao)
values
(1,1,'cesta simples'),
(2,2,'aspirina'),
(3,3,'queijo'),
(4,4,'arroz');

insert lista
(id)
values
(1),
(2);

insert lista_itens
(id, lista_id, itens_id, quantidade)
values
(1, 1, 1, 3),
(2, 1, 1, 1),
(3, 2, 4, 20),
(4, 2, 3, 50);

insert familia
(id, nomeChefeFamilia, cpfChefeFamilia, enderecoChefeFamilia)
values
(1,'alpha filho', '12345678901', 'rua one, 321'),
(2,'beta filho', '23456789012', 'rua two, 432'),
(3,'gamma', '34567890123', 'rua three, 543');

insert integranteFamilia
(id, familia_id, nome, cpf)
values
(1,1,'alpha pai', '12345543211'),
(2,1,'alpha mae', '23456654322'),
(3,2,'beta pai', '34567765433'),
(4,2,'beta vo', '45678876544'),
(5,2,'beta mae', '56789987655');

insert papel
(id, descricao)
values
(1,'admin'),
(2,'user');

insert usuario
(id, papel_id, representante_id, login, senha)
values
(1,1,1,'admin','admin'),
(2,2,2,'user','user');

insert movimentos
(id, lista_id, usuario_id, familia_id, dataMovimento, horaMovimento, justificativa)
values
(1,1,2,1,'01-01-01','01:01:01','nenhuma'),
(2,2,2,2,'02-02-02','02:02:02','nenhuma');

insert log 
(id, usuario_id, logData, logHora, tabela, registro, operacao) 
values 
(1,1,'02-01-01','01:01:01','usuario',2,'add usuario');








