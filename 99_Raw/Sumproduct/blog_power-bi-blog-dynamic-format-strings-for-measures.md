# Power BI Blog: Dynamic Format Strings for Measures

**Source:** https://sumproduct.com/blog/power-bi-blog-dynamic-format-strings-for-measures/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Dynamic Format Strings for Measures

*   June 28, 2023

Power BI Blog: Dynamic Format Strings for Measures
==================================================

Power BI Blog: Dynamic Format Strings for Measures
==================================================

29 June 2023

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at the new dynamic format strings for measures._

Ever wanted to format a measure differently based upon a slicer selection or some other conditional way? Well now you can. This month’s update begins with the public Preview of dynamic format strings for measures.

In a measure, you define the measure itself with a DAX expression, but until now you could only provide that measure a static format string such as Currency, Whole number, Decimal, _etc_. or a type in the static format string, such as “dd MMM yyyy” for “09 Mar 2023”. With dynamic format strings (it doesn’t sound grammatically correct to me – I hope they aren’t “very hidden”!), you can create that format string also using a DAX expression. This provides you with the flexibility to adjust the format string to a variety of contexts within a report.

For example, a common scenario for this is currency conversion. If you have the currency format strings in your Currency table, you can define a DAX expression to use it. To add a dynamic format string to a measure, click the measure in the Data pane, then in the Measure tools ribbon Format dropdown choose ‘Dynamic’.

![](https://sumproduct.com/wp-content/uploads/2025/05/f889cf1a065f93d84ec049d27f249d98.jpg)

A new dropdown will appear to the left of the DAX formula bar, and it will be on ‘Format’. By default, whatever static format string corresponds to the previous Format dropdown will be pre-populated to get you started, but you can also delete it and use whatever DAX expression you want for your dynamic format string. In this example, it’s looking up the string from ‘Currency’ \[Currency Format\], and if that is ambiguous, then using

**“$#,0.00;($#,0.00);$#,0.00”**

![](https://sumproduct.com/wp-content/uploads/2025/05/f3d8431ae4e5e8359454d20d5e9a90d6.jpg)

If you want to get back to your measure DAX expression, you can change that left dropdown to ‘Measure’.

![](https://sumproduct.com/wp-content/uploads/2025/05/7480a75487389235d879efadf0110169.jpg)

Finally, if you want to remove the dynamic format string, go back to the Format dropdown, and choose any of the other options available. A warning dialog will appear as you will not be able to undo this action – so be careful!

![](<Base64-Image-Removed>)

Dynamic format strings are not new, and those of you who are familiar with calculation groups in SQL Server Analysis Services, Azure Analysis Services, and / or Power BI using external tools may know calculation items (supported in some tabular models, these can significantly reduce the number of redundant measures by grouping common measure expressions as calculation items) already have dynamic format strings. These same dynamic format string DAX patterns can now be utilized in individual measures in Power BI too.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-dynamic-format-strings-for-measures/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-dynamic-format-strings-for-measures/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-dynamic-format-strings-for-measures/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-dynamic-format-strings-for-measures/#0)

[](https://sumproduct.com/blog/power-bi-blog-dynamic-format-strings-for-measures/#0 "close")

top