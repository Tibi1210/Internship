
CREATE TABLE "Users" (
    "User ID" int,
    "Employer Number" int,
    "Creation Date" date,
    "Username" varchar(255),
    "Password" varchar(255),
    "Level" int,
    "Active" boolean
);

CREATE TABLE "Courses" (
    "Course ID" int,
    "Course Name" varchar(255),
    "Platform ID" int,
    "Duration" int,
    "Creation Date" date,
    "Tags" varchar(255),
    "Photo" varchar(255),
    "Active" boolean
);

CREATE TABLE "Platforms" (
    "Platform ID" int,
    "Platform Name" varchar(255),
    "Hyperlink Path" varchar(255),
    "Active" boolean
);

CREATE TABLE "Reviews" (
    "User ID" int,
    "Course ID" int,
    "Feedback" varchar(255), 
    "Like/Dislike" boolean,
    "Ranking Score (out of 5)" int,
    "Active" boolean
);

CREATE TABLE "Photos" (
    "Course ID" int,
    "Platform ID" int,
    "Image Object" varchar(255),
    "Active" boolean
);

CREATE TABLE "Certifications" (
    "Certification ID" int,
    "User ID" int,
    "Course ID" int,
    "Completion Duration" int,
    "Completion Date" date,
    "Active" boolean
);

CREATE TABLE "Ongoing Trainings" (
    "Training ID" int,
    "User ID" int,
    "Course ID" int,
    "Status" varchar(255),
    "Completion Percentage" int,
    "Start Date" date,
    "Finish Date" date,
    "Last Updated" date,
    "Active" boolean
);