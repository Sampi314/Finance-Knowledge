# Monday Morning Mulling: September 2019 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-september-2019-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: September 2019 Challenge

*   September 29, 2019

Monday Morning Mulling: September 2019 Challenge
================================================

Monday Morning Mulling: September 2019 Challenge
================================================

30 September 2019

_On the final Friday of each month, we set an Excel problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

Welcome to this month’s Monday Morning Mulling. Were you able to work around the error found in our [last blog](https://www.sumproduct.com/)
?

As a recap, we were presented with data similar to the following:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-354.jpg)

However, we want to present it as follows _automatically_:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-363.jpg)

This sounds like a job for Power Query, which is our recommended approach. Therefore, the first thing we’ll do is load the Table into the Power Query Editor, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-344.jpg)

It was hinted on Friday that this transformation fell in between an unpivot and a pivot. Well, I sort of lied – it’s actually _one of each_. First, we need to unpivot. Therefore, once in the Power Query Editor, we select the **Name** column only and then choose ‘Unpivot other columns’ from the ‘Unpivot columns’ dropdown in the Transform tab, as pictured:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-316.jpg)

Note you _don’t_ select the **Budget** and **Forecast** columns and unpivot them. If you do that, if the number of years were to be added, these columns wouldn’t be unpivoted. It’s safer to unpivot everything except for the Name field, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-272.jpg)

If more fields appear (_e.g._ **2021 Budget**, **2021 Forecast**, **2021 Variance**), these would automatically unpivot too.

Next, we want to split the **Attribute** column up into year and whether it is Budget or Forecast (in this instance). To do this, we should split the column at the space in each text string. This space is known as a _delimiter_, so it makes sense to select the **Attribute** column and then choose to split the column by delimiter as follows:

![](<Base64-Image-Removed>)

Bizarrely, this transformation is on the Home tab, not the Transform tab! Select the ‘By Delimiter’ option from the ‘Split column’ dropdown. This will generate the ‘Split Column by Delimiter’ dialog, where we will split on the first, left-most occurrence of the space delimiter.

![](<Base64-Image-Removed>)

This results in the **Attribute** column effectively being split in two:

![](<Base64-Image-Removed>)

We are nearly there. We’ve decomposed (so to speak!), now we need to “re-compose”. It’s time to select the **Attribute.2** column and use it for a pivot:

![](<Base64-Image-Removed>)

Having selected the **Attribute.2** column, select ‘Pivot column’ from the Transform tab. This gives rise to the ‘Pivot Column’ dialog:

![](<Base64-Image-Removed>)

Ensure that it is the **Attribute.2** column that is used to create new columns. Then, select the **Value** field as the ‘Values Column’ and choose ‘Sum’ as the ‘Aggregate Value Function’ in the ‘Advanced options’, all as pictured _(above)_. This will then pivot the **Attribute.2** column, creating two columns, **Budget** and **Forecast**, summing the values which relate to each context:

![](<Base64-Image-Removed>)

All that’s left to do now is rename the **Attribute.1** column to **Year** and load it back into Excel:

![](<Base64-Image-Removed>)

Simple! If you want to play along at home, you can check out our example file [here](https://sumproduct.com/assets/blog-pictures/2019/challenges-fff-mmm/sep-19/mmm/pivoted-data-example.xlsx)
.

_The Final Friday Fix will return on Friday 25 October with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-september-2019-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-september-2019-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-september-2019-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-september-2019-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-september-2019-challenge/#0 "close")

top