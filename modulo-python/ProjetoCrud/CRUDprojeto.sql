create	database loja;
use loja;

create table produto(
id int auto_increment primary key,
nome varchar(60) not null,
descricao varchar(150) not null,
qntd_disponivel int not null,
preco float not null
);

create table venda (
id int auto_increment primary key,
id_produto int not null,
foreign key (id_produto) references produto (id),
qntd_vendida float not null,
data_venda date
);

