# Power BI Blog: Conditionally Formatting Brackets with Negatives

**Source:** https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-brackets-with-negatives/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Conditionally Formatting Brackets with Negatives

*   June 24, 2020

Power BI Blog: Conditionally Formatting Brackets with Negatives
===============================================================

Power BI Blog: Conditionally Formatting Brackets with Negatives
===============================================================

25 June 2020

_Welcome back to this week’s edition of the Power BI blog series. This week,_ _we look_ _at how to apply conditional formatting – specifically including brackets – to negative field values._

A commonly requested formatting style by accountants is to have negative numbers encapsulated with brackets in the report. Power BI inherently does not have such a formatting style. Therefore, we are going to have to be a little creative if we want to achieve the bracketed look.

Here is our dataset for this week:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-194-1.jpg)

Bringing in this data into Power BI and creating measures to calculate the total profit, we can then create the following visualisation:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-184-1.jpg)

We can see that for some days in January we have a negative profit amount (a loss), and we want to be able to display negative values with brackets around them. The trick here is to use the **FORMAT** function. Thisfunction has the following syntax:

**FORMAT(value, format\_string)**

where:

*   the **value** parameter is the measure or field that we want to format
*   the **format\_string** parameter is the format style that we want to apply to the field or measure.

The **format\_string** argument accepts code similar to the [custom number formatting](https://www.sumproduct.com/thought/number-formatting)
 codes in Excel:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-178-1.jpg)

With this knowledge borne in mind, let’s create the following measure:

**(Total Profit) Formatted =**

**FORMAT(**

        **\[Total Profit\],**

        **“#,###  ; (#,###)”**

    **)**

The ‘**#,###**‘ in the first section represents the format we want to apply to positive numbers, the next section separated by the semi-colon ‘**(#,###)**‘, is the code that we want to apply to negative numbers. The formatted measure now looks like this:

![](<Base64-Image-Removed>)

Success! Power BI now displays negative numbers with brackets around the value. Let’s fix the alignment so that the values are right justified. Select the visualisation, click on the Format tab under the Visualizations area, scroll down to ‘Field Formatting’. Here, select the **‘(Total Profit) Formatted’** measure and then select ‘Right’ in the Alignment options:

![](<Base64-Image-Removed>)

That’s how we format negative numbers with brackets in Power BI!

An important thing to note is that Power BI has styled the values as text and not numbers. Therefore, any calculations or measures built from this **‘(Total Profit) Formatted’** should be performed with the original measure **‘Total Profit’.**

That’s it for this week, come back next week for more on Power BI.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-brackets-with-negatives/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-brackets-with-negatives/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-brackets-with-negatives/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-brackets-with-negatives/#0)

[](https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-brackets-with-negatives/#0 "close")

top