-- List all cities of California found in `hbtn_0d_usa`
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
