select CONVERT(INT, CEILING(AVG(CONVERT(FLOAT, salary)) - AVG(CONVERT(FLOAT, REPLACE(CONVERT(CHAR, salary),'0',''))))) from employees;
