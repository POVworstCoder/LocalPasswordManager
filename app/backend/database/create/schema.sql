-- Create the account table if it doesn't exist
CREATE TABLE IF NOT EXISTS account (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    site_url TEXT,
    password TEXT NOT NULL
);

-- Insert test data into the account table
INSERT INTO account (username, email, site_url, password) VALUES
    ('testuser1', 'testuser1@example.com', 'https://example.com', 'password123'),
    ('testuser2', 'testuser2@example.com', 'https://example2.com', 'mypassword456'),
    ('testuser3', 'testuser3@example.com', 'https://example3.com', 'qwerty789'),
    ('testuser4', 'testuser4@example.com', 'https://example4.com', '12345678'),
    ('testuser5', 'testuser5@example.com', 'https://example5.com', 'securepass001');
