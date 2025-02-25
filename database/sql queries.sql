CREATE DATABASE IF NOT EXISTS literacy_data;
USE literacy_data;

-- Create table for population data
CREATE TABLE IF NOT EXISTS population_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    area_name VARCHAR(255),
    total_rural_urban VARCHAR(50),
    age_group VARCHAR(50),
    total_population INT,
    male_population INT,
    female_population INT,
    total_population_attending_edu_inst INT,
    male_population_attending_edu_inst INT,
    female_population_attending_edu_inst INT,
    total_literates INT,
    male_literates INT,
    female_literates INT
);

-- Load data from CSV file
SET GLOBAL local_infile = 1;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/hp new one.csv'
INTO TABLE population_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Check data
SHOW COLUMNS FROM population_data;
SELECT COUNT(*) FROM population_data;
SELECT * FROM population_data LIMIT 10;
SELECT DISTINCT area_name FROM population_data;

-- Remove duplicates
DELETE FROM population_data 
WHERE id NOT IN (SELECT MIN(id) FROM population_data GROUP BY area_name, age_group);

-- Handle missing values
UPDATE population_data 
SET total_population = COALESCE(total_population, 0);

-- Basic analysis
SELECT area_name, (total_literates / total_population) * 100 AS literacy_rate
FROM population_data 
WHERE age_group = 'All ages';

SELECT area_name, 
       (male_literates / male_population) * 100 AS male_literacy_rate,
       (female_literates / female_population) * 100 AS female_literacy_rate
FROM population_data 
WHERE age_group = 'All ages';

SELECT area_name, (total_literates / total_population) * 100 AS literacy_rate
FROM population_data 
WHERE (total_literates / total_population) * 100 < 50;

-- Export cleaned data
SELECT * FROM population_data 
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cleaned_data.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
































