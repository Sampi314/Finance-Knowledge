# A to Z of Excel Functions: The PERCENTOF Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentof-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The PERCENTOF Function

*   December 10, 2023

A to Z of Excel Functions: The PERCENTOF Function
=================================================

A to Z of Excel Functions: The PERCENTOF Function
=================================================

11 December 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **PERCENTOF** function._

**The PERCENTOF function**

![](<Base64-Image-Removed>)

This function may be used in conjunction with functions such as **[GROUPBY](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-groupby-function)
**and **[PIVOTBY](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-pivotby-function)
**, or else on its own. This is used to return the percentage that a subset makes up of a given dataset. It is logically equivalent to

**SUM(subset)  
/ SUM(everything)**

It sums the values in the subset of the dataset and divides it by the sum of all the values. It has the following syntax:

**\=PERCENTOF(data\_subset,  
data\_all)**

The arguments are as follows:

*   **data\_subset:** this is required, and represents the values that are in the data subset
*   **data\_all:** this too is required, and denotes the values that make up the entire set.

Consider the following Excel Table called **tbl**:

![](<Base64-Image-Removed>)

You can use it, for example, with **[GROUPBY](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-groupby-function)
**:

**\=GROUPBY(tbl\[Category\],tbl\[Sales\],PERCENTOF)**

![](<Base64-Image-Removed>)

Alternatively, it may be used on its own:

**\=PERCENTOF(G13:G14,G13:G16)**

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentof-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentof-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentof-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentof-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentof-function/#0 "close")

top