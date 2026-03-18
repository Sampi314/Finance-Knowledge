# Power Pivot Principles: Disconnected Tables and Exchange Rates

**Source:** https://sumproduct.com/blog/power-pivot-principles-disconnected-tables-and-exchange-rates/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Disconnected Tables and Exchange Rates

*   August 13, 2018

Power Pivot Principles: Disconnected Tables and Exchange Rates
==============================================================

Power Pivot Principles: Disconnected Tables and Exchange Rates
==============================================================

14 August 2018

_Welcome back to our Power Pivot blog. Today, we discuss why disconnected tables may be useful in Power Pivot._

In our previous blog, [Power Pivot Principles: Calculating with Other Tables](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-calculating-with-other-tables)
, we highlighted how useful connected tables can be when creating measures. This time, we will cover a useful application of _dis_connected tables, using them to help calculate values in different currencies.

I’ll begin with creating the following table in Excel; note that the values in column **B** have to be derived through this formula:

**\=TEXT(A2,”0.00″)**

![](<Base64-Image-Removed>)

Once this table has been created, highlight it and convert the range into a Table (**CTRL + T**). The next step is to highlight the entire Table and copy it into Power Pivot. I have named this Table **_Exchange\_Rate_**. We can do this by going to the ‘Power Pivot’ tab on the Ribbon and selecting the ‘Add to Data Model’ option, _viz._

![](<Base64-Image-Removed>)

After adding the table to the Data Model, we can create a new PivotTable through Power Pivot with \[Sales\] by **_SalesTerritory_**:

![](<Base64-Image-Removed>)

Create a measure called **FX**:

**\=MAX(Exchange\_Rate\[A$ Per Euro\])**

![](<Base64-Image-Removed>)

Add a slicer on the **_Exchange\_Rate_** Table, on the ‘AUD Per Euro’ column.

![](<Base64-Image-Removed>)

Note the fact there are two “tables” called **_Exchange\_Rate_** – one referring to the Table itself and one to the table loaded into Power Pivot. We have selected the Power Pivot one in the image _(above)_.

This slicer does not manipulate the PivotTable, as the slicer updates the Table but not the PivotTable – this is because they are not connected!

What’s next? Well, let’s create a new measure:

**\=\[Sales\]/\[FX\]**

![](<Base64-Image-Removed>)

Now remove the other fields from the PivotTable’s ‘Values’ area so we just have the ‘Sum of SalesAmount’ and ‘Sales in Euros’.

![](<Base64-Image-Removed>)

Now, changing the slicer will automatically convert the sales amount into Euros!

That’s it for this week.

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-disconnected-tables-and-exchange-rates/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-disconnected-tables-and-exchange-rates/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-disconnected-tables-and-exchange-rates/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-disconnected-tables-and-exchange-rates/#0)

[](https://sumproduct.com/blog/power-pivot-principles-disconnected-tables-and-exchange-rates/#0 "close")

top