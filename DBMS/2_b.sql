mysql> create table students (roll_no int, name varchar(30), division varchar(5), branch varchar(30), city varchar(30), marks float, primary key(roll_no));
Query OK, 0 rows affected (2.72 sec)

mysql> describe students;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| roll_no  | int         | NO   | PRI | NULL    |       |
| name     | varchar(30) | YES  |     | NULL    |       |
| division | varchar(5)  | YES  |     | NULL    |       |
| branch   | varchar(30) | YES  |     | NULL    |       |
| city     | varchar(30) | YES  |     | NULL    |       |
| marks    | float       | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
6 rows in set (0.19 sec)

mysql> insert into students (roll_no, name, division, branch, city, marks)
    -> values (1, "Nandini", "TE1", "Computer", "Pune", 70),
    -> (2, "Chinmay", "TE1", "Computer", "Pune", 60),
    ->  (3, "Samarth", "TE1", "Computer", "Pune", 50),
    -> (4, "Shweta", "TE1", "Computer", "Pune", 90),
    ->  (5, "Vivek", "TE1", "Computer", "Pune", 80),
    -> (6, "Ninad", "TE1", "Computer", "Pune", 85),
    -> (7, "Vedant", "TE2", "IT", "Pune", 56),
    -> (8, "Aamod", "TE1", "Mech", "Pune", 70),
    -> (9, "Advait", "TE2", "Comp", "Mumbai", 80),
    -> (10, "Vivek", "TE1", "Entc", "Nagpur", 98);
Query OK, 10 rows affected (0.35 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> select name,city from students;
+---------+--------+
| name    | city   |
+---------+--------+
| Nandini | Pune   |
| Chinmay | Pune   |
| Samarth | Pune   |
| Shweta  | Pune   |
| Vivek   | Pune   |
| Ninad   | Pune   |
| Vedant  | Pune   |
| Aamod   | Pune   |
| Advait  | Mumbai |
| Vivek   | Nagpur |
+---------+--------+
10 rows in set (0.00 sec)

mysql> select distinct(name) from students;
+---------+
| name    |
+---------+
| Nandini |
| Chinmay |
| Samarth |
| Shweta  |
| Vivek   |
| Ninad   |
| Vedant  |
| Aamod   |
| Advait  |
+---------+
9 rows in set (0.09 sec)

mysql> select * from students;
+---------+---------+----------+----------+--------+-------+
| roll_no | name    | division | branch   | city   | marks |
+---------+---------+----------+----------+--------+-------+
|       1 | Nandini | TE1      | Computer | Pune   |    70 |
|       2 | Chinmay | TE1      | Computer | Pune   |    60 |
|       3 | Samarth | TE1      | Computer | Pune   |    50 |
|       4 | Shweta  | TE1      | Computer | Pune   |    90 |
|       5 | Vivek   | TE1      | Computer | Pune   |    80 |
|       6 | Ninad   | TE1      | Computer | Pune   |    85 |
|       7 | Vedant  | TE2      | IT       | Pune   |    56 |
|       8 | Aamod   | TE1      | Mech     | Pune   |    70 |
|       9 | Advait  | TE2      | Comp     | Mumbai |    80 |
|      10 | Vivek   | TE1      | Entc     | Nagpur |    98 |
+---------+---------+----------+----------+--------+-------+
10 rows in set (0.00 sec)

mysql> select * from students where marks>75;
+---------+--------+----------+----------+--------+-------+
| roll_no | name   | division | branch   | city   | marks |
+---------+--------+----------+----------+--------+-------+
|       4 | Shweta | TE1      | Computer | Pune   |    90 |
|       5 | Vivek  | TE1      | Computer | Pune   |    80 |
|       6 | Ninad  | TE1      | Computer | Pune   |    85 |
|       9 | Advait | TE2      | Comp     | Mumbai |    80 |
|      10 | Vivek  | TE1      | Entc     | Nagpur |    98 |
+---------+--------+----------+----------+--------+-------+
5 rows in set (0.00 sec)

mysql> select * from students where name like "S%";
+---------+---------+----------+----------+------+-------+
| roll_no | name    | division | branch   | city | marks |
+---------+---------+----------+----------+------+-------+
|       3 | Samarth | TE1      | Computer | Pune |    50 |
|       4 | Shweta  | TE1      | Computer | Pune |    90 |
+---------+---------+----------+----------+------+-------+
2 rows in set (0.03 sec)

mysql> select * from students where marks>50 and marks<60;
+---------+--------+----------+--------+------+-------+
| roll_no | name   | division | branch | city | marks |
+---------+--------+----------+--------+------+-------+
|       7 | Vedant | TE2      | IT     | Pune |    56 |
+---------+--------+----------+--------+------+-------+
1 row in set (0.00 sec)

mysql> select * from students where branch="Computer" and city="Pune";
+---------+---------+----------+----------+------+-------+
| roll_no | name    | division | branch   | city | marks |
+---------+---------+----------+----------+------+-------+
|       1 | Nandini | TE1      | Computer | Pune |    70 |
|       2 | Chinmay | TE1      | Computer | Pune |    60 |
|       3 | Samarth | TE1      | Computer | Pune |    50 |
|       4 | Shweta  | TE1      | Computer | Pune |    90 |
|       5 | Vivek   | TE1      | Computer | Pune |    80 |
|       6 | Ninad   | TE1      | Computer | Pune |    85 |
+---------+---------+----------+----------+------+-------+
6 rows in set (0.04 sec)

mysql> update students set branch="IT" where roll_no=9;
Query OK, 1 row affected (0.20 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> insert into students(roll_no, name, division, branch, city, marks)
    -> values (11, "X", "BE1", "Computer", "Pune", 75),
    -> (12, "Y", "BE2", "IT", "Mumbai", 70);
Query OK, 2 rows affected (0.17 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> delete from students where division="BE1" or division="BE2";
Query OK, 2 rows affected (0.32 sec)

mysql> create table te_students as select roll_no, name from students;
Query OK, 10 rows affected (3.25 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> select roll_no from students
    -> union
    -> select roll_no from te_students;
+---------+
| roll_no |
+---------+
|       1 |
|       2 |
|       3 |
|       4 |
|       5 |
|       6 |
|       7 |
|       8 |
|       9 |
|      10 |
+---------+
10 rows in set (0.10 sec)

mysql> select upper(name) from students;
+-------------+
| upper(name) |
+-------------+
| NANDINI     |
| CHINMAY     |
| SAMARTH     |
| SHWETA      |
| VIVEK       |
| NINAD       |
| VEDANT      |
| AAMOD       |
| ADVAIT      |
| VIVEK       |
+-------------+
10 rows in set (0.21 sec)

mysql> select bin(marks), hex(marks) from students;
+------------+------------+
| bin(marks) | hex(marks) |
+------------+------------+
| 1000110    | 46         |
| 111100     | 3C         |
| 110010     | 32         |
| 1011010    | 5A         |
| 1010000    | 50         |
| 1010101    | 55         |
| 111000     | 38         |
| 1000110    | 46         |
| 1010000    | 50         |
| 1100010    | 62         |
+------------+------------+
10 rows in set (0.10 sec)
