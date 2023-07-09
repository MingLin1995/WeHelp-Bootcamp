use mydb;
show tables;
create table product5(
	id int primary key auto_increment,
    name varchar(255) not null
);
insert into product5(name) values('美式');
insert into product5(name) values('拿鐵');
insert into product5(name) values('奶茶');
select * from product5;
