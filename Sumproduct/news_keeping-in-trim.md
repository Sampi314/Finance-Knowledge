# Keeping in TRIM

**Source:** https://sumproduct.com/news/keeping-in-trim/

---

[Home](https://sumproduct.com/)

\> Keeping in TRIM

*   August 29, 2024

Keeping in TRIM
===============

Keeping in TRIM
===============

29 August 2024

Microsoft announced a new function, **TRIMRANGE**, and an accompanying set of new reference operators today. Albeit in Preview only (and presently only to a select few which seems to be slightly less than the number of lottery winners on the moon), **TRIMRANGE** scans in from the edges of a range or array until it finds the first non-blank cell (or value). It then excludes those blank rows or columns.

It should be noted that **TRIMRANGE** and the associated new reference operators are not text functions, so they are not going to be useful for cell contents, such as line breaks or carriage returns.

The syntax is as follows:

**TRIMRANGE(range, \[trim\_rows\], \[trim\_columns\])**

It has three \[3\] arguments:

*   **range:** this argument is required and representsthe range (or array) to be trimmed
*   **trim\_rows:** this argument is optional and determines which rows should be trimmed by selecting one of four \[4\] values:
    *   **0:** none
    *   **1:** trims leading blank rows
    *   **2:** trims trailing blank rows
    *   **3 (default if omitted):** trims both leading and trailing blank rows
*   **trim\_columns:** this argument is optional and determines which columns should be trimmed by selecting one of four \[4\] values:
    *   **0:** none
    *   **1:** trims leading blank columns
    *   **2:** trims trailing blank columns
    *   **3 (default if omitted):** trims both leading and trailing blank columns.

In essence, the **TRIMRANGE** function removes empty rows and / or columns from the edges of a range. This can be particularly useful when writing dynamic array formulae or optimising aggregation, array or lambda functions for performance.

We think **TRIMRANGE** may have missed a trick here in its initial Preview guise as we think of the **TRIM** function which removes excess space, not just at the beginning and end of a text string but throughout. We can’t help feeling options to remove blank rows / columns throughout the range might be welcomed by many and feel there are many areas where this would be beneficial (_e.g._ charting, dashboards, summary outputs).

In the example below, **TRIMRANGE** has been used to calculate the length of any text entered into column **A**:

![](https://sumproduct.com/wp-content/uploads/2025/05/9df9f00c99e05a745830ceedf2a02c1b.jpg)

The formula here is given by

**\=LEN(A1:A5)**

However, we might wish to extend the range to add more words in column **A**, and this can lead to redundant calculations and possibly slower performance as the spreadsheet becomes more complex.

![](https://sumproduct.com/wp-content/uploads/2025/05/abf8f90d5eb42aedc874fe014f25c76c.jpg)

This is where the formula

**\=LEN(TRIMRANGE(A:A))**

can come to the rescue and remove unused calculations (but reinstate them later if more text is added in column **A**):

![](<Base64-Image-Removed>)

Easy!

![](<Base64-Image-Removed>)

Without the use of **TRIMRANGE**,

**\=LEN(A:A)**

would calculate for every cell in column **C**, returning over a million unnecessary results. Besides being inefficient, trailing undesirable zeroes are returned to the grid. This can be especially problematic if you then try and operate on the spill using **\=C1#** notation.

**TRIMRANGE** is also a useful tool for optimising the performance of lambda functions that operate on ranges. No doubt Microsoft has some particular scenarios in mind here (more new dynamic array functions soon possibly?). It allows lambda authors to more tightly scope ranges, which can reduce the number of required computations.

We don’t have this function ourselves yet, but anecdotal evidence suggests this function will not work with three-dimensional references, but it does seem to work with arrays as well as ranges. We shall do more testing as and when we can!

This new function has provided Microsoft with the opportunity to introduce **Trim References**, also known as **Trim Refs**. These may be used to achieve the same functionality as **TRIMRANGE** more succinctly by replacing the range’s colon “**:**” with one of the three Trim Ref types described below:

![](<Base64-Image-Removed>)

Personally, I’d like a different syntax such as **<:>**, **<:** and **:>** to make it easier to read for accessibility purposes, but hey, beggars cannot be choosers. Remember, all of the above is in Preview: your feedback is welcomed and there is still time to make a difference before they land in production / become Generally Available.

Full-column references are often avoided because they can have poor performance with some functions. However, with Trim Refs, they are much more performant as the full-column reference can be constrained to just the portion with values.

Before you get too excited, this new function and these new references are currently available to Beta Channel users running **Version 2409 (Build 18020.2000)** or later, and even then, it’s not everyone – yet! Pray Santa thinks you’ve been good!

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/keeping-in-trim/#0)
    
*   [Register](https://sumproduct.com/news/keeping-in-trim/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/keeping-in-trim/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/keeping-in-trim/#0)

[](https://sumproduct.com/news/keeping-in-trim/#0 "close")

top