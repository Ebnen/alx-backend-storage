-- This script creates a table called users with the following columns:
-- id: an integer that auto-increments and is the primary key
-- email: a string that cannot be null and must be unique
-- name: a string that can be null
-- The UNIQUE constraint on the email column ensures that no two users can have the same email address.
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
