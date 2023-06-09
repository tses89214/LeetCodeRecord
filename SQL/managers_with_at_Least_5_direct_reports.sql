/*
 Table: Employee
 
 +-------------+---------+
 | Column Name | Type    |
 +-------------+---------+
 | id          | int     |
 | name        | varchar |
 | department  | varchar |
 | managerId   | int     |
 +-------------+---------+
 id is the primary key column for this table.
 Each row of this table indicates the name of an employee, their department, and the id of their manager.
 If managerId is null, then the employee does not have a manager.
 No employee will be the manager of themself.
 
 
 Write an SQL query to report the managers with at least five direct reports.
 
 Return the result table in any order.
 
 The query result format is in the following example.
 
 
 
 Example 1:
 
 Input: 
 Employee table:
 +-----+-------+------------+-----------+
 | id  | name  | department | managerId |
 +-----+-------+------------+-----------+
 | 101 | John  | A          | None      |
 | 102 | Dan   | A          | 101       |
 | 103 | James | A          | 101       |
 | 104 | Amy   | A          | 101       |
 | 105 | Anne  | A          | 101       |
 | 106 | Ron   | B          | 101       |
 +-----+-------+------------+-----------+
 Output: 
 +------+
 | name |
 +------+
 | John |
 +------+
 */
WITH
  MANAGER_ID_MORE_THAN_FIVE as (
    select
      managerId
    from
      Employee
    group by
      managerId
    HAVING
      COUNT(*) >= 5
  )
select
  Employee.name
FROM
  Employee
  INNER JOIN MANAGER_ID_MORE_THAN_FIVE ON Employee.id = MANAGER_ID_MORE_THAN_FIVE.managerId