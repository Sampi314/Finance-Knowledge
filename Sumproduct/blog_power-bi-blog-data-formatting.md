# Power BI Blog: Data Formatting

**Source:** https://sumproduct.com/blog/power-bi-blog-data-formatting/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Data Formatting

*   September 22, 2021

Power BI Blog: Data Formatting
==============================

Power BI Blog: Data Formatting
==============================

23 September 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we discuss data formatting in Power BI._

One way to format values is using the ‘Formatting’ section under ‘Column / Measure’ tools, which will appear after you select a column or measure. This method is a simple way to set the data format using some common default settings.

![](<Base64-Image-Removed>)

Another way is by going to the **Model tab -> Choose a column / measure under Fields -> Properties -> Formatting section**:

![](<Base64-Image-Removed>)

This method allows us to use some predefined formats as well as to apply our own custom format. For example:

![](<Base64-Image-Removed>)

Sometimes, we may need to dynamically change the formats in different scenarios. For example, our users may come from many countries which have different formatting requirements for currency, date, _etc._ In this case, we can use the DAX **FORMAT** function. This function is similar to the TEXT function that we may use in Microsoft Excel.

Its syntax is as follows:

**FORMAT(value, format\_string)**

where:

*   **value** is a value or expression that evaluates to a single value
*   **format\_string** is a formatting template using the characters _(below)_.

While you can find various formatting templates on the [Microsoft website](https://docs.microsoft.com/en-us/dax/format-function-dax)
, below are some custom format characters that we find are the most commonly used**:**

**Numbers**

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

**Text**

![](<Base64-Image-Removed>)

**Time**

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

**Examples**

![](<Base64-Image-Removed>)

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-data-formatting/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-data-formatting/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-data-formatting/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-data-formatting/#0)

[](https://sumproduct.com/blog/power-bi-blog-data-formatting/#0 "close")

top