# A to Z of Excel Functions: The FACT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fact-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The FACT Function

*   April 21, 2019

A to Z of Excel Functions: The FACT Function
============================================

A to Z of Excel Functions: The FACT Function
============================================

22 April 2019

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **FACT** function._

**The FACT function**

In mathematics, the factorial of a non-negative integer **n**, denoted by **n!**, is the product of all positive integers less than or equal to **n**. For example,

5! = 5 × 4 × 3 × 2 × 1 = 120.

The value of 0! is 1, according to the convention for what is known as an empty product, being the multiplicative identity (just as zero (0) is the additive identity).

The factorial operation is encountered in many areas of mathematics, notably in combinatorics, algebra, and mathematical analysis. Its most basic occurrence is the fact that there are **n!** ways to arrange **n** distinct objects into a sequence. These arrangements are called the permutations of the set of objects.

These numbers become astronomical (technical term) _very_ quickly.

In **FACT**, Excel has a function, **FACT**, which calculates these factorials and has the following syntax:

**FACT(number)**.

The **FACT** function has the following arguments:

*   **number:** this is required and is a non-negative number for which you require the factorial.

It should be further noted that:

*   if **number** is not an integer, it is truncated
*   the factorial of a negative **number** returns a _#NUM!_ error
*   the largest allowed positive number (which has to be calculated rather than input) is 1.7976931348623158 x 10308 (also denoted as 1.79769E+308). 171! is larger than this upper bound and hence 171! or any higher value will return a _#NUM!_ error.

Please see my example below:

![](<Base64-Image-Removed>)

Let’s take a closer look at the **FACT** function:

![](<Base64-Image-Removed>)

Do you see what happens from **FACT(15)** onwards? These numbers are expressed – and more importantly, stored – in Scientific (Exponential) notation. 15! is actually 1,307,674,368,000, although it is displayed as 1.30767E+12 and is stored as 1307674368000 (deliberately no commas), which is why its length is 13 (there are 13 digits – more precisely, characters – in the text string).

Similarly:

*   22! is actually 1,124,000,727,777,607,680,000, which is displayed by default as 1.124E+21 and is stored as 1.12400072777761E+21. This stored string has 20 characters: 15 digits (the maximum significant figures Excel can display), a decimal point and four characters for “E+21”. This means that the maximum length for a number smaller than 10100 is 20 characters
*   23! is actually 25,852,016,738,884,976,640,000, which is displayed by default as 2.5852E+22 and is stored as 2.5852016738885E+22. This stored string has 19 characters. This time only 14 digits are included: this is because the 15th number would be “0” and hence is suppressed. This is why 23! has a length of 19 rather than 22! which has a length of 20. 23! is definitely larger than 22!

Therefore, precision is of concern with larger numbers in Excel as they will only display to a maximum of 15 significant figures.

There are two more issues though.

Firstly, let’s take a look at 171!

![](<Base64-Image-Removed>)

It’s the first number in the sequence Excel cannot calculate. The _#NUM!_ error is well earned. The largest allowed positive number (which has to be calculated rather than input) is 1.7976931348623158 x 10308 (also denoted as 1.79769E+308). 171! is larger than this upper bound.

Secondly, I note using numbers only will not retain precision. I need to convert the number to text so that Excel will store all the characters (that’s OK – the maximum number of characters allowed in one cell is 32,767 if I link it in from a closed workbook). The problem is, many Excel functions – including most of the useful text manipulation functions, such as **LEFT**, **RIGHT** and **LEN** will only work with a maximum of 255 characters.

To solve the challenge, you need to get creative and I will demonstrate this by calculating 171!, which is (big drum roll please)…

![](<Base64-Image-Removed>)

This is a screenshot straight out of the [attached Excel workbook](https://sumproduct.com/assets/blog-pictures/2019/a-to-z/160/sp-search-for-171-factorial.xlsx)
 which calculates 171! as 1,241,018,070,217,667,823,424,840,524,103,103,992,616,605,577,501,693,185,388,951,803,611,996,075,221,691,752,992,751,978,120,487,585,576,464,959,501,670,387,052,809,  
889,858,690,710,767,331,242,032,218,484,364,310,473,577,889,968,548,278,290,754,541,561,964,852,153,468,318,044,293,239,598,173,696,899,657,235,903,947,616,152,278,  
558,180,061,176,365,108,428,800,000,000,000,000,000,000,000,000,000,000,000,000,000 – only without the commas!

How was this achieved? Without any VBA, I created a table in Excel to calculate the following:

1.  I need to identify the largest factorial in my table (171) and multiply this by 9.99999999999999… (rounded up to 10) to work out the number of characters I need to keep in reserve, which is 171 x 10 which is 1710 (without commas). This is four characters. Given one character is already used, I need to keep three characters in reserve (this is used for the next step)
2.  Since the maximum number of significant figures is 15, I need to separate my number into blocks (what I called “batches” in the model) into text strings of no more than 15 – 3 = 12 characters. This was defined as the **Batch\_Length**
3.  Define 1! as 1
4.  Convert 1! (1) to a text string (“1”)
5.  Now we need to calculate the next factorial
6.  Calculate the character length of this string
7.  Divide this length by **Batch\_Length** (_i.e._ 12) rounded up to the nearest whole number. This is how many batches are needed
8.  Split the text factorial into batches: Batch 1 is the final 12 characters, Batch 2 is the 24th from last to 13th from last digit, Batch 3 is the 36th from last to the 25th from last digit, and so on
9.  For each batch, convert the text string back to a number simply by multiplying by the factorial you are trying to calculate (_e.g._ if you have just calculated 1! then multiply by two, if it is 17! then multiply by 18)
10.  If the resulting number contains more than 12 characters, split the number in two: the “edited” number is the last 12 characters and the “residual” is any digits at the beginning not included
11.  Add the residual from Batch **n-1** to the Edited number in Batch **n**
12.  Convert all of the numbers back to text strings
13.  Concatenate the batches using the ampersand (‘&’) operator (note this cannot be done with a text function because only 255 characters are allowed and only 15 significant figures would be displayed)
14.  This is the next factorial in the series
15.  To calculate the next factorial in the sequence, return to Step 5 _(above)_.

This is more complicated than it sounds (and it sounds complicated!) due to having to consider what happens if a batch in the middle of the text string starts with one or more zeros, for example. For those who would like to know more (or simply suffer with insomnia), please review the table in the Excel file.

You might think, “who cares about 171 factorial?” and you may have a point. However, this simple question has a non-trivial solution and highlights key issues that need to be considered when with large computations and / or numbers:

*   Even when you encounter a limitation in Excel, where there’s a will there’s a way (and often a relative too)
*   You need to be mindful of the degree of precision in Excel’s outputs (only 15 significant figures)
*   Larger numbers may not be manipulable using Excel’s built-in functions
*   Factorials (even large ones) are often used in combinatoric problems, such as selecting a subset **x** from a larger set **y**. Given **x** and **y**, the solution Excel may give may not be quite correct. This is why many statisticians often use software other than Excel.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fact-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fact-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fact-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fact-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fact-function/#0 "close")

top