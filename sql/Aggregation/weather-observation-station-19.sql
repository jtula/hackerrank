select ROUND(SQRT(POW(MIN(lat_n) - MIN(long_w),2) + POW(MAX(lat_n) - MAX(long_w),2)),4) from station;
