# A to Z of Excel Functions: The PROB Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-prob-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The PROB Function

*   February 4, 2024

A to Z of Excel Functions: The PROB Function
============================================

A to Z of Excel Functions: The PROB Function
============================================

5 February 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **PROB** function._

**The PROB function**

I have no **PROB** with this function. It returns the probability that values in a range (to be specified) are between two limits. If the upper limit is not specified, **PROB** returns the probability that the value in the **x\_range** is equal to the lower limit.

The **PROB** function uses the following syntax to operate:

**PROB(x\_range, probability\_range, lower\_limit, \[upper\_limit\])**

The **PROB** function has the following arguments:

*   **x\_range:** this is required and represents the range of numerical values of **x** with which there are associated probabilities
*   **probability\_range:** this is also required, and denotes a set of probabilities associated with the values in the **x\_range**
*   **lower\_limit:**this is required and cites the lower bound on the value for which you want a probability
*   **upper\_limit:** this argument is optional and represents the upper bound on the value for which you require a probability.

It should be further noted that:

*   if any value in **probability\_range** ≤ 0 or if any value in **probability\_range** > 1, **PROB** returns the _#NUM!_ error value
*   if the sum of the values in **probability\_range** is not equal to 1, **PROB** returns the _#NUM!_ error value
*   if **upper\_limit** is omitted, **PROB** returns the probability of being equal to the **lower\_limit**
*   if **x\_range** and **probability\_range** contain a different number of data points, **PROB** returns the _#N/A_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-prob-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-prob-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-prob-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-prob-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-prob-function/#0 "close")

top