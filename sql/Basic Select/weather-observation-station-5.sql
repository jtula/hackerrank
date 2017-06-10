#MySQL
select city, CHAR_LENGTH(city) as L1 FROM station order by L1 asc limit 1;
SELECT city, CHAR_LENGTH(city) as L2 FROM station order by L2 desc limit 1;
