# Monday Morning Mulling: August 2024 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-august-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: August 2024 Challenge

*   September 1, 2024

Monday Morning Mulling: August 2024 Challenge
=============================================

Monday Morning Mulling: August 2024 Challenge
=============================================

2 September 2024

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for_ you _to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

**_The Challenge_**

We asked you to consider forecasting our company’s sales 10 years in advance. We had received specific sales estimates out to Year 5, but after that, we were simply provided with a growth rate. We wanted a formula that will simply calculate the sales for any particular period.

It wasn’t quite as simple as that though. For any period, we needed to be able to apply a sales discount, which will discount the sales by a set value. Additionally, it was important to note that the first period will always just take the value in the **Sales** ow less the sales discount. Finally, in the scenario where we were given both a sales value and a growth rate, the growth rate would need to override the value whilst in the scenario where neither were given, sales growth were to be assumed to be zero \[0\].

We challenged you to find the most efficient formula to calculate the sales for a given period. The question file is available for download [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/August/sp-sales-forecast---challenge.xlsx)
.

![](<Base64-Image-Removed>)

As always, there were some requirements:

*   the sales discount could not make the net sales lower than zero \[0\], and were only to be applied to the period it was specified in; it did not accumulate
*   it must be done with a single Excel formula, although it might need to be copied across for different periods
*   no **LAMBDA** or **LAMBDA** helper functions (_e.g_. **LET**, **BYROW** or **MAP**) were allowed
*   no Power Query or VBA were allowed; this was a formula challenge.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/August/sp-sales-forecast---suggested-solution.xlsx)
, which shows our suggested solution. The steps are detailed below.

**_Calculate the Sales without the Discount_**

The first step is to create a formula to calculate the sales without the discount. We need to ensure that any value in the **Sales****Growth** row is overriding any value in the **Sales** row. We need to make sure that this formula differentiates between a zero \[0\] and an empty cell for both the **Sales** and **Sales****Growth** rows. The formula we came up with is as follows:

**\=IF(J10=1,J11,IF(J12=””,IF(J11=””,I18,J11),I18\*(1+J12)))**

Firstly, it looks at the year, taking whatever the value is in **Sales** if the year is equal to one \[1\], _i.e._ it is the first year. Next, it checks if the **Sales****Growth** row is empty. If it’s not, the formula multiplies the **Sales Growth** by the previous **Sales** output. If it is empty, it does one more check to see whether the **Sales** value is empty. If it is it just assumes no growth, if not it takes the **Sales** value.

![](<Base64-Image-Removed>)

**_Subtract the Discount_**

The next step is to subtract the sales discount. While some of you may just look to subtract the value in the **Sales Discount** from our previously calculated formula, that doesn’t work as previous year’s sales discounts are then compounded when the growth rate is applied. Therefore, we need the formula to adjust for this, and apply the sales discount differently depending on whether it is using a value or growth rate. Additionally, we need to ensure that the net sales never drop below zero \[0\]. We produced the following formula:

**\=MAX(0,IF(J$10=1,J11,IF(J12=””,IF(J11=””,I18+I13,J11),(I18+I13)\*(1+J12)))-J13)**

In the situation where both **Sales** and **Sales Growth** are blank, we add back the previous period’s sales discount. If the **Sales Growth** is blank, we can just take the value in **Sales**.

Finally, when given a growth rate, we need to add back the previous period’s discount and then multiply the result by one \[1\] plus the growth rate. Then, outside of these functions we subtract the sales discount. Finally, the [**MAX**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-max-function)
 function around the outside limits the value to zero \[0\] in situations where the sales discount would push it negative. This will give us our **Net Sales**.

![](<Base64-Image-Removed>)

_The Final Friday Fix will return on 27 September 2024 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-august-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-august-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-august-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-august-2024-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-august-2024-challenge/#0 "close")

top