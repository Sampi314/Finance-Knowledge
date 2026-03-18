# Power BI Blog: {Missing Field or Column Breaking Query}, No Problem!

**Source:** https://sumproduct.com/blog/power-bi-blog-missing-field-or-column-breaking-query-no-problem/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: {Missing Field or Column Breaking Query}, No Problem!

*   July 29, 2020

Power BI Blog: {Missing Field or Column Breaking Query}, No Problem!
====================================================================

Power BI Blog: {Missing Field or Column Breaking Query}, No Problem!
====================================================================

30 July 2020

_Welcome back to this week’s edition of the Power BI blog series. This week,_ _we look_ _at how to deal with missing columns._

Has this ever happened to you?

You are creating a Power BI report where you pull data from a table:

![](<Base64-Image-Removed>)

For some obscure reason there are two columns for **CustomerKey** so you, being a good data modeller, remove the **CustomerKey2** column in the query culling redundant data from your table.

![](<Base64-Image-Removed>)

You load it up to Power BI and create your report. A couple of days later someone decides to “help out” and remove the extra **CustomerKey** column in the dataset without your knowledge. When the report is refreshed they get this error:

![](<Base64-Image-Removed>)

Great, someone has meddled with the source data, removed a column and is asking why is the query broken? They did not change anything!

Not to fear, there is a method that we can adopt to circumvent this from happening. But first lets go back and look at the ‘Query Editor’ to see what is going wrong. I’d like to draw your attention to the ‘**Removed Other Columns**‘ step in the ‘Applied Steps’ area:

![](<Base64-Image-Removed>)

The **Table.SelectColumns** command is written with the following syntax:

\= Table.SelectColumns(Table\_Name,{“Field 1”, “Field 2″…})

If the initial fields specified in the command are not present in the table the query will return with an error. That is what is breaking our query.

The **SelectColumns** command has an error trap built into it that is not commonly known. We can add a third parameter into the command that will instruct Power Query to perform an action if a field is missing. In this case we add ‘**MissingField.UseNull**‘ as our third parameter:

\= Table.SelectColumns(SalesTable\_Table,{“ProductKey”, “OrderDate”, “CustomerKey”, “SalesAmount”, “TaxAmt”, “Freight”, “Total Invoice”}, MissingField.UseNull)

Refreshing the query should result in this:

![](<Base64-Image-Removed>)

Power Query will populate the missing field with **null** values. This would allow subsequent dependent steps in the query to continue to work whilst treating the **CustomerKey** field as **null**.

Hopefully this tip can help queries you write not fall victim to rogue fields that “mysteriously disappear”. Of course, this isn’t the best solution, but used creatively with other measures in place **MissingField.UseNull** can prove to be an effective solution to missing fields.

That’s it for this week, come back next week for more on Power BI.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-missing-field-or-column-breaking-query-no-problem/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-missing-field-or-column-breaking-query-no-problem/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-missing-field-or-column-breaking-query-no-problem/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-missing-field-or-column-breaking-query-no-problem/#0)

[](https://sumproduct.com/blog/power-bi-blog-missing-field-or-column-breaking-query-no-problem/#0 "close")

top