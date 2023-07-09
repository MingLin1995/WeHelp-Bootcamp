/*--------------------#8 Join 合併查詢-----------------------------------*/
show databases;
use mydb;
show tables;

/*建立品項的資料表*/
create table product_inf(     
	id int primary key auto_increment,
    name varchar(255) not null
);
insert into product_inf(name) values('美式');
insert into product_inf(name) values('拿鐵');
insert into product_inf(name) values('奶茶');
select * from product_inf;

/*建立選項的資料表*/
create table variant(
	id int primary key auto_increment,
    product_id int,   /*這是連接的關鍵*/
    size varchar(2) not null,
    price int not null default 30
);
insert into variant(product_id,size,price) values(1,'中杯',40);
insert into variant(product_id,size,price) values(1,'大杯',50);
insert into variant(product_id,size,price) values(2,'中杯',60);
insert into variant(product_id,size,price) values(2,'大杯',70);
insert into variant(product_id,size,price) values(3,'中杯',80);
insert into variant(product_id,size,price) values(3,'大杯',90);
select * from variant;

/*合併查詢兩個資料表(全部資料)*/ /*select * from 資料表一 inner join 資料表二 on 合併條件*/
select * from product_inf inner join variant on product_inf.id=variant.product_id;
/*合併查詢兩個資料表(特定欄位)*/
select product_inf.name,variant.size,variant.price 
from product_inf inner join variant on product_inf.id=variant.product_id;


/*--------------------#9 Left Join 左合併、Right Join 右合併-----------------------------------*/
/*透過left、right可以包含未對應到的資料*/

/*新增沒有對應到的資料*/
insert into product_inf(name) values('青茶');
insert into variant (product_id,size,price) value (5,'大杯',100);

select * from product_inf left join variant on product_inf.id=variant.product_id; /*會出現青茶，但沒有對應的資料，所以沒有其他資訊*/
select * from product_inf right join variant on product_inf.id=variant.product_id;/*會出相關資訊，但沒有對應的資料，所以沒有青茶*/

/*GPT教學 union 無論是否有對應都取出*/
select * from product_inf left join variant on product_inf.id=variant.product_id
union
select * from product_inf right join variant on product_inf.id=variant.product_id;


/*--------------------#10 Foreign Key 外鍵的觀念和設置-----------------------------------*/
/*外鍵，就是建立關聯性，防止資料缺漏，保持一致性*/

/*alter table 資料表二 add foreign key (外鍵欄位名稱) references 資料表一(主鍵欄位名稱)*/
alter table variant add foreign key (product_id) references product_inf (id);

/*選項資料表新增外鍵的設定，連接到產品資料表的主鍵 可以防止資料被誤刪(有關連性的不能刪除)*/
delete from product_inf where id=3; /*沒辦法刪除因為有foreign key的限制*/

/*若要刪除，要先把資料表二的"外鍵欄位"刪除，才可以刪除資料表一*/
delete from variant where product_id=3;


