select ROUND(hh.lat_n,4) AS mediam from station hh, station lh group by hh.lat_n having SUM(SIGN(1 - SIGN(lh.lat_n - hh.lat_n))) = (COUNT(*) + 1) / 2;
