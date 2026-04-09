# A to Z of Excel Functions: The SUMIF Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sumif-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The SUMIF Function

*   March 16, 2026

A to Z of Excel Functions: The SUMIF Function
=============================================

_Welcome back to our regular A to Z of Excel Functions blog.  Today we look at the **SUMIF** function._

**The SUMIF function**

![](<Base64-Image-Removed>)

Even if you are unfamiliar with this function, you can still probably guess what **SUMIF** does: it combines **SUM** with **IF** to provide conditional summing, _i.e._ where you wish to add numerical values, provided they meet a certain criterion.  For example, imagine you were reviewing the following data summary:

![](<Base64-Image-Removed>)

The function **SUMIF(range, criterion\[, sum\_range\])** is ideal for summing data based upon one \[1\] requirement:

*   **range** is the array that you wanted evaluated by the criterion (in this instance, cells **F12:F21**)
*   **criterion** is the criterion in the form of a number, expression, or text that defines which cell(s) will be added, e.g. “X”, 1, **G26** or **“<>”&G27** (this last one means “not equal to the value in cell **G27**”)
*   **sum\_range** are the actual cells to be added if their corresponding cells in **Range** match the **criterion**.  This should be of the same dimensions as **range**; if it is not specified, it is presumed to be **range**.

Therefore, to find the sales for Business Unit 1 in the above example, you can use the formula **\=SUMIF(F12:F21,1,H12:H21)** (which is $1,000), or to find the total sales of Product X, the formula could be modified to **\=SUMIF(G12:G21,”X”,H12:H21)** (which is $1,200)(note that any text must be in inverted commas).

**SUMIF** is fine when there is only one condition.  However, how would you find the total sales of Product Z in Business Unit 1 using this function?  That’s two criteria and **SUMIF** does not work with multiple conditions.  There are various alternatives using other functions, but it is possible to solve this problem simply using **SUMIF**.

It is often possible to cheat with SUMIF by making a ‘mega-criterion’ out of multiple criteria.  This works on joining criteria together usually by using the ampersand (‘**&**’) operator.

Let’s consider our example, slightly revised, from above.

![](<Base64-Image-Removed>)

A new column has been inserted (column **H**), with a formula combining the contents of columns **F** and **G** (_e.g._ the formula in cell **H12** is **\=F12&G12**).  Provided that all possible combinations are unique (_i.e._ no duplicates can be generated), a simple **SUMIF** can then be applied, _e.g._

> **\=SUMIF(H12:H21,”1Z”,I12:I21)**.

This is by far and away the simplest solution – _if it works_.  It can fall down though (in another example, the concatenation ”111” might refer to Product 1 in Business Unit 11 or Product 11 in Business Unit 1). 

_We’ll continue our A to Z of Excel Functions soon.  Keep checking back – there’s a new blog post every business day._

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sumif-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sumif-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sumif-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sumif-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sumif-function/#0 "close")

top