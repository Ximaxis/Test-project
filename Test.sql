
-- Работа выполнялась на базе MySQL8
drop database if exists test;
create database test;
use test;

-- Таблица заголовка заказа

drop table if exists order_headers;
create table order_headers (
    id int not null auto_increment unique primary key, -- Идентификатор таблицы заказа, 
	-- лучше использовать serial для id но не стал сильно начальные условия менять
    reg_number VARCHAR(100) not null, -- Регистрационный номер заказа
    on_date datetime default now() -- Дата формирования заказа
    
    
);

-- Таблица деталей заказа

drop table if exists order_details ;
create table order_details  (
	id int not null auto_increment unique primary key, -- Идентификатор строки деталей заказа
	hdr_id int not null, -- Идентификатор заказа
	good_id int not null, -- Идентификатор товара
	amount DECIMAL(19,4) not null, -- Количество товара
    price DECIMAL(19,2) not null, -- Цена за единицу измерения товара для данного заказа
	
    foreign key (hdr_id) references order_headers(id)
);

-- Test insert

insert into order_headers (reg_number, on_date) values
('NWMX23214JJ', default),
('NSDKW241411', '2020-08-12 22:01:15'),
('DJWIOR784268', default)
;
insert into order_details (hdr_id, good_id, amount, price) values
('1','1','12412','412.24'),
('1','2','15125.3644','6412.13'),
('1','3','112412.22','6412.13'),
('1','4','76512.2622','1212.13'),
('2','5','45742.5822','24412.13'),
('2','6','68662.7822','36412.13'),
('2','7','88662.7822','76412.13'),
('2','1','46412','412.24'),
('3','8','15','4'),
('3','9','4','15'),
('3','6','3262','36412.13')
;


-- Выборка

select oh.*, od.*
from order_headers oh
join  (select o.*, max(o.price * o.amount) as summ_order 
from order_details o 
left join order_details d on o.hdr_id = d.hdr_id 
     	and o.price < d.price 
     where d.price is null 
    group by o.hdr_id) od on od.hdr_id = oh.id
;

