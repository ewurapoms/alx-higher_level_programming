-- Lists all California cities in the hbtn_0d_usa database
-- Results are ordered by ascending cities.id
SELECT c.id, c.name
FROM cities c, states s
WHERE c.state_id = s.id AND s.name = 'California'
ORDER BY c.id;
