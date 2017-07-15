select h.hacker_id, h.name
from hackers h, difficulty d, challenges c, submissions s  
where h.hacker_id=s.hacker_id and c.challenge_id=s.challenge_id and d.difficulty_level=c.difficulty_level and s.score=d.score and c.difficulty_level=d.difficulty_level
group by h.hacker_id, h.name
having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, s.hacker_id asc
