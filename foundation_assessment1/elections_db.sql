CREATE DATABASE Democracy;

USE Democracy;

CREATE TABLE Elections (
    RecordId INT NOT NULL,
    Candidate VARCHAR(50) NOT NULL,
    Votes INT NOT NULL,
    District VARCHAR(50) NOT NULL
);

-- Now populating the Elections table
INSERT INTO Elections
(RecordId, Candidate, Votes, District)
VALUES
(1, 'Mr Grumpy', 10, 'Green Area'),
(2, 'Mr Happy', 17, 'Green Area'),
(3, 'Mr Funny', 18, 'Green Area'),
(4, 'Mr Tickles', 2, 'Green Area'),
(5, 'Mr Grumpy', 5, 'Orange Area'),
(6, 'Mr Happy', 20, 'Orange Area'),
(7, 'Mr Funny', 4, 'Orange Area'),
(8, 'Mr Tickles', 15, 'Orange Area'),
(9, 'Mr Grumpy', 22, 'Blue Area'),
(10, 'Mr Happy', 25, 'Blue Area'),
(11, 'Mr Funny', 34, 'Blue Area'),
(12, 'Mr Tickles', 8, 'Blue Area'),
(13, 'Mr Grumpy', 9, 'Pink Area'),
(14, 'Mr Happy', 12, 'Pink Area'),
(15, 'Mr Funny', 6, 'Pink Area'),
(16, 'Mr Tickles', 17, 'Pink Area');
