select ROUND(ABS(MIN(lat_n) - MIN(long_w)) + ABS(MAX(lat_n) - MAX(long_w)),4) from station;

