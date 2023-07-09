/*--------------------#12 Index Aggregate Function 聚合函式和分群-----------------------------------*/
show databases;
use mydb;
show tables;
create table product4(
	id int primary key auto_increment,
    name varchar(255) not null
);
insert into product4(name) values('美式');
insert into product4(name) values('拿鐵');
insert into product4(name) values('奶茶');
select * from product4;

create table variant4 (
	id int primary key auto_increment,
    product_id int,
    size varchar(2) not null,
    price int not null default 30
);
insert into variant4(product_id,size,price) values(1,'中杯',40);
insert into variant4(product_id,size,price) values(1,'大杯',50);
insert into variant4(product_id,size,price) values(2,'中杯',50);
insert into variant4(product_id,size,price) values(2,'大杯',60);
insert into variant4(product_id,size,price) values(3,'中杯',50);
insert into variant4(product_id,size,price) values(3,'大杯',60);
select * from variant4;

/*主要是用來取得資料表的統計資訊*/
/*count(欄位名稱)計算有幾筆資料 sum總和 max最大值 min最小值 avg平均數 std標準差*/
/*select 聚合函數(欄位名稱) from 資料表名稱 group by 欄位名稱*/
select sum(price) from variant4;
select avg(price),std(price) from variant4;
/*通常會搭配group分群 by 欄位名稱*/
select avg(price) from variant4 group by product_id;
select size,avg(price) from variant4 group by size;

/*綜合運用*/
select product4.name,avg(variant4.price) /*取的產品名稱跟價格平均數*/
from product4 inner join variant4 on product4.id=variant4.product_id  /*建立關聯性*/
group by variant4.product_id; /*依照產品id連接產品名稱分類*/









