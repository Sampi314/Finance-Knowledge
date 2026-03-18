# Power BI Blog: Field Parameters – Part 2

**Source:** https://sumproduct.com/blog/power-bi-blog-field-parameters-part-2/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Field Parameters – Part 2

*   September 14, 2022

Power BI Blog: Field Parameters – Part 2
========================================

Power BI Blog: Field Parameters – Part 2
========================================

15 September 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we continue looking at Field Parameters by showing how to edit existing Field Parameters._

Until recently, allowing users to dynamically change the dimensions and scales on charts in Power BI reports required some serious **DAX** knowledge. However, since the arrival of Field Parameters, there is a function specifically designed for this purpose. Users may dynamically adjust the measures or columns being analysed in a report by using Field Parameters. Even better, Field Parameters are easy to set up. We just choose the measures or columns the readers would want to change, and this feature can assist report readers to explore and personalise the report output.

Last time, we created our first Field Parameter:

![](<Base64-Image-Removed>)

Since the ‘Add slicer to this page’ option was selected, we created a slicer on the page as soon as we clicked on the Create button.

![](<Base64-Image-Removed>)

However, if we go back to where we created the Field Parameter, there is no option to manage existing parameters.

![](<Base64-Image-Removed>)

Existing Field Parameters appear in the Field pane:

![](<Base64-Image-Removed>)

They can be edited using the Formula bar, similar to any other measure:

![](<Base64-Image-Removed>)

The **DAX** code is:

**Choices = {**

    **(“Total Amount”, NAMEOF(‘Measures Table'\[Total Amount\]), 0),**

    **(“Total Sales”, NAMEOF(‘Measures Table'\[Total Sales\]), 1),**

    **(“% Var”, NAMEOF(‘Measures Table'\[% Var\]), 2)**

**}**

It is essentially a list of fields, the function **NAMEOF()** returns the name of the measure, and the number indicates the order, starting with zero \[0\].

If we had renamed any fields, the first name would change, for example if we had renamed ‘**Total Amount**‘ to **Total**:

**(“Total”, NAMEOF(‘Measures Table'\[Total Amount\]), 0),**

This means we can rename the fields in an existing Field Parameter in the same way. We may also add more fields and change the order by editing the **DAX** code and using the same format. If we wanted to add **Total Items** after **Total Sales**, the syntax would be:

**Choices = {**

    **(“Total Amount”, NAMEOF(‘Measures Table'\[Total Amount\]), 0),**

    **(“Total Sales”, NAMEOF(‘Measures Table'\[Total Sales\]), 1),**

    **(“Total Items”, NAMEOF(‘Measures Table'\[Total Items\]), 2),**

    **(“% Var”, NAMEOF(‘Measures Table'\[% Var\]), 3)**

**}**

Existing Field Parameters may also be viewed from the Data tab:

![](<Base64-Image-Removed>)

Another way we can edit the **DAX** code for the Field Parameter is to add a new column. Let’s say we want to add a new column which we will call **Category**. Note that the existing columns are separated in the **DAX** syntax by a comma \[**,**\]. We may use this syntax to add values for our new column:

![](<Base64-Image-Removed>)

The **DAX** code we have used is:

**Choices = {**

    **(“Total Amount”, NAMEOF(‘Measures Table'\[Total Amount\]), 0, “Sales”),**

    **(“Total Sales”, NAMEOF(‘Measures Table'\[Total Sales\]), 1, “Sales”),**

    **(“% Var”, NAMEOF(‘Measures Table'\[% Var\]), 2, “Percentage”)**

**}**

This creates a new column **Value4**, which we can rename to **Category**.

![](<Base64-Image-Removed>)

We can then add this level when we are using **Choices**:

![](<Base64-Image-Removed>)

We have now covered creating and editing Field Parameters; next time, we will look at them in action when we use them to dynamically impact visualisations.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-field-parameters-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-field-parameters-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-field-parameters-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-field-parameters-part-2/#0)

[](https://sumproduct.com/blog/power-bi-blog-field-parameters-part-2/#0 "close")

top