CREATE TABLE match_stats (
    id SERIAL PRIMARY KEY,
    match_id VARCHAR(50),
    player_name VARCHAR(100),
    runs INTEGER,
    balls INTEGER,
    fours INTEGER,
    sixes INTEGER,
    strike_rate NUMERIC(5, 2),
    dismissal VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM match_stats;

------------Top 3 Run Scorers-------
SELECT player_name, runs 
FROM match_stats 
ORDER BY runs DESC 
LIMIT 3;

----------Team Strike Rate Analysis------
SELECT player_name, strike_rate 
FROM match_stats 
WHERE runs > 10;

-- This removes all existing data but keeps the table structure
TRUNCATE TABLE match_stats;
TRUNCATE TABLE player_stats;