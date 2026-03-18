# Power Pivot Principles: Getting the Measure of a Measure – Multiple Measure Management

**Source:** https://sumproduct.com/blog/power-pivot-principles-getting-the-measure-of-a-measure-multiple-measure-management/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Getting the Measure of a Measure – Multiple Measure Management

*   November 23, 2020

Power Pivot Principles: Getting the Measure of a Measure – Multiple Measure Management
======================================================================================

Power Pivot Principles: Getting the Measure of a Measure – Multiple Measure Management
======================================================================================

24 November 2020

_Welcome back to the Power Pivot Principles blog. This week, we will consider where to store measures when you have many measures and tables in your database._

Whether we are working in Excel or Power BI, sometimes the number of tables in our database can get – shall we say? – a little “disorganised”, _e.g._

![](<Base64-Image-Removed>)

It’s neither neat nor tidy, but we can often not see the wood for the trees. If you have been following [this series](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
, you will note we stress time and time again that you should not add calculated columns, but instead use measures to aggregate and report upon data. The problem is the number of measures can quickly get out of hand. Measures are there to be used – _repeatedly_ used – so they need to be robust, flexible and, quite frankly, filed well (so you can find them!).

There are two schools of thought as to how best to do this. Measures need a home. They are stored in tables within your database. The question is, which table(s) should you store them in?

One alternative is to have measures reside in the same table as the (the majority of) the data it summarises. For example, consider the following:

![](<Base64-Image-Removed>)

Here, we are in the Power Pivot window (in Excel, rather than Power BI), specifically, in the **Sales** tab (_i.e._ in the **Sales** table), circled _(bottom left)_. There are other tables (_e.g._ **Customer**, **Product**, **FX**, …), but we can clearly see we have measures residing in **Sales**. They may be made visible by pressing the ‘Calculation Area’ button _(top right, highlighted)_, and we have taken the liberty of highlighting their position accordingly.

These may be individually cut and pasted into a ‘Calculation Area’ of another tab / table, or by returning to Excel, going to the ‘Power Pivot’ tab, and selecting ‘Manage Measures…’ from the ‘Measures’ dropdown, _viz._

![](<Base64-Image-Removed>)

Then, having selected a measure and clicking ‘Edit’, we can choose the ‘Table name:’ where we wish to move it to:

![](<Base64-Image-Removed>)

That’s easy enough, and for many, this makes perfect sense. This works fine when measures are unambiguous. However, what happens when it becomes a judgment call? For example, if we calculate **Sales in Euros** as a measure, should we place this in the **Sales** table or the **FX** table? This can be especially confusing for end users, whose views may differ from the measure creator’s. Also, what happens if we need to remove a table? This can be cumbersome if we need to retain the measures and there are many of them.

The second alternative is to create a blank table, where **_all_** measures are stored. At least you have them in one place and they may be found, once sorted. To achieve this, first create a table in Excel, _e.g._

![](<Base64-Image-Removed>)

Here, this has been called the one-field Table **Measures**, and the only field has been named **Null** to remind users this is deliberately empty.

We then highlight this Table and copy (**CTRL + C**) and then in the Power Pivot window, we paste (it doesn’t matter which table / tab you are in: a new tab will be created) using the big ‘Paste’ button (**CTRL + V** will not work).

![](<Base64-Image-Removed>)

You will need to rename the Table:

![](<Base64-Image-Removed>)

You will find you CANNOT name your table **Measures**! Once you have changed the name (we have chosen **Custom Measures**), you will then have a repository where all the measures for the entire database may be stored:

![](<Base64-Image-Removed>)

There are arguments for and against both approaches. This second option is useful so you know where all the measures are (there is no confusion), but an inexperienced end user may see there is no data and think it better to delete the table (and the stored measures too!). The trick is to make a deliberate call as to which is the more appropriate approach in the given circumstances.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-getting-the-measure-of-a-measure-multiple-measure-management/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-getting-the-measure-of-a-measure-multiple-measure-management/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-getting-the-measure-of-a-measure-multiple-measure-management/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-getting-the-measure-of-a-measure-multiple-measure-management/#0)

[](https://sumproduct.com/blog/power-pivot-principles-getting-the-measure-of-a-measure-multiple-measure-management/#0 "close")

top