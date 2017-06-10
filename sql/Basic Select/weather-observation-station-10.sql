#MSSQL
select distinct city from station where city like '%[^aeiou]' order by city asc;
