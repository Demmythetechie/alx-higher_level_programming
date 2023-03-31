-- This is a subquery that list cities in a particular state using
-- a subquery that gets the id of state where the name is California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California');
