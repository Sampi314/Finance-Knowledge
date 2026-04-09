# The A to Z of DAX Functions – GENERATEALL

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-generateall/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – GENERATEALL

*   January 30, 2024

The A to Z of DAX Functions – GENERATEALL
=========================================

Power Pivot Principles: The A to Z of DAX Functions – GENERATEALL
=================================================================

30 January 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **GENERATEALL**._

**_The _GENERATEALL_ function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/3cb2969a68570a14750a197b81177899.jpg)

The _**GENERATEALL**_ functionis one of the Table manipulation functions which return a table with the Cartesian product between each row in **table1** and the table that results from evaluating **table2** in the context of the current row of **table1**. It has the following syntax:

_**GENERATEALL**_**(table1, table2)**

where:

*   **table1, table2:** these are required and can be any DAX expressions that return a table.

The functions **GENERATEALL** and [**GENERATE**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-generate)
 are very similar and for more information about the latter we recommend our earlier [blog article](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-generate)
 on **GENERATE**. It should be noted that:

*   if **table2** evaluates to an empty table for the current row of **table1**, the output table of the **GENERATEALL** function will contain the current row of **table1**, with _null_ values in the cells corresponding to **table2**; while the [**GENERATE**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-generate)
     function will not include the current row from **table1**
*   all column names from **table1**and **table2** must be different else an error is returned
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s consider the following example.

![](<Base64-Image-Removed>)

**DEFINE**

    **VAR Dates = UNION(**

        **ROW(“Start”, DATE(2019, 1,  
1), “End”, DATE(2019, 1, 3)),**

        **ROW(“Start”, DATE(2019, 2,  
20), “End”, DATE(2019, 2, 22))**

    **)**

**EVALUATE**

    **Dates**

We’ve created a short table **Dates** with two \[2\] columns **Start** and **End** containing date values.

![](<Base64-Image-Removed>)

Then we use table **Dates** as the **table1** argument and use the [**DATESBETWEEN**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-datesbetween)
 function to generate a **table2** argument:

**EVALUATE**

    **GENERATEALL(**

        **Dates,**

        **DATESBETWEEN(‘Calendar'\[Date\], \[Start\],  
\[End\])**

    **)**

The function [**DATESBETWEEN**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-datesbetween)
 returns a single-column table containing dates between **Start** and **End**, for each row of table **Dates**. Then the **GENERATEALL** function cross-joins that with the first table **Dates**:

![](<Base64-Image-Removed>)

The above functionality is common between the two \[2\] functions **GENERATEALL** and [**GENERATE**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-generate)
. Now let’s consider another example. We can change the first table slightly to generate blank values:

**DEFINE**

    **VAR Dates2 = UNION(**

        **ROW(“Start”, DATE(2019, 1,  
1), “End”, DATE(2019, 1, 3)),**

        **ROW(“Start”, DATE(2019, 2,  
20), “End”, DATE(2019, 2, 18))**

    **)**

Now the second row of the table **Dates2** contains an end date earlier than the start date, so that the [**DATESBETWEEN**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-datesbetween)
 function will generate an empty table for that row.

**EVALUATE**

    **GENERATEALL(**

        **Dates2,**

        **DATESBETWEEN(‘Calendar'\[Date\], \[Start\],  
\[End\])**

    **)**

The above **DAX** statement returns the following table, including the blank value:

![](<Base64-Image-Removed>)

In contrast, if we employ the [**GENERATE**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-generate)
 function:

**EVALUATE**

    **GENERATE(**

        **Dates2,**

        **DATESBETWEEN(‘Calendar'\[Date\], \[Start\],  
\[End\])**

    **)**

the blank value will be excluded:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-generateall/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-generateall/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-generateall/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-generateall/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-generateall/#0 "close")

top