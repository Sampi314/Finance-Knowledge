# A Modicum of MOD

**Source:** https://sumproduct.com/thought/a-modicum-of-mod/

---

[Home](https://sumproduct.com/)

\> A Modicum of MOD

*   May 14, 2025

A Modicum of MOD
================

When to use this divisive function and what to be careful of.

Off Your Rocker Using MOD..?
============================

What’s in a name? This article looks at one of Excel’s less well known but useful functions – as long as you understand its limitations. By Liam Bastick, Director with SumProduct Pty Ltd.

Query
-----

I have recently discovered the MOD function in Excel. I am not quite sure when you might use it in practice and colleagues have told me there are some slight issues with it. Could you please shed some light?

Advice
------

The MOD function, **MOD(number,divisor)**, returns the remainder after the **Number** (first argument) is divided by the **Divisor** (second argument). The result has the same sign as the divisor.

For example, 9 / 4 = 2.25, or 2 remainder 1. MOD(9,4) is an alternative way of expressing this, and hence equals 1 also. Note that the 1 may be obtained from the first calculation by (2.25 – 2) x 4 = 1, i.e. in general:

MOD(n,d) = n – d\*INT(n/d),

where **INT()** is the integer function in Excel.

### Uses of MOD

This function has various uses and I provide three common examples below:

*   **Obtaining “residuals”**: In some instances in modelling, you need the integer part of a number, e.g. how many payments fall between two dates may calculate as 9.94 – but that’s nonsense. In this instance, you would have only made nine payments, i.e. INT(9.94). Similarly, you might want to accrue the fee for payments not yet made. Using MOD(9.94,1) = 0.94, i.e. the number after the decimal place. Note that 9.94 – INT(9.94) gives the same result here; the MOD approach is simply shorter.
*   **Calculations at regular time intervals:** Consider tax payments as an example. Many companies make tax payments quarterly (i.e. once every three months). If we assume these payments are made in March, June, September and December then we can formulate the payment as

IF(MOD(Month\_Number)=0,Make\_Payment,0), etc.

![](<Base64-Image-Removed>)

Tax Payments Example

*   **Summing every nth row:** It is not uncommon for users to want to sum every nth cell (e.g. second, third, fourth,…) in a spreadsheet. Excel has no standard function which will do this, but MOD can come to the rescue. For example, the following array formula was used in cell H53 in the following example:

{=SUM(IF(MOD($E$19:$E$48,$G$13)=0,$F$19:$F$48,0))}

![](<Base64-Image-Removed>)

Summing every nth row

Arrays using large ranges can cause calculations to slow down considerably. This is why I used a counter rather than the volatile **ROW()** function (volatile functions calculate each time you press ‘ENTER’ or F9). For more on arrays, please see the [following link](https://www.sumproduct.com/thought/array-of-light)
.

Further, this last example could also be calculated using **DSUM()** avoiding array functions altogether. For more on this function, please see [this link](https://www.sumproduct.com/thought/multiple-criteria)
.

The last two examples are illustrated in the attached [Excel file](https://sumproduct.com/assets/thought-files/sp-mod-examples.xls)
.

### Care with MOD (1): Minor Inaccuracies

If accuracy is vital, be careful with MOD as it may give very slightly erroneous results:

![](<Base64-Image-Removed>)

Minor inaccuracies with MOD

The result for MOD in cell G17 here might seem inconsequential, but imagine you were making calculations based on **MOD(Number,Divisor)=0**. In this case MOD would not equal zero and the calculation would not work.

This issue tends to occur more commonly when working with non-integers.

The problem here isn’t really MOD. Calculations are performed in binary \[1,0\] format and most floating point numbers have no exact binary representation (just as 1/3 has no exact decimal representation). In this instance, 10 times the binary approximation to 622.2 is

6222.0000000000004547…

i.e. you may need to use the **ROUND(number,num\_digits)** as part of your formula too.

### Care with MOD (2): #NUM! Errors

If the number is 134,217,728 (227) times greater or more than the divisor this gives rise to a #NUM! error viz.

![](<Base64-Image-Removed>)

#NUM! example

Some texts suggest that you could use the formula

\=MOD(MOD(Number,134217728\*Divisor),Divisor).

This will solve for larger numbers much larger than the limit for MOD, but theoretically will hit the same problem when the number being evaluated reaches 134,217,728\*134,217,728\*Divisor. For most uses, this is limit is large enough that it will never be reached, but I suggest sticking with Microsoft’s recommended solution which is calculating the “longhanded” result as illustrated above (cell G24, again please see the [attached Excel file](https://sumproduct.com/assets/user-upload/sp-mod-examples1.xls)
).

### Care with MOD (3): Positives and Negatives

When using the MOD() function with one negative number and the expected result is the numerator, MOD(9,-10) returns -1, whereas you could argue the correct result should be 9:

![](<Base64-Image-Removed>)

Negative divisors

Note that the longhand approach also gives a result of -1.

Microsoft explains that this approach has been taken deliberately in order to be consistent with the dBase MOD function.

If you always need MOD to deliver a value of x where 0 ? x < divisor, then use the adjusted formula:

\=IF(MOD(Number,Divisor)<0,ABS(Divisor)+MOD(Number,Divisor)).

### And Finally…

In summary, I suppose you can say that MOD does cause division amongst financial modellers!

### Related Articles

Liked this article? Here are some other articles that you may find interesting.

*   [Sum Every Nth Item](https://www.sumproduct.com/thought/sum-every-nth-item)
     – Presenting a simple formulaic approach for summing every Nth item in a list
*   [Time Series](https://www.sumproduct.com/thought/time-series)
     – No time series problems – period! _MODELLING_
*   [\>Consistent Formulae](https://www.sumproduct.com/thought/consistent-formulae)
     – How to seek out inconsistencies consistently. _AUDITING_

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/a-modicum-of-mod/#0)
    
*   [Register](https://sumproduct.com/thought/a-modicum-of-mod/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/a-modicum-of-mod/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/a-modicum-of-mod/#0)

[](https://sumproduct.com/thought/a-modicum-of-mod/#0 "close")

top