# The A to Z of DAX Functions – EVEN

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-even/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – EVEN

*   September 19, 2023

The A to Z of DAX Functions – EVEN
==================================

Power Pivot Principles: The A to Z of DAX Functions – EVEN
==========================================================

19 September 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **EVEN**._

**_The_** _**EVEN**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/9292f6f2385871e23822e1b9eba6cb11.jpg)

If DAX frustrates you, don’t get mad, get **EVEN**.

The **EVEN** functionis one of the math and trig functions which returns numbers rounded up to the nearest even integer.

![](https://sumproduct.com/wp-content/uploads/2025/06/4ed2be7f547d8b29c3bb1f18a39efd65.jpg)

You can use this function for processing items that come in twos. For example, a packing crate accepts rows of one or two items. The crate is full when the number of items, rounded up to the nearest two, matches the crate’s capacity.

It has the following syntax:

**EVEN(number)**

It has one \[1\] argument here:

*   **number**: a value to round.

Further, it should be noted:

*   if the number is non-numeric, the **EVEN** function returns an error message
*   regardless of the sign of the number, a value is rounded up when adjusted away from zero \[0\].
*   if the number is an even integer, no rounding occurs
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Consider using **EVEN** with the values -14.1, 14, “29.1” and “One”. Let’s create the following measures to test **EVEN** out:

![](<Base64-Image-Removed>)

![](https://sumproduct.com/wp-content/uploads/2025/06/7730086600a716d935b8d4e7899d326c.jpg)

As we can see here the value -14.1 is rounding to -16 instead of -14 as we mentioned before the value is rounding away from zero \[0\]. Hence, the number returned is -16.

![](https://sumproduct.com/wp-content/uploads/2025/06/864908ad9ffe377a764d2c737ef87002.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/26259c6e5468cbbbdcfc46d91cf4957f.jpg)

As we can see here, the number is not rounded up to the next even number in this case.

![](https://sumproduct.com/wp-content/uploads/2025/06/13736e48293ed8e554dd18ff8e6a9993.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/3ac75cfe1767c3c121059dfd21ad4b01.jpg)

The next example we have here is to deal with a number in form of a text string. As you can see here the **EVEN** function will convert the text into value and then perform the rounding.

![](https://sumproduct.com/wp-content/uploads/2025/06/f0543a08462e6ee203a83bdab90d412b.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/7165f3fd62ae0f8868025a2076a5f340.jpg)

Although we were able to pass through the formula checking protocol in the Measure dialog we were unable to put this measure in the PivotTable and obtain the above error message instead.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-even/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-even/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-even/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-even/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-even/#0 "close")

top