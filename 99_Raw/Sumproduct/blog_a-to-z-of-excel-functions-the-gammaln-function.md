# A to Z of Excel Functions: The GAMMALN Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gammaln-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The GAMMALN Function

*   January 19, 2020

A to Z of Excel Functions: The GAMMALN Function
===============================================

A to Z of Excel Functions: The GAMMALN Function
===============================================

20 January 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **GAMMALN** function._

**The GAMMALN function**

The Gamma distribution is widely used in engineering, science and business, to model continuous variables that are always positive and have skewed distributions. The Gamma distribution can be useful for any variable which is always positive, such as cohesion or shear strength for example.

It is a distribution that arises naturally in processes for which the waiting times between events are relevant, and is often thought of as a waiting time between Poisson distributed events (the Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval). This is what is known as “queueing analysis”.

To understand it, first think of factorials, _e.g._ 5! = 5 x 4 x 3 x 2 x 1 = 120. So far, so good, but how do you calculate if the factorial number you want to evaluate isn’t an integer? The Gamma function is used to calculate this:

**Г(N+1) = N \* Г(N)**

That’s great (if a little recursive), so can be expressed better (!) mathematically as follows:

![](<Base64-Image-Removed>)

Clear as mud? Well, it gets better. The Gamma distribution just referred to has the following probability density function:

![](<Base64-Image-Removed>)

where **Г(****α)** is the Gamma function, and the parameters **α** and **β** are both positive, _i.e._**α** > 0 and **β** > 0:

*   **α** is known as the shape parameter, while **β** is referred to as the scale parameter
*   **β** has the effect of stretching or compressing the range of the Gamma distribution. A Gamma distribution with **β** = 1 is known as the standard Gamma distribution.

The Gamma distribution represents a family of shapes. As suggested by its name, **α** controls the shape of the family of distributions. The fundamental shapes are characterized by the following values of **α**:

*   Case I (**α** < 1): when **α** < 1, the Gamma distribution is exponentially shaped and asymptotic to both the vertical and horizontal axes
*   Case II (**α** = 1): the Gamma distribution with shape parameter **α** = 1 and scale parameter **β** is the same as an exponential distribution of scale parameter (or mean) **β**
*   Case III (α > 1): when **α** is greater than one, the Gamma distribution assumes a mounded (unimodal), but skewed shape. The skewness reduces as the value of **α** increases.

![](<Base64-Image-Removed>)

The **GAMMALN** function is the natural logarithm of the Gamma function, **Г(N)**. It has the following syntax:

**GAMMALN(x)**

It’s important to note that this function has been replaced with a new function (**GAMMALN.PRECISE**) that may provide improved accuracy and whose name better reflects its usage and consistency with other programming languages. Although this function is still available for backward compatibility, you should consider using the new functions from now on, because this function may not be available in future versions of Excel.

The **GAMMALN** function has the following argument:

*   **x:** this is required and this represents the value for which you wish to calculate the natural logarithm of **Г(x)**.

It should be noted that:

*   if **x** is nonnumeric, **GAMMALN** returns the _#VALUE!_ error value
*   if **x** ≤ 0, **GAMMALN** returns the _#NUM!_ error value
*   the number **e** raised to the **GAMMALN(i)** power, where **i** is an integer, returns the same result as **(i – 1)!**
*   **GAMMALN** is calculated as follows:  
    **GAMMALN = LN(Γ(x))**.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gammaln-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gammaln-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gammaln-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gammaln-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gammaln-function/#0 "close")

top