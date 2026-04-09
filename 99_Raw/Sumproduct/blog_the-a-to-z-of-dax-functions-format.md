# The A to Z of DAX Functions – FORMAT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-format/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – FORMAT

*   January 2, 2024

The A to Z of DAX Functions – FORMAT
====================================

Power Pivot Principles: The A to Z of DAX Functions – FORMAT
============================================================

2 January 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **FORMAT**._

**_The_** _**FORMAT**_ **_function_**

The _**FORMAT**_ functionis one of the text functions which converts a value to text in a specified format (great dictionary definition, eh?). It has the following syntax:

**FORMAT****(value, format\_string\[, locale\_name\])**

*   **value**: this argument is required which is a value or expression that evaluates to a single value
*   **format\_string**: this is also required. It is a string with the formatting template
*   **locale\_name**: this is not required. This is the name of the locale that the function will use. Possible strings values here accepted by Windows API function **LocaleNameToLCID()**.

It should be noted that:

*   when formatting the result, the predefined format string uses the model culture property. By default, the model culture is setting accordingly to the locale of the computer. The model culture property for newly created Power BI Desktop models may be modified via **Options -> Regional Settings -> Model language**. For Analysis Services, the model culture is initially set according to the Language property defined by the instance
*   rather than being used by the .NET Framework, the format strings that are accepted as an argument for the **FORMAT**function are generated from those that are used by Visual Basic (OLE Automation). As such, you may get unexpected results or run into an error if the supplied input does not match any defined format strings. For example, “p” for “Percent” is not an accepted shorthand. If you provide strings that are not included in the predefined format strings list, they will be treated either as part of a custom format string or as a literal string
*   a measure result is converted to a text data type by using **FORMAT**. If the measure result is originally of numeric data type, then with **FORMAT**, the measure can’t be used on visuals where the values section requires a numeric data type, like with charts. An alternative method for defining a conditional format string for a measure in Power BI is to use dynamic format strings, which preserve the measure’s numeric data type
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s consider the following **EVALUATE** statement:

**EVALUATE**

**{**

**(“Percent”,FORMAT(0.14159,”Percent”)),**

**(“Currency(1)”,FORMAT(3.1415926,”$#,0.00;($#,0.00);$-“)),**

**(“Currency(2)”,FORMAT(-3.1415926,”#,0.00;(#,0.00);-“)),**

**(“Currency(3)”,FORMAT(0,”$#,0.00;(#,0.00);-“)),**

**(“Date(1)”,FORMAT(DATE(2022,1,17),”yyyy-mm-dd”)),**

**(“Date(2)”,FORMAT(DATE(2022,1,17),”ddmmmyy”)),**

**(“Date(Q)”,FORMAT(DATE(2022,1,17),”QQyyyy”))**

**}**

![](<Base64-Image-Removed>)

It will return the following table with the value formatted as follows:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-format/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-format/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-format/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-format/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-format/#0 "close")

top