CREATE TABLE "Employer" (
	"Employer_ID"	INTEGER,
	"FullName"	TEXT,
	"JoiningDate"	TEXT,
	"CurrentPosition"	TEXT,
	"Department"	TEXT,
	PRIMARY KEY("Employer_ID")
);

CREATE TABLE "Services" (
	"Software_ID"	INTEGER,
	"Name"	TEXT,
	"Category"	TEXT,
	"Size"	INTEGER,
	"NumberOfInstallments"	TEXT,
	PRIMARY KEY("Software_ID")
);


CREATE TABLE "Software_Requests" (
	"Employer_ID"	INTEGER,
	"Software_ID"	INTEGER,
	"RequestStartDate"	TEXT,
	"RequestCloseDate"	TEXT,
	"Status"	TEXT
);



INSERT INTO Employer (Employer_ID,FullName,JoiningDate,CurrentPosition,Department) VALUES (1,'John','2022-jun-20','Big Guy', 'Software and Data');

INSERT INTO Services (Software_ID,Name,Category,Size,NumberOfInstallments) VALUES (1,'Softwaareee','A',12345, 1);

INSERT INTO Software_Requests (Employer_ID,Software_ID,RequestStartDate,RequestCloseDate,Status) VALUES (1,1,'2022-jun-21','2022-jun-22','done');
