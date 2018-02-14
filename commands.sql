select * from tweets;
select * from users;
select * from faves;
select * from follows;
select first_name from user;
select first_name, last_name from user;
select first_name from users where id = 2;
select last_name from users where id = 2; or id = 3;
select from users where first_namelike "K%";
select from users order by birthday desc;
select from users order by birthday asc;
insert into twitter, tweets
UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)
INSERT INTO table_name (column_name1, column_name2)
VALUES('column1_value', 'column2_value');
DELETE FROM table_name WHERE condition(s)
