show databases; /*查詢伺服器有那些資料庫*/
create database mydb; /*建立新的資料庫*/
drop database mydb; /*刪除資料庫*/

use mydb; /*準備要在哪個資料庫做操作*/

Show tables;/*看資料庫底下有哪些資料表*/

create table product( /*建立產品資料表(product)*/
	品項 int, /*欄位名稱:id 對應的資料型態:int*/
	name varchar(255), /*可存放255個字*/
	price int
);

select * from product;/*取出資料表中的全部資料*/

insert into product(品項,name,price) values(1,'拿鐵',50);/*新增資料(欄位名稱)values(資料)*/
insert into product(品項,name,price) values(2,'美式',40);

drop table product; /*刪除資料表*/




/*----------------------- #5 Table 資料表：主鍵、欄位設定-----------------------------*/
use mydb;
Show tables;
create table product( 
	id int, 
	name varchar(255),
	price int
);
insert into product(id,name,price) values(1,'拿鐵',50);
insert into product(id,name,price) values(2,'美式',40);
insert into product(id,name,price) values(2,'奶茶',45); /*狀況一：編號重複*/
insert into product(id,price) values(3,30);  /*狀況二：name忘了打(會變成空值)*/
select * from product; /* *代表所有欄位 */
drop table product;

-- 創建正確的產品資料表 -- 
create table product( 
	id int primary key auto_increment, 
    /*primary key主鍵(每一筆資料的編號不重複) auto_increment自動增加(每次新增資料自動將編號+1)*/ 
	name varchar(255) not null, /*not null 不允許空值*/
	price int not null default 30 /*default 欄位預設值30元*/
);
insert into product(id,name,price) values(1,'拿鐵',50);
insert into product(id,name,price) values(2,'美式',40);
insert into product(id,name,price) values(2,'奶茶',45); /*狀況一：編號重複*/ /*會跳出錯誤*/
insert into product(name,price) values('奶茶',45); /*不用輸入id就會自動增加*/
insert into product(id,price) values(3,30);  /*狀況二：name忘了打(會變成空值)*/ /*會跳出錯誤*/
insert into product(name) values('青茶'); /*價格就是預設值*/




/*----------------------- #6 Table 資料表：篩選資料 -----------------------------*/
select * from product; /* *代表所有欄位 */
select * from product where price=45; /* where 篩選條件*/
select * from product where price>30;
select * from product where price<40;
select * from product where price<>50;
select * from product where name='青茶';
select * from product where price<>50 and name='美式';
select * from product where price=50 and name='奶茶'; /*沒有這種資料所以空值*/
select * from product where price=50 or name='奶茶';

select name from product where price=45; /*只取出特定欄位的資料*/
select name,price from product where price=45; /*多個特定欄位用,隔開*/




/*-------------------#7 Table 資料表：更新、刪除資料---------------------*/
/*先關閉MySQL Workbench的安全設定*/
set sql_safe_updates=0;

update product set price=50 where name='奶茶'; /*若要更新特篩選條件的資料就要加上where*/
update product set price=55,name='奶茶加倍' where id=4; /*一次更新多個欄位*/
update product set price=35 where price<=35; /*低於35元的都漲價成35*/

delete from product where name='奶茶加倍'; /*刪除資料*/

select * from product;/*取出資料表中的全部資料*/



























