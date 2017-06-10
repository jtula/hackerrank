select bst.n, case
                when P is NULL then 'Root' 
                when (select COUNT(*) from bst as b where b.p = bst.n) = 0 then 'Leaf'
                else 'Inner' 
              end
 from bst order by bst.n
