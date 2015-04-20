1. Show all playerids and salaries with a salary in the year 1985 above 500k.

    ```sql
    SELECT *
    FROM salaries
    WHERE yearid = 1985
        AND salary > 500000
    ```

2. Show the teams for each year that had a rank of 1.

    ```sql
    SELECT
        yearid,
        teamid
    FROM teams
    WHERE rank = 1
    ```

3. How many schools are in schoolstate of CT?

    ```sql
    SELECT
        COUNT(*)
    FROM schools
    WHERE schoolstate = 'CT'
    ```

4. How many schools are there in each state?

    ```sql
    SELECT
        schoolstate,
        COUNT(*)
    FROM schools
    GROUP BY schoolstate
    ```

5. What was the total spend on salaries by each team, each year?

    ```sql
    SELECT
        yearid,
        teamid,
        SUM(salary)
    FROM salaries
    GROUP BY 1, 2
    ORDER BY 1, 2 -- easier to read
    ```

6. Find all of the salaries of shortstops (fieldings, pos) for the year 2012.

    ```sql
    SELECT
        f.playerid,
        s.salary
    FROM fielding f
    INNER JOIN salaries s ON s.playerid = f.playerid
        AND s.yearid = f.yearid
    WHERE f.pos = 'SS'
        AND s.yearid = 2012
    ```

7. What is the first and last year played for each player?

    ```sql
    SELECT
        playerid,
        MIN(yearid),
        MAX(yearid)
    FROM salaries
    GROUP BY 1
    ```

8. Who has played the most all star games?

    ```sql
    SELECT
        playerid,
        COUNT(*)
    FROM allstarfull
    GROUP BY 1
    ```

9. Which school has generated the most distinct players?

    ```sql
    SELECT
        schoolid,
        COUNT(DISTINCT playerid),
    FROM collegeplaying
    GROUP BY 1
    ```

10. Which school has generated the most expensive players? (expensive defined by their first year's salary).

    ```sql
    SELECT *
    FROM (SELECT DISTINCT
            b.playerid,
            b.schoolid,
            rank() OVER (PARTITION BY s.playerid ORDER BY s.yearid asc) "year_played",
            s.salary
        FROM salaries s
        INNER JOIN collegeplaying b on b.playerid = s.playerid) a
    WHERE year_played = 1
    ORDER BY 4 desc
    ```

11. Show the 5 most expensive salaries for each team in the year 2014.

    ```sql
    SELECT *
    FROM (SELECT DISTINCT
            playerid,
            teamid,
            yearid,
            rank() OVER (PARTITION BY teamid, yearid ORDER BY salary desc) "ordered_salary",
            salary
        FROM salaries
        WHERE yearid = 2014) a
    WHERE ordered_salary < 6
    ORDER BY 2, 5 desc
    ```

12. Partition the average salaries by team and year, against year. Find players that were paid more than 1 standard deviation above the average salary for that team and year. Show a count by playerid.

    ```sql
    SELECT *
    FROM (SELECT DISTINCT
            playerid,
            teamid,
            yearid,
            AVG(LOG(salary+1)) OVER (PARTITION BY teamid, yearid) "avg_salary",
            STDDEV(LOG(salary+1)) OVER (PARTITION BY teamid, yearid) "std_salary",
            LOG(salary+1) "salary"
        FROM salaries) a
    WHERE avg_salary + std_salary < salary
    ORDER BY 3, 2, 6 desc;

    SELECT *
    FROM (SELECT DISTINCT
            playerid,
            teamid,
            yearid,
            AVG(salary) OVER (PARTITION BY teamid, yearid) "avg_salary",
            STDDEV(salary) OVER (PARTITION BY teamid, yearid) "std_salary",
            salary
        FROM salaries) a
    WHERE avg_salary + std_salary < salary
    ORDER BY 3, 2, 6 desc;
    ```
13. Calculate the win percentage. convert w and g into numerics (floats) to do so. (w::numeric, for example)

    ```sql
    SELECT
        teamid,
        yearid,
        g,
        w,
        ROUND(w::numeric / g::numeric * 100, 2) "win_percentage"
    FROM teams
    ORDER BY 2, 5 desc
    ```
14. rank() the total spend by team each year against their actual rank that year. Is there a correlation of spend to performance?

    ```sql
    -- teams.rank is by league and division, so use that for the most accurate values.
    SELECT
        t.lgid,
        t.divid,
        t.teamid,
        t.yearid,
        t.rank,
        rank() OVER (PARTITION BY t.yearid, t.lgid, divid ORDER BY a.spend DESC) "spend_rank",
        a.spend
    FROM teams t
    INNER JOIN (SELECT
            s.teamid,
            s.yearid,
            SUM(salary) "spend"
        FROM salaries s
        INNER JOIN teams t ON t.yearid = s.yearid AND t.teamid = s.teamid
        GROUP BY 1, 2) a ON t.teamid = a.teamid AND t.yearid = a.yearid
    ORDER BY 4, 1, 2, 5;
    ```