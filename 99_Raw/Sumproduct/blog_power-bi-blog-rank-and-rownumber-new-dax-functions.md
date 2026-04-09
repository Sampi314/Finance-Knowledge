# Power BI Blog: RANK and ROWNUMBER (New DAX Functions)

**Source:** https://sumproduct.com/blog/power-bi-blog-rank-and-rownumber-new-dax-functions/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: RANK and ROWNUMBER (New DAX Functions)

*   July 12, 2023

Power BI Blog: RANK and ROWNUMBER (New DAX Functions)
=====================================================

Power BI Blog: RANK and ROWNUMBER (New DAX Functions)
=====================================================

13 July 2023

_Welcome back to this week’s edition of the Power BI blog series. This week, we inspect two new DAX functions, **RANK** and **ROWNUMBER**._

Two new functions have been added to the DAX / Power BI repertoire that should assist when calculating rankings: **RANK** and **ROWNUMBER** are joining the DAX ranks.

These functions return a number indicating the rank for the current context within the specified partition, sorted by the specified order. The difference between **RANK** and **ROWNUMBER** is that if there is a tie (_i.e_. two rows would get the same rank assigned) **ROWNUMBER** will return an error, whereas **RANK** will just assign the same **RANK** multiple times. You should note that returning an error is a last resort; **ROWNUMBER** will try to avoid doing that by finding the least number of additional columns required to uniquely identify every row and append these new columns to the **ORDERBY** clause. Only after it is unable to uniquely identify every row, **ROWNUMBER** will return an error.

These functions rely on the **ORDERBY**and **PARTITIONBY** functions.

In the following example, we have a list of customers and their birth dates. I have added the following measures to my model:

**RankByBirthDateSkip = RANK(SKIP,  
ALLSELECTED(DimCustomer), ORDERBY(DimCustomer\[BirthDate\]))**

**RankByBirthDateDense = RANK(DENSE,  
ALLSELECTED(DimCustomer), ORDERBY(DimCustomer\[BirthDate\]))**

**RowNumberByBirthDate =  
ROWNUMBER(ALLSELECTED(DimCustomer), ORDERBY(DimCustomer\[BirthDate\]))**

This is the first part of the output:

![](<Base64-Image-Removed>)

All measures here return the same result. However, for customers that share a birthday, the results are different:

![](<Base64-Image-Removed>)

Notice how both Donald Garcia and Kayla Garcia are both on the same date. Using **RANK** with the ties parameter set to **SKIP** (the default) assigns them a rank of 41. The same happens when using **RANK** with the ties parameter set to **DENSE**. However, notice that the next customer receives a different rank (43 when the ties parameter is set to **SKIP** and 42 when set to **DENSE**). By contrast, **ROWNUMBER** gives Donald and Kayla an unique rank (41 and 42) as it expands the **ORDERBY** clause to try to unique identify these customers and is successful in doing so.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-rank-and-rownumber-new-dax-functions/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-rank-and-rownumber-new-dax-functions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-rank-and-rownumber-new-dax-functions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-rank-and-rownumber-new-dax-functions/#0)

[](https://sumproduct.com/blog/power-bi-blog-rank-and-rownumber-new-dax-functions/#0 "close")

top