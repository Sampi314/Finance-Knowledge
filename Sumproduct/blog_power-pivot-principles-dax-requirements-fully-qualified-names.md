# Power Pivot Principles: DAX Requirements – Fully Qualified Names

**Source:** https://sumproduct.com/blog/power-pivot-principles-dax-requirements-fully-qualified-names/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: DAX Requirements – Fully Qualified Names

*   November 5, 2018

Power Pivot Principles: DAX Requirements – Fully Qualified Names
================================================================

Power Pivot Principles: DAX Requirements – Fully Qualified Names
================================================================

6 November 2018

_Welcome back to our Power Pivot blog. Today, we go over when to use fully qualified names._

We’ve touched briefly on fully qualified names or column references [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-tips-on-calculated-columns)
. However, we thought we should take this opportunity to expand on fully qualified names and when they are required.

Just to recap, a fully qualified name of a column is the ‘Table Name’ followed by the \[Column Name\] encapsulated by square brackets:

![](<Base64-Image-Removed>)

DAX requires a fully qualified name to be used whenever a column reference is used as:

*   an argument in the **VALUES** function
*   an argument in the **ALL** or **ALLEXCEPT** function
*   a filter in the **CALCULATE** function
*   an argument in the **RELATEDTABLE** function
*   an argument in any time intelligence function (**DATEADD**, **TOTALYTD**).

Generally, it is always a good idea to use the fully qualified name whenever we are referring to columns, so don’t be lazy!

A separate point that we wish to address is the single quotation marks that encapsulate the table name ‘Product SubCategory’.

![](<Base64-Image-Removed>)

The table name above is enclosed in single quotation marks because the table name contains a space. This referencing convention is also applicable to tables with reserved keywords (such as DATE\_START), similarities with DAX functions or special characters (**.,;’:/\*|?&%$!+=()\[\]{}<>**).

That’s it for this week, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-dax-requirements-fully-qualified-names/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-dax-requirements-fully-qualified-names/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-dax-requirements-fully-qualified-names/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-dax-requirements-fully-qualified-names/#0)

[](https://sumproduct.com/blog/power-pivot-principles-dax-requirements-fully-qualified-names/#0 "close")

top