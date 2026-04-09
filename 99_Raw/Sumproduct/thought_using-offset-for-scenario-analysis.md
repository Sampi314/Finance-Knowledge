# Using OFFSET for Scenario Analysis

**Source:** https://sumproduct.com/thought/using-offset-for-scenario-analysis/

---

[Home](https://sumproduct.com/)

\> Using OFFSET for Scenario Analysis

*   May 14, 2025

Using OFFSET for Scenario Analysis
==================================

How to use OFFSET with "what-if"analysis.

Useful Modelling Functions #4: Using OFFSET for Scenario Analysis
=================================================================

_Liam Bastick explains how OFFSET can assist with “what if?” analysis._

**_OFFSET at the outset_**

Recently, I talked about **INDEX** and **MATCH** functions concerned with position; this time, I look at **OFFSET**, a function which considers disposition or displacement. The syntax for **OFFSET** is as follows:

**OFFSET(Reference,Rows,Columns,\[Height\],\[Width\])**

The arguments in square brackets (**Height** and **Width**) can be omitted from the formula (they both have a default value of 1 which will be explained further next time).

In its most basic form, **OFFSET(Reference,Rows,Columns)** will select a reference **Rows** rows down (**\-Rows** would be **Rows** rows up) and **Columns** columns to the right (**\-Columns** would be **Columns** columns to the left) of the **Reference**. For example, consider the following grid:

![](<Base64-Image-Removed>)

**OFFSET(A1,2,3)** would take us two rows down and three columns across to cell **D3**. Therefore, **OFFSET(A1,2,3)** = 16, _viz._

![](<Base64-Image-Removed>)

**OFFSET(D4,-1,-2)** would take us one row up and two columns to the left to cell **B3**. Therefore, **OFFSET(D4,-1,-2)** = 14, _viz._

![](<Base64-Image-Removed>)

It is this displacement technique that can create a scenario table:

![](<Base64-Image-Removed>)

This example is included in the [attached Excel file](https://sumproduct.com/assets/thought-files/using-offset-for-scenario-analysis/sp---using-offset-for-scenario-analysis.xlsm)
. Essentially, the assumptions used in the model are linked from cells **L17:L24** (mainly in cyan). These values are drawn from the scenario table to the right of the highlighted yellow range (_e.g._ cells **N17:N24** constitute Scenario 1. The “Base” case, cells **O17:O24** constitute Scenario 2).

The Scenario Selector is located in cell **H12**. Using **OFFSET** we can retain all scenarios and select as we see fit. For example, the formula in cell **L18** (highlighted) is simply **\=OFFSET(M18,,$H$12)**, that is, start at cell **M18** and displace zero rows and the value in **H12** columns across. In the illustration above, the formula locates the cell one column to the right, which is Scenario 1.

The advantage of **OFFSET** over other functions such as **INDEX**, **CHOOSE** and **LOOKUP** functions is that the range of data can be added to. The image below shows Scenarios 6 and 7 added in an instant. Whilst the other functions require a specified range whereas we can keep adding scenarios without changing the formula / making the model inefficient.

![](<Base64-Image-Removed>)

It should be noted that **OFFSET** is a **volatile function**, _i.e._ a function that causes recalculation of a formula in the cell where it resides every time Excel recalculates. This occurs regardless of whether precedent cells / calculations have changed, or whether the formula also contains non-volatile functions. One test to check whether your workbook is volatile is close a file after saving and see if Excel prompts you to save it a second time (this is an indicative test only).

**OFFSET** is also what is known as a **non-auditable** function in that it does not recognise dependent cells that are linked via an **OFFSET** function. For example, in my illustration above, the $3.70 in cell **N18** is clearly used. However, if you were to select this cell and trace dependents (**ALT + M + D**), you would get the following message:

![](<Base64-Image-Removed>)

This should not put you off using **OFFSET**; it is a function that frequently calculates much quicker than the alternative options and its advantages may often outweigh the potential pitfalls.

It’s such a versatile and useful function I shall be continuing with further examples next time…

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/using-offset-for-scenario-analysis/#0)
    
*   [Register](https://sumproduct.com/thought/using-offset-for-scenario-analysis/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/using-offset-for-scenario-analysis/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/using-offset-for-scenario-analysis/#0)

[](https://sumproduct.com/thought/using-offset-for-scenario-analysis/#0 "close")

top