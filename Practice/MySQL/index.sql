/*--------------------#11 Index 索引的觀念和實作-----------------------------------*/
show databases;
use mydb;
show tables;

create table product3(     
	id int primary key auto_increment,
    name varchar(255) not null
);
insert into product3(name) values('美式');
insert into product3(name) values('拿鐵');
insert into product3(name) values('奶茶');
insert into product3(name) values('青茶');
insert into product3(name) values('綠茶');

select * from product3;
explain select * from product3 where name='青茶'; /*explain 可以了解細節運作*/ /*檢查五筆資料，整個資料的百分之20%是我們要的資料*/


/*index 建立樹狀結構，可以提高搜尋速度*/
/*新增索引 alter table 資料表 add index 索引名稱(參考的欄位名稱)*/
alter table product3 add index name_index(name);/*再次用explain執行，會發現是直接用索引去搜尋，實際檢查一筆資料，就找到我們要的，速度提升五倍*/

/*刪除索引 alter table 資料表 drop index 索引名稱*/
alter table product3 drop index name_index;

/*主鍵也是一種索引*/
explain select * from product3 where id=4;


