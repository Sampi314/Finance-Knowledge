# Power BI Blog: Field Parameters – Part 4

**Source:** https://sumproduct.com/blog/power-bi-blog-field-parameters-part-4/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Field Parameters – Part 4

*   September 28, 2022

Power BI Blog: Field Parameters – Part 4
========================================

Power BI Blog: Field Parameters – Part 4
========================================

29 September 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we continue looking at Field Parameters with an example using multiple Field Parameters._

Until recently, allowing users to dynamically change the dimensions and scales on charts in Power BI reports required some serious **DAX** knowledge. However, since the arrival of Field Parameters, there is a function specifically designed for this purpose. Users can dynamically adjust the measures or columns being analysed in a report by using Field Parameters. Even better, Field Parameters are easy to set up. We just choose the measures or columns the readers would want to change, and this feature can assist report readers to explore and personalise the report output.

In [Part 1](https://www.sumproduct.com/blog/article/power-bi-tips/field-parameters-part-1)
, we created our first Field Parameter:

![](https://sumproduct.com/wp-content/uploads/2025/05/c175d305eab539711617f9983c305c99.jpg)

Since the ‘Add slicer to this page’ option was selected, we created a slicer on the page as soon as we clicked on the Create button.

![](https://sumproduct.com/wp-content/uploads/2025/05/aad46d32d530285ccdcdae89b68cc669.jpg)

In [Part 2](https://www.sumproduct.com/blog/article/power-bi-tips/field-parameters-part-2)
, we looked at the **DAX** syntax of the Field Parameter and how to edit it.

![](https://sumproduct.com/wp-content/uploads/2025/05/089c2b20ea546e505c6ef8ec8f6100a4.jpg)

[Last time](https://www.sumproduct.com/blog/article/power-bi-tips/field-parameters-part-3)
, we looked at an example where an Area chart used the Field Parameter in the Y-axis.

![](https://sumproduct.com/wp-content/uploads/2025/05/ac60bd9d81373b53ff09288096df6c2b.jpg)

This week, we create another Field Parameter to use on a chart, using the same process as [Part 1](https://www.sumproduct.com/blog/article/power-bi-tips/field-parameters-part-1)
. This time, the Field Parameter includes fields from multiple tables:

![](https://sumproduct.com/wp-content/uploads/2025/05/b3c099ecc64d26f9afa1c8ac67ad961a.jpg)

We have

*   **Supplier** and **State** from **dSupplier**
*   **Fabric** from **dProduct**
*   **Buyer** from **dBuyer**
*   **Quarter** from **dCalendar**.

We change the order by clicking and dragging in the ‘Add and reorder fields’ section:

![](<Base64-Image-Removed>)

This time, we opt to create a Clustered column chart:

![](<Base64-Image-Removed>)

We drag **Category** to the X-axis, and **Choices** to the Y-axis.

![](<Base64-Image-Removed>)

We add slicers for both Field Parameters, which allows us to dynamically examine the data on the Clustered column chart from different perspectives:

![](<Base64-Image-Removed>)

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-field-parameters-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-field-parameters-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-field-parameters-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-field-parameters-part-4/#0)

[](https://sumproduct.com/blog/power-bi-blog-field-parameters-part-4/#0 "close")

top