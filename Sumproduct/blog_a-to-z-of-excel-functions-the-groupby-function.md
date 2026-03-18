# A to Z of Excel Functions: The GROUPBY Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-groupby-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The GROUPBY Function

*   December 3, 2023

A to Z of Excel Functions: The GROUPBY Function
===============================================

A to Z of Excel Functions: The GROUPBY Function
===============================================

4 December 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **GROUPBY** function._

**The GROUPBY function**

The **GROUPBY** function allows you to create a summary of your data formulaically. It supports grouping along one axis and aggregating the associated values. For instance, if you had a table of sales data, you might generate a summary of sales by year, or by salesperson, or by category, or by…

In essence, it allows you to group, aggregate, sort and filter data based upon the fields you specify.

The syntax of the **GROUPBY** function is given by:

**GROUPBY(row\_fields,  
values, function, \[field\_headers\], \[total\_depth\], \[sort\_order\], \[filter\_array\])**

It has the following arguments:

*   **row\_fields:** this is required, and represents a column-oriented array or range that contains the values which are used to group rows and generate row headers. The array or range may contain multiple columns. If so, the output will have multiple row group levels

*   **values:** this is also required, and denotes a column-oriented array or range of the data to aggregate. The array or range may contain multiple columns. If so, the output will have multiple aggregations

*   **function:** also required, this is an explicit or eta reduced lambda (_e.g._ **[SUM](https://www.sumproduct.com/thought/sum-things-to-consider)
    **, **[PERCENTOF](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-percentof-function)
    **, **[AVERAGE](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-average-function)
    **, **[COUNT](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-count-function)
    **) that is used to aggregate **values**. A vector of lambdas may be provided. If so, the output will have multiple aggregations. The orientation of the vector will determine whether they are laid out row- or column-wise

*   **field\_headers:** this and the remaining arguments are all optional. This represents a number that specifies whether the **row\_fields** and **values** have headers and whether field headers should be returned in the results. The possible values are:
    
    *   **Missing:** Automatic
    *   **0:** No
    *   **1:** Yes and don’t show
    *   **2:** No but generate
    *   **3:** Yes and show
    
    It should be noted that “Automatic” assumes the data contains headers based upon the **values** argument. If the first value is text and the second value is a number, then the data is assumed to have headers. Fields headers are shown if there are multiple row or column group levels
    

*   **total\_depth:** this optional argument determines whether the row headers should contain totals. The possible values are:
    
    *   **Missing**: Automatic, with grand totals and, where possible, subtotals
    *   **0:** No Totals
    *   ****1:****Grand Totals
    *   ****2:****Grand and Subtotals
    *   ****\-1:****Grand Totals at Top
    *   ****\-2:****Grand and Subtotals at Top
    
    It should be noted that for subtotals, fields must have at least two \[2\] columns. Numbers greater than two \[2\] are supported provided there are sufficient columns
    

*   **sort\_order:** again optional, this argument denotes a number indicating how rows should be sorted. Numbers correspond with the columns in **row\_fields** followed by the columns in **values**. If the number is negative, the rows are sorted in descending / reverse order. A vector of numbers may be provided when sorting based upon only **row\_fields  
    **

*   **filter\_array:** the final optional argument, this represents a column-oriented one-dimensional array of Boolean values \[1, 0\] that indicate whether the corresponding row of data should be considered. It should be noted that the length of the array must match the length of **row\_fields**.

To show how **GROUPBY** works, consider the following Excel Table:

![](<Base64-Image-Removed>)

I have converted this data table into an Excel Table by selecting all the data and using **Insert -> Table** (**CTRL + T**) and calling the resultant Table **tbl**. Look, it’s late as I write this and I have no imagination, OK!?

I can summarise my Table very simply using the formula

**\=GROUPBY(tbl\[Category\],tbl\[Sales\],SUM)**

![](<Base64-Image-Removed>)

How easy is that!? Essentially, I am summing the sales (using the eta lambda **SUM**) by the **Category** field.

If you want to aggregate by more than one **row\_field**, as stated above, this is possible. One way is to use **[HSTACK](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-hstack-function)
**:

**\=GROUPBY(HSTACK(tbl\[Year\],tbl\[Category\]),tbl\[Sales\],SUM)**

![](<Base64-Image-Removed>)

This simply combines the **Year** and **Category** fields in the **tbl** Table, and then sums **Sales** across them. However, I think I prefer the **[CHOOSECOLS](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-choosecols-function)
**approach:

**\=GROUPBY(CHOOSECOLS(tbl,1,2),tbl\[Sales\],SUM)**

![](<Base64-Image-Removed>)

Here, the idea is that I shall **SUM Sales** by columns 1 (**Year**) and 2 (**Category**) of the **tbl** Table. This might not seem as clear as the **HSTACK** alternative at first glance as you have to refer to the Table to identify what the columns are. However, stick with me. Let me make the formula more complex:

**\=GROUPBY(CHOOSECOLS(tbl,MATCH(F$12,tbl\[#Headers\],0),  
MATCH(G$12,tbl\[#Headers\],0)),tbl\[Sales\],SUM)**

![](<Base64-Image-Removed>)

Looks horrible, yes? I have replaced the values 1 and 2 in the previous formula with

**MATCH(F$12,tbl\[#Headers\],0)**

and

**MATCH(G$12,tbl\[#Headers\],0)**

which return the positions in the **Headers** row of the Table **tbl**. Now, this may seem overkill but consider the following image:

![](<Base64-Image-Removed>)

Brilliant. I have changed the background colour of the first two headers to yellow. Well no, it’s a little more than that. I have used data validation dropdown lists (**ALT + D + L**) to create input headers!!

![](<Base64-Image-Removed>)

Thus, if I change the selections, I have dynamic summarisations, such as

![](<Base64-Image-Removed>)

or

![](<Base64-Image-Removed>)

Multiple summary statistics may be created similarly, or else you can simply connect them if the reporting fields are contiguous, _e.g._

**\=GROUPBY(CHOOSECOLS(tbl,1,2),tbl\[\[Sales\]:\[Rating\]\],AVERAGE)**

![](<Base64-Image-Removed>)

Here, **tbl\[\[Sales\]:\[Rating\]\]** may be used to specify the **values** as they are side by side.

Obviously, there are many more arguments to play with, but hopefully, you get the general idea, such as ranking the **Item** field in descending order by **Sales** using the formula

**\=GROUPBY(tbl\[Item\],tbl\[Sales\],SUM,,,-2)**

![](<Base64-Image-Removed>)

Indeed, the outputs summarised don’t have to be numerical. A more comprehensive example summarising the **Items** field might look like this:

**\=GROUPBY(tbl\[Category\],tbl\[Item\],LAMBDA(x,ARRAYTOTEXT(SORT(UNIQUE(x)))))**

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-groupby-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-groupby-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-groupby-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-groupby-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-groupby-function/#0 "close")

top