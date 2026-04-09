# Power Query: Joining Grades

**Source:** https://sumproduct.com/blog/power-query-joining-grades/

---

[Home](https://sumproduct.com/)

\> Power Query: Joining Grades

*   August 14, 2018

Power Query: Joining Grades
===========================

Power Query: Joining Grades
===========================

15 August 2018

_Welcome to our Power Query blog. This week, I look at [last week’s](https://sumproduct.com/blog/power-query-upgrading-grades/)
 problem again, but this time I translate numbers to letters in multiple columns by joining tables._

I (still) have the exam results for some children who were lucky(!) enough to take their exams when the system was in the middle of changing from letters to numbers. I want to replace the numbers with text so that I can see everything in the same format – this time I have two tables – I have created a table of the current numeric grades and their letter equivalent:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-585.jpg)

I create a query ‘From Table’ in the ‘Get & Transform’ section of the ‘Data’ tab. I begin by creating a query for my smaller numeric and letter equivalents table.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-605.jpg)

On the ‘Close & Load’ dropdown I choose to ‘Close & Load To…’ so that I can create a ‘Connection Only’ query for this table, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-557.jpg)

I can now create a query for my list of grades.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-506.jpg)

From within my ‘Grades List’ query, I can choose to ‘Merge Queries’ from the ‘Combine’ section of the ‘Home’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-421.jpg)

I have chosen a ‘Left Outer’ join as I want to keep my original ‘Grades List’ query and add the letter equivalents. I join the **_English Language_** and the **_Number Grade_** columns.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-361.jpg)

The merge has given me the letter equivalents for my **_English Language_** column: the first entry shows that the first grade in the table 8 corresponds to A\*/A. I can expand the Grade Equivalents column.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-299.jpg)

I only want the letter grade, so I expand the column and rename the letter grade to show that it corresponds to the **_English Language_** column.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-254.jpg)

Now I have my **_Eng Lang Letter Grade_** column, I repeat the merge process for the **_English Language_** and **_Mathematics_** columns.

![](<Base64-Image-Removed>)

I have all my equivalent grades. I ‘Close & Load’ my query to a new worksheet.

![](<Base64-Image-Removed>)

I can also handle the issue of the examination board adding a level 10 to the grades and altering the boundaries.

![](<Base64-Image-Removed>)

If I update, my ‘Grades List’ query is refreshed, and I see that the grades equivalents have changed for 9, 8 and 7.

![](<Base64-Image-Removed>)

There is yet another way to approach this task, and I’ll look at another method next time which combines replacing data with using the equivalents table.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-joining-grades/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-joining-grades/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-joining-grades/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-joining-grades/#0)

[](https://sumproduct.com/blog/power-query-joining-grades/#0 "close")

top