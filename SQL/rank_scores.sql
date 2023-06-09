/*
 Table: Scores
 
 +-------------+---------+
 | Column Name | Type    |
 +-------------+---------+
 | id          | int     |
 | score       | decimal |
 +-------------+---------+
 id is the primary key for this table.
 Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
 
 
 Write an SQL query to rank the scores. The ranking should be calculated according to the following rules:
 
 The scores should be ranked from the highest to the lowest.
 If there is a tie between two scores, both should have the same ranking.
 After a tie, the next ranking number should be the next consecutive integer value.
 In other words, there should be no holes between ranks.
 Return the result table ordered by score in descending order.
 
 The query result format is in the following example.
 
 
 Example 1:
 
 Input: 
 Scores table:
 +----+-------+
 | id | score |
 +----+-------+
 | 1  | 3.50  |
 | 2  | 3.65  |
 | 3  | 4.00  |
 | 4  | 3.85  |
 | 5  | 4.00  |
 | 6  | 3.65  |
 +----+-------+
 Output: 
 +-------+------+
 | score | rank |
 +-------+------+
 | 4.00  | 1    |
 | 4.00  | 1    |
 | 3.85  | 2    |
 | 3.65  | 3    |
 | 3.65  | 3    |
 | 3.50  | 4    |
 +-------+------+
 
 */
/*
 (MySQL)
 Step:
 1. SELECT DISTINCT scores, For example: 1,1,2,2,3,3 -> 1,2,3
 2. generate rank for the scores (named `rank`).
 3. JOIN it with the origin table.
 4. order by score. 
 */
WITH
  DistinctScores as (
    SELECT
      DISTINCT score
    FROM
      Scores
  ),
  RankScores as (
    SELECT
      score,
      RANK() OVER (
        ORDER BY
          score DESC
      ) AS `rank`
    FROM
      DistinctScores
  )
SELECT
  Scores.score,
  RankScores.rank
FROM
  Scores
  JOIN RankScores ON Scores.score = RankScores.score
ORDER BY
  Scores.score DESC