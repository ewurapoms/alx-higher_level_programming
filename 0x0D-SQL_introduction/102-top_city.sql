-- Lists the cities with the highest average
SELECT `city`, AVG(`value`) AS `average_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `average_temp` DESC
LIMIT 3;
