-- Sample SQL table structure
CREATE TABLE solar_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    voltage FLOAT,
    current FLOAT,
    temperature FLOAT,
    light_intensity FLOAT
);
