query_1 = "
CREATE TABLE Readers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    email VARCHAR(60) UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT true
);
"
query_2 = "
CREATE TABLE PublishingHouses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    city VARCHAR(20),
    address VARCHAR(120)
);
"
query_3 = " 
CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(60),
    price DECIMAL(5, 2),
    author VARCHAR(60),
    publishing_houses_id INT,
    FOREIGN KEY (publishing_houses_id) REFERENCES PublishingHouses(id)
);
"
query_4 = "
CREATE TABLE ReadersBooks (
    reader_id INT,
    book_id INT,
    FOREIGN KEY (reader_id) REFERENCES Readers(id),
    FOREIGN KEY (book_id) REFERENCES Books(id)
);
"
query_5 = "
SELECT * FROM Books WHERE price > 10
"
query_6 = "
INSERT INTO PublishingHouses (name, city, address)
VALUES('Super Books', 'Wilderness', '120 Main Road')
"
query_7 = "
DELETE FROM Books WHERE id = 12
"
query_8 = "
SELECT * FROM Readers
WHERE id IN (SELECT reader_id FROM ReadersBooks)
"
query_9 = "
UPDATE Readers SET is_active = false WHERE id = 2
"
query_10 = "
ALTER TABLE Readers ADD COLUMN date_of_birth DATE
"
