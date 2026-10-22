## Day 4 - SQL
Create Database college;
Create Table student1(
Rollno Int Primary key,
Name Varchar(50),
Marks Int Not Null,
Grade Varchar(20),
City Varchar(10)
);


Insert into student1
(Rollno,Name,Marks,Grade,City)
Values
(101,'Anil',78,'C','Pune'),
(102,'Amit',75,'A','Mumbai'),
(103,'Ajay',76,'B','Mumbai'),
(104,'Aaku',77,'A','Delhi'),
(105,'Avinash',79,'F','Delhi'),
(106,'Ayush',80,'B','Delhi');

Select*From student1;
