select
  case
    when a + b <= c then "Not A Triangle"
    when a = b AND b = c then "Equilateral"   
    when a = b AND a <> c then "Isosceles"
    when a = c AND a <> b then "Isosceles"
    when b = c AND a <> b then "Isosceles"
    else "Scalene"
  end
from triangles
