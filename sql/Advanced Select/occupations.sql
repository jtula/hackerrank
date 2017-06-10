select doctor, professor, singer, actor from 
  (select name, occupation ,ROW_NUMBER() over(partition by occupation order by name) as temp from occupations)
    up pivot( MAX(name) for occupation in (doctor, professor, singer, actor) ) as pvt;
