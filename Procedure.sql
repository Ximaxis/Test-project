
-- Работа выполнялась на базе MySQL8
use test;


-- Процедура


DELIMITER //

drop procedure if exists update_product //
create procedure update_product 
(
	date_from datetime, 
	date_to datetime, 
	good_id_old int, 
	good_id_new int
	)
begin
	
	-- В первую временную таблицу заносятся все заказы которые надо заменить
	
	drop table if exists tmp_table ;
	create temporary table tmp_table
	(select hdr_id, good_id 
	from order_headers o
	join (select * from order_details where good_id = good_id_old) d on o.id = d.hdr_id
	where on_date > date_to and on_date < date_from);

	-- проверяем если запись есть данные для изменений, то продолжаем выполнение скрипта
	
if (select exists(select * from tmp_table))
    then
    
    -- во вторую временнную таблицу заносим id уже имеющихся таких же товаров в изменяемых заказах 
    -- и стоимость товара за неимением глобальной таблицы с товарами, откуда её можно было бы взять
    
	drop table if exists tmp_table2 ;
	create temporary table tmp_table2
	(select hdr_id, d.id, price, amount
	from order_headers o
	join (select * from order_details where good_id = good_id_new) d on o.id = d.hdr_id
	where on_date > date_to and on_date < date_from and o.id in (select hdr_id from tmp_table) );
	
	-- Обновляем id товара и задаем новую цену 

	update order_details old ,
	tmp_table as new
	set
	old.good_id = good_id_new, old.price = (select price from tmp_table2 limit 1)
	where 
	old.good_id = good_id_old and new.hdr_id = old.hdr_id
;	

	-- Увеличиваем количество товара если такой уже был
	
	update order_details old ,
	tmp_table2 as new
	set
	old.amount = (old.amount + new.amount)
	where 
	old.good_id = good_id_new and new.hdr_id = old.hdr_id
;
	
	-- удаляем дублирующиеся товары в змененых заказах

	delete 
	from order_details old3
	where old3.id in (select id from tmp_table2)
	;
end if;
end //

DELIMITER ;

-- вызов процедуры

call update_product ('2020-08-15','2020-08-12','1','6');

-- вызов таблицы

select * from order_details;