# A to Z of Excel Functions: The PRODUCT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-product-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The PRODUCT Function

*   March 10, 2024

A to Z of Excel Functions: The PRODUCT Function
===============================================

A to Z of Excel Functions: The PRODUCT Function
===============================================

11 March 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **PRODUCT** function._

**The PRODUCT function**

![](<Base64-Image-Removed>)

The **PRODUCT** function multiplies all the numbers given as arguments and returns the product. For example, if cells **A1** and **A2** numbers, you can use the formula **\=PRODUCT(A1, A2)** to multiply those two numbers together. You can also perform the same operation by using the multiply (**\***) mathematical operator; for example, **\=A1 \* A2**.

The **PRODUCT** function is useful when you need to multiply many cells together. For example, the formula **\=PRODUCT(A1:A9, C1:C9)** is equivalent to

\=**A1 \* A2 \* A3 \* A4 \* A5  
\* A6 \* A7 \* A8 \* A9 \* C1 \* C2 \* C3 \* C4 \* C5 \* C6 \* C7 \* C8 \* C9.**

The **PRODUCT** function uses the following syntax to operate:

**PRODUCT(number1\[, number2, …\])**

The **PRODUCT** function has the following arguments:

*   **number1:** this is required and represents the first number or range you wish to multiply
*   **number2, …:** this argument is optional and represents the additional number(s) or range(s) you want to multiply, up to a maximum of 255 arguments.

It should be noted that if an argument is an array or reference, only numbers in the array or reference are multiplied. Empty cells, logical values, and text in the array or reference will be ignored.

**PRODUCT** is often used in financial modelling. Consider the following example:

![](<Base64-Image-Removed>)

In this illustration, you might not understand what the **MOD** function does, but hopefully, you can follow each of the flags in rows 4 to 7 without being an Excel guru. Row 9, the product, simply multiplies all of the flags together (using the **PRODUCT** function allows you to add additional conditions / rows easily). This effectively produces a sophisticated **[AND](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-and-function)
** flag, where all of the formulae are mercifully short.

Some might wonder why I use **PRODUCT** rather than **[MIN](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-min-function)
**here. I confess it is partly a preference and partly the fact that if you are modelling optimisation problems, **MIN** can give rise to non-smooth outputs (not a good thing) whereas **PRODUCT** does not.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-product-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-product-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-product-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-product-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-product-function/#0 "close")

top