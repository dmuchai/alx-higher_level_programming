-- displays the top 3 of cities temp during July and Aug ordered by temp
SELECT `city`, 
       ROUND(AVG(`value`), 4) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
