select case
           when grades.grade > 7 then students.name
           else null
           end,
           grades.grade,
           students.marks
        FROM students, grades where students.marks >= grades.min_mark and students.marks <= grades.max_mark   
            ORDER BY grades.grade desc, students.name asc;
