-- Data prepapred by Amir Salimi
  
PRAGMA foreign_keys = ON;

insert into users values ('mc@gmail.com','Michael Choi','abcd','Edmonton','M');
insert into users values ('tedwalsh@td.com','Ted Walsh','7632','Calgary','M');
insert into users values ('hm@mah.com','Harry Mah','1453','Waterloo, ON','M');
insert into users values ('ks@gmail.com','Kaitlyn Scott','pqwe','Toronto, ON','F');
insert into users values ('angels@gmail.com','Angel Silverman','anlo','Edmonton','F');
insert into users values ('mk@abc.com','Maximillion Kung','0931','Burnaby, BY','F');
insert into users values ('davood@gmail.com','Davood Rafiei','1234','Edmonton','M');
insert into users values ('amr@yahoo.ca','Amir Salimi','123445','Edmonton','O');
insert into users values ('amrv2@yahoo.ca','Amir Salimi','123445','Edmonton','O');
insert into users values ('chomsky@mit.edu','Noam Chomsky','420420','MIT','N');

insert into products values ('P01', 'Nikon F100');
insert into products values ('P02', 'Nikon D3500');
insert into products values ('P03', 'BMW M8');
insert into products values ('P04', 'ps4xbox');
insert into products values ('P06', 'ps4xbox');
insert into products values ('P07', 'Porsche 91');
insert into products values ('P08', 'Porsche 98');
insert into products values ('P10', 'kettle');
insert into products values ('P11', 'kettle2');
insert into products values ('P12', 'kettle sold as item only');


insert into sales values ('S01', 'mc@gmail.com', 'P06',  datetime('now','-365 days'), 'ticket ps4', 'Mint', 1400);
insert into sales values ('S02', 'mc@gmail.com', 'P04',  datetime('now','-730 days'), 'xbox Voucher', 'Used', 698);
insert into sales values ('S03', 'hm@mah.com', 'P04', datetime('now','+3 days'), ' xxboxx x', 'New', 10);
insert into sales values ('S04', 'ks@gmail.com', 'P06', datetime('now','-1 days'), 'tick ps4', 'ticket', 3000);
insert into sales values ('S042', 'ks@gmail.com', 'P04', datetime('now','-1 days'), 'vouch  xBoX', 'ticket', 3000);
insert into sales values ('S041', 'ks@gmail.com', 'P08', datetime('now','+4 days'), 'vouch', 'voucher', 3000); 
insert into sales values ('S05', 'angels@gmail.com', 'P12', datetime('now','+1 minute'), 'ticket', 'very old', 30);
insert into sales values ('S051', 'angels@gmail.com', 'P01', datetime('now','+3 days','-10 minute'), 'ticket', 'very old', 30); 
insert into sales values ('S052', 'angels@gmail.com', 'P02',datetime('now','+3 days','+10 minute'), 'ticket', 'very old', 30); 
insert into sales values ('S06', 'davood@gmail.com', 'P03', datetime('now','+1 days','+6 hour','1 minute'), 'voucher', 'useful voucher', 424);
insert into sales values ('S07', 'davood@gmail.com', 'P04', datetime('now','+100 days','-6 hour','-10 minute'), 'ps4 xbox', 'old console', 424);
insert into sales values ('S08', 'ks@gmail.com', 'P08', datetime('now','-100 days'), 'PS4 xbox', 'mint', 10000);
insert into sales values ('S09', 'chomsky@mit.edu', 'P10', datetime('now','+100 days','-1 hour','-11 minute'), 'ok kettle', 'new', 1);
insert into sales values ('S091', 'chomsky@mit.edu', 'P11', datetime('now','+100 days''+2 hour','+41 minute'), 'good kettle', 'new', 2);
insert into sales values ('S092', 'davood@gmail.com', 'P01', datetime('now','+100 days'), 'great camera', 'new', 3);
insert into sales values ('S093', 'davood@gmail.com', 'P12', datetime('now','+300 days'), 'a kettle', 'new', 100);
insert into sales values ('S010', 'amrv2@yahoo.ca', 'P07', datetime('now','+300 days'), 'lorum ipsum', 'new', 100);


insert into bids values ('B01', 'hm@mah.com', 'S01', '2016-04-01', 1405.02);
insert into bids values ('B02', 'ks@gmail.com', 'S01', '2016-04-02', 1407.99);
insert into bids values ('B03', 'hm@mah.com', 'S02', '2018-09-11', 299);
insert into bids values ('B04', 'davood@gmail.com', 'S02', '2018-09-12', 999);
insert into bids values ('B05', 'angels@gmail.com', 'S03', '2016-01-03', 499);
insert into bids values ('B06', 'tedwalsh@td.com', 'S04', '2019-05-19', 3000);
insert into bids values ('B07', 'ks@gmail.com', 'S04', '2019-05-20', 4000);
insert into bids values ('B08', 'ks@gmail.com', 'S04', '2019-05-21', 100); 
insert into bids values ('B09', 'tedwalsh@td.com', 'S04', '2019-06-22', 101);
insert into bids values ('B091', 'tedwalsh@td.com', 'S042', '2019-06-22', 8001);
insert into bids values ('B101', 'angels@gmail.com', 'S06', '2020-01-0', 421);
insert into bids values ('B102', 'angels@gmail.com', 'S06', '2020-01-07', 422);
insert into bids values ('B103', 'angels@gmail.com', 'S06', '2020-01-07', 424);
insert into bids values ('B11', 'amr@yahoo.ca', 'S07', '2018-09-12', 25);
insert into bids values ('B111', 'amr@yahoo.ca', 'S08', '2018-09-12', 50);

-- insert into items values ('S01', 1, 'N01', 'Nikon F100 body');
-- insert into items values ('S01', 2, 'N01', 'Nikon 50mm, f/1.4 lens');
-- insert into items values ('S03', 1, 'N02', 'Nikon 55mm, f/3.5-5.6G VR lens');
-- insert into items values ('S04', 1, 'N01', 'Nikon item 1');
-- insert into items values ('S04', 2, 'N02', 'Nikon item 2');
-- insert into items values ('S04', 3, 'B01', 'car item');
-- insert into items values ('S04', 4, 'K01', 'kettle item');
-- insert into items values ('S092', 1, 'K01', 'kettle item');
-- insert into items values ('S092', 2, 'K01', 'kettle item');
-- insert into items values ('S092', 3, 'K01', 'kettle item');
-- insert into items values ('S093', 1, 'N01', 'a camera item');
-- insert into items values ('S093', 2, 'K03', 'a kettle item');
-- insert into items values ('S010', 1, 'PS02', 'play station');

insert into reviews values ('mc@gmail.com', 'tedwalsh@td.com', 3.9, 'great guy!', '2016-05-02');
insert into reviews values ('ks@gmail.com', 'tedwalsh@td.com', 4, 'great guy!', '2016-05-02');
insert into reviews values ('davood@gmail.com', 'tedwalsh@td.com', 4, 'great guy!', '2016-05-02');
insert into reviews values ('mk@abc.com', 'tedwalsh@td.com', 4.1, 'great guy!', '2016-05-02');  
insert into reviews values ('tedwalsh@td.com', 'ks@gmail.com', 4, 'great guy!', '2016-05-02');
insert into reviews values ('mc@gmail.com', 'ks@gmail.com', 4, 'great guy!', '2016-05-02');
insert into reviews values ('angels@gmail.com', 'ks@gmail.com', 4.2, 'great guy!', '2016-05-02'); 
insert into reviews values ('hm@mah.com', 'mc@gmail.com', 5, '', datetime('now','-4 years'));
insert into reviews values ('angels@gmail.com', 'mc@gmail.com', 5, '', datetime('now','-3 years'));
insert into reviews values ('mc@gmail.com', 'davood@gmail.com', 3.9, 'great guy!', '2016-05-02');
insert into reviews values ('hm@mah.com', 'davood@gmail.com', 5, '', datetime('now','-4 years'));
insert into reviews values ('angels@gmail.com', 'davood@gmail.com', 5, '', datetime('now','-3 years'));
insert into reviews values ('tedwalsh@td.com', 'davood@gmail.com', 5, 'great prof!', '2016-05-02');  
insert into reviews values ('mc@gmail.com', 'amr@yahoo.ca', 1, 'bad', '2016-05-02');
insert into reviews values ('hm@mah.com', 'amr@yahoo.ca', 1, 'slow', datetime('now','-4 years'));
insert into reviews values ('angels@gmail.com', 'amr@yahoo.ca', 1, 'tired', datetime('now','-3 years'));
insert into reviews values ('mc@gmail.com', 'amrv2@yahoo.ca', 5, 'bad', '2016-05-02');
insert into reviews values ('hm@mah.com', 'amrv2@yahoo.ca', 5, 'slow', datetime('now','-4 years'));
insert into reviews values ('angels@gmail.com', 'amrv2@yahoo.ca', 5, 'tired', datetime('now','-3 years'));
insert into reviews values ('mc@gmail.com', 'hm@mah.com', 2, 'bad', '2016-05-02');
insert into reviews values ('hm@mah.com', 'hm@mah.com', 2, 'slow', datetime('now','-4 years'));
insert into reviews values ('angels@gmail.com', 'hm@mah.com', 2, 'tired', datetime('now','-3 years'));
insert into reviews values ('tedwalsh@td.com', 'chomsky@mit.edu', 1, '!', '2016-05-02');
insert into reviews values ('angels@gmail.com', 'chomsky@mit.edu', 1, 'ok!', '2016-05-02'); 

insert into previews values (1, 'P01', 'hm@mah.com', 1, 'definitly used',  datetime('now','-6 months'));
insert into previews values (2, 'P02', 'hm@mah.com', 1, 'unused',  datetime('now','-4 months'));
insert into previews values (3, 'P03','ks@gmail.com', 3, 'great quality',  datetime('now','-5 months'));
insert into previews values (4, 'P04','ks@gmail.com', 5, 'great quality',  datetime('now','-5 months'));
insert into previews values (5, 'P02', 'mk@abc.com', 4.1, 'amazing car', datetime('now','-6 months'));
insert into previews values (6, 'P02', 'mk@abc.com', 3.8, 'amazing car', datetime('now','-5 months'));
insert into previews values (61, 'P02', 'mk@abc.com', 4.2, 'amazing car', datetime('now','-5 months'));
insert into previews values (7, 'P07', 'mk@abc.com', 5, 'a console', datetime('now','-12 months'));
insert into previews values (8, 'P08', 'mk@abc.com', 5, 'xbox+ps4?', datetime('now','-12 months'));
insert into previews values (9, 'P10', 'mk@abc.com', 4, '3rd time buying', datetime('now','-1 months'));
insert into previews values (10, 'P11', 'mk@abc.com',3.9, 'addicted', datetime('now','-1 months'));
insert into previews values (11, 'P12', 'mk@abc.com',5, 'addicted', datetime('now','-1 months'));
insert into previews values (12, 'P06', 'hm@mah.com',5, 'addicted', datetime('now','-2 months'));
insert into previews values (13, 'P02', 'chomsky@mit.edu',5, 'addicted', datetime('now','-3 months'));
