--1.
SELECT artists.Name AS 'Artist Name', IFNULL(albums.Title,'No Album') AS 'Album Name' 
FROM artists
LEFT JOIN albums
ON artists.ArtistId=albums.ArtistId
ORDER BY artists.Name;

--2.
SELECT artists.Name AS 'Artist Name', albums.Title AS 'Album Name' 
FROM artists
INNER JOIN albums
ON artists.ArtistId=albums.ArtistId
ORDER BY albums.Title DESC;

--3.
SELECT artists.Name AS 'Artist Name'
FROM artists
LEFT JOIN albums
ON artists.ArtistId=albums.ArtistId
WHERE albums.ArtistId IS NULL
ORDER BY artists.Name;

--4.
SELECT artists.Name AS 'Artist Name', COUNT(albums.Title) AS 'No of albums' 
FROM artists
LEFT JOIN albums
ON artists.ArtistId=albums.ArtistId
GROUP BY artists.Name
ORDER BY COUNT(albums.Title) DESC, artists.Name ASC;

--5.
SELECT artists.Name AS 'Artist Name', COUNT(albums.Title) AS 'No of albums' 
FROM artists
LEFT JOIN albums
ON artists.ArtistId=albums.ArtistId
GROUP BY artists.Name
HAVING COUNT(albums.Title)>10
ORDER BY COUNT(albums.Title) DESC, artists.Name ASC;

--6.
SELECT artists.Name AS 'Artist Name', COUNT(albums.Title) AS 'No of albums' 
FROM artists
LEFT JOIN albums
ON artists.ArtistId=albums.ArtistId
GROUP BY artists.Name
ORDER BY COUNT(albums.Title) DESC
LIMIT 3;

--7.
SELECT artists.Name AS 'Artist Name', albums.Title AS 'Album Name', tracks.Name AS 'Track'
FROM artists
WHERE artists.ArtistId=albums.ArtistId AND albums.AlbumId=tracks.AlbumId
ORDER BY tracks.TrackId; 

--8.
SELECT EmployeeId AS 'Employee Id', FirstName AS 'Employee Name', Title AS 'Employee Title', ReportsTo AS 'Manager Id'
FROM employees

--9.
CREATE VIEW 'top_employees' AS
SELECT employees.EmployeeId AS 'emp_Id', employees.FirstName AS 'emp_Name', COUNT(customers.CustomerId) AS 'cust_count'
FROM employees
LEFT JOIN customers
ON customers.SupportRepId=employees.EmployeeId
GROUP BY employees.EmployeeId

--10.
INSERT INTO media_types (MediaTypeId,Name) VALUES (6,'MP3')

CREATE TRIGGER mp3
BEFORE INSERT
ON tracks
BEGIN
    SELECT CASE WHEN NEW.MediaTypeId = 6 THEN 
        RAISE(ABORT, "Cant be mp3") 
    END;
END;

--11.
CREATE TABLE tracks_audi_log (
    operation TEXT,
    datetime  TEXT,
    username  TEXT,
    old_value TIME,
    new_value TEXT
);

CREATE TRIGGER 'tracks_audit'
AFTER UPDATE
ON tracks
WHEN old.Name <> new.Name
BEGIN
INSERT INTO tracks_audit_logs (operation,datetime,username,old_value,new_value)
VALUES ('UPDATE',Date('now'),'sqlite user',old.Name,new.Name);
END;