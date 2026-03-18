# A to Z of Excel Functions: The MOD Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mod-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The MOD Function

*   July 10, 2022

A to Z of Excel Functions: The MOD Function
===========================================

A to Z of Excel Functions: The MOD Function
===========================================

11 July 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **MOD** function._

**The MOD function**

The **MOD** function, **MOD(number, divisor)**, returns the remainder after the **number** (first argument) is divided by the **divisor** (second argument). The result has the same sign as the **divisor**.

For example, 9 / 4 = 2.25, or 2 remainder 1. **MOD(9,4)** is an alternative way of expressing this, and hence equals one \[1\] also. Note that the 1 may be obtained from the first calculation by (2.25 – 2) x 4 = 1, _i.e._ in general:

**MOD(n, d) = n – d \* INT(n / d)**,

where **INT()** is the integer function in Excel.

_**Uses of MOD**_

This function has various uses and I provide three common examples below:

*   **Obtaining “residuals”:** in some instances in modelling, you need the integer part of a number, _e.g_. how many payments fall between two dates may calculate as 9.94 – but that’s nonsense. In this instance, you would have only made nine payments, _i.e_. **INT(9.94)**.
    
    Similarly, you might want to accrue the fee for payments not yet made. Using **MOD(9.94,1)** = 0.94, _i.e._ the number after the decimal place. Note that 9.94 – **INT(9.94)** gives the same result here; the **MOD** approach is simply shorter
    
*   **Calculations at regular time intervals:** consider tax payments as an example. Many companies make tax payments quarterly (_i.e_. once every three months). If we assume these payments are made in March, June, September and December then we can formulate the payment as **IF(MOD(month\_number)=0, make\_payment, 0)**, _etc._

![](<Base64-Image-Removed>)

*   **Summing every nth row:** it is not uncommon for users to want to sum every **n**th cell (_e.g_. second, third, fourth,…) in a spreadsheet. Excel has no standard function which will do this, but **MOD** can come to the rescue. For example, the array formula

**{=SUM(IF(MOD($E$19:$E$48,$G$13)=0,$F$19:$F$48,0))}  
**

was used in cell **H53** in the following example:

![](<Base64-Image-Removed>)

Arrays using large ranges can cause calculations to slow down considerably. This is why I used a counter rather than the volatile **ROW()** function (volatile functions calculate each time you press **ENTER** or **F9**).

_**Care with MOD (1): Minor Inaccuracies**_

If accuracy is vital, be careful with **MOD** as it may give very slightly erroneous results:

![](<Base64-Image-Removed>)

The result for **MOD** in cell **G17** might seem inconsequential, but imagine you were making calculations based on **MOD(number, divisor)=0**. In this case, **MOD** would not equal zero \[0\] and the calculation would not work.

This issue tends to occur more commonly when working with non-integers.

The problem here isn’t really **MOD**. Calculations are performed in binary \[1,0\] format and most floating point numbers have no exact binary representation (just as 1/3 has no exact decimal representation). In this instance, 10 times the binary approximation to 622.2 is

6222.0000000000004547….

_i.e._ you may need to use the **ROUND(number, number\_of\_digits)** as part of your formula too.

_**Care with MOD (2): #NUM! Errors**_

If the number is 134,217,728 (227) times greater or more than the divisor this gives rise to an _#NUM!_ error, _viz_.

![](<Base64-Image-Removed>)

Some texts suggest that you could use the formula

**\=MOD(MOD(number, 134217728\*divisor), divisor)**

This will solve for larger numbers much larger than the limit for **MOD**, but theoretically will hit the same problem when the number being evaluated reaches 134,217,728\*134,217,728\***divisor**. For most uses, this is limit is large enough that it will never be reached, but I suggest sticking with Microsoft’s recommended solution which is calculating the “longhanded” result as illustrated above (cell **G24**).

_**Care with MOD (3): Positives and Negatives**_

When using the **MOD** function with one negative number and the expected result is the **numerator**, **MOD(9,-10)** returns -1, whereas you could argue the correct result should be 9:

![](<Base64-Image-Removed>)

Note that the longhand approach also gives a result of -1. Microsoft explains that this approach has been taken deliberately in order to be consistent with the dBase **MOD** function.

If you always need **MOD** to deliver a value of **x** where 0 ? **x** < **divisor**, then use the adjusted formula:

**\=IF(MOD(number, divisor)<0, ABS(divisor) + MOD(number, divisor))**.

**_And Finally…_**

In summary, I suppose you can say that **MOD** does cause division amongst financial modellers!

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found__[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mod-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mod-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mod-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mod-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mod-function/#0 "close")

top