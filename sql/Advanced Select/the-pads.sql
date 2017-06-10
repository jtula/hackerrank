select CONCAT(name, '(', substring(occupation, 1, 1), ')') from occupations order by name asc;
select CONCAT('There are total ', COUNT(*), ' ', LOWER(occupation), 's.') FROM occupations group by occupation  order by COUNT(*);
