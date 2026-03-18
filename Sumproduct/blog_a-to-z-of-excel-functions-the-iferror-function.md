# A to Z of Excel Functions: The IFERROR Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iferror-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The IFERROR Function

*   May 24, 2020

A to Z of Excel Functions: The IFERROR Function
===============================================

A to Z of Excel Functions: The IFERROR Function
===============================================

25 May 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **IFERROR** function._

**The IFERROR function**

**IFERROR** first came into being back in Excel 2007. It was something users had asked Microsoft for, for a very long time. But let me go back in time first and explain why.

At the time of writing, there are 12 **IS** functions, _i.e._ functions that give rise to a TRUE or FALSE value depending upon whether a certain condition is met:

1\. **ISBLANK(Reference):** checks whether the **Reference** is to an empty cell

2\. **ISERR(Value):** checks whether the **Value** is an error (_e.g. #REF!, #DIV/0!, #NULL!_). This check specifically excludes _#N/A_

3\. **ISERROR(Value):** checks whether the **Value** is an error (_e.g. #REF!, #DIV/0!, #NULL!_). This is probably the most commonly used of these functions in financial modelling

4\. **ISEVEN(Number):** checks to see if the **Number** is even

5\. **ISFORMULA(Reference):** checks to see whether the **Reference** is to a cell containing a formula

6\. **ISLOGICAL(Value):** checks to see whether the **Value** is a logical (TRUE or FALSE) value

7\. **ISNA(Value):** checks to see whether the **Value** is _#N/A_. This gives us the rather crude identity **ISERR + ISNA = ISERROR**

8\. **ISNONTEXT(Value):** checks whether the **Value** is not text (_N.B._ blank cells are not text)

9\. **ISNUMBER(Value):** checks whether the **Value** is a number

10\. **ISODD(Number):** checks to see if the **Number** is odd. Personally, I find the number 46 very odd, but Excel doesn’t

11\. **ISREF(Value):** checks whether the **Value** is a reference

12\. **ISTEXT(Value):** checks whether the **Value** is text.

You get the idea. As mentioned previously, sometimes you need to trap errors that may originate from a formula that is correct most of the time. Where possible, you should be specific with regard to what you are checking, _e.g._

**\=IF(Denominator=0, Error\_Trap, Numerator / Denominator)**

In this example, I am checking to see whether the **Denominator** is zero. I could use this formula instead:

**\=IF(ISERROR(Numerator / Denominator), Error\_Trap, Numerator / Denominator)**

The difference here is that this will check for anything that may give rise to an error:

![](<Base64-Image-Removed>)

Do you see the problem here? I have to put the same formula in _twice_. If that is a long formula, then the calculation becomes doubly long. This is where **IFERROR** comes in; it halves the length of the calculation but still achieves the same effect

**\=IFERROR(Calculation, Error\_Trap)**

Essentially, this formula is the bastard lovechild of **IF** and **ISERROR**. It checks to see whether the **Calculation** will give rise to a _prima facie_ error. If it does, it will return **Error\_Trap**; otherwise, it will perform the said **Calculation**, _e.g._

![](<Base64-Image-Removed>)

You shouldn’t just sprinkle **IFERROR** throughout your models like your formulae are confetti. Used unwisely, **IFERROR** can disguise the fact that your formula isn’t working correctly and that modifications to the logic may be required. Try to use it sparingly.

Sometimes you have to use **IF** and **ISERROR** in combination anyway:

**\=IF(ISERROR(Calculation), Error\_Trap, Different\_Calculation)**

In this example, the formula is checking to see whether a particular **Calculation** gives rise to an error. If it does, the **Error\_Trap** will be referenced in the usual way, but if not a **Different\_Calculation** (not the **Calculation** used for the test) will be computed.

These two methodologies should be mastered. You will create more robust and flexible models once your error become a thing of the past. Not just the model – but your own expertise – will become more trusted in your organisation if users never encounter _prima facie_ errors in your model.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iferror-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iferror-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iferror-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iferror-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iferror-function/#0 "close")

top