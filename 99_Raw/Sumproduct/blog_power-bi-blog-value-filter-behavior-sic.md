# Power BI Blog: Value Filter Behavior (sic)

**Source:** https://sumproduct.com/blog/power-bi-blog-value-filter-behavior-sic/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Value Filter Behavior (sic)

*   January 1, 2025

Power BI Blog: Value Filter Behavior (sic)
==========================================

Power BI Blog: Value Filter Behavior (sic)
==========================================

2 January 2025

_Welcome back to this week’s edition of the Power BI blog series. This week, we discuss ‘Value Filter Behavior’._

**DAX** has an automatic filtering mechanism that occurs when multiple columns from the same table are filtered. This behaviour is informally called ‘auto-exist’. **DAX** understands that not all combinations of values across these columns are valid and as a result it automatically excludes invalid combinations. The **DAX** engine generated a coalesced value filter that not only returns valid combinations but also affects measured calculations. This month, Power BI is giving you more control over whether you want this behaviour in your semantic model. You can decide whether you want to turn off coalesced values filters and turn on independent value filters instead. Turning on independent value filters by setting the ‘Value filter behaviour’ setting to Independent _(see below)_ results in multiple filters on the same table being kept separate instead of the **DAX** engine combining these into one.

When you are filtering multiple columns on the same table, the current default value filter behaviour takes these filters and combines them into one, considering only the combinations that exist. Consider the following two columns on the same table:

1.  **Year**, which contains values like ‘2023’
2.  **Month**, which contains values like ‘January 2024’.

If you filter on both **Year** and **Month**, since these columns are on the same table, the value filter behaviour combines the filters into one, but only the combinations that exist are considered. Of course, the combination of the month January 2024 with year 2023 does not exist and would not be included in the filter. There are, however, situations in which the results are surprising.

Let’s look at an example, where we have a catalogue (**Catalog**) showing availability of colours for products by year. The manufacturer of these products has experimented with making products in various colours throughout the years:

![](https://sumproduct.com/wp-content/uploads/2025/05/38f0ac2589f2e1323efec9a2c9e1249b-1.jpg)

We have three \[3\] products that have been available in various colours over the years. Notice how there are no red products offered in 2024. That is going to be important a little later. Now, let’s count the number of products by adding the following measure:

**Number of Products = COUNTROWS( ‘Catalog’ )**

The following matrix shows the number of products that are available in various colours per year:

![](<Base64-Image-Removed>)

Now, let’s add another measure to calculate the total number of products for all years:

**Number of Products All Years = CALCULATE ( \[Number of Products\], ALL (  
‘Catalog'\[Year\] ) )**

Let’s put these measures side-by-side and filter to year 2023 and just the blue and red colours (no black). As you can see, the number of products is four \[4\] and the number of products across all years for these two colours is six \[6\]:

![](<Base64-Image-Removed>)

If we switch the Year to 2024, we expect the ‘Number of Products’ measure to return two \[2\], as there are just two products that are blue in 2024 and there are no red products in that year. Furthermore, we would expect that the number of products for all years will not change, because, after all, it is supposed to be calculated across all years. However, the ‘Number of Products for All Years’ changes from six \[6\] to five \[5\]:

![](<Base64-Image-Removed>)

The number of products across all years should still be six, not five. What we are seeing here is the value filter behaviour in action: it is combining filters on the same table, removing combinations that did not exist. The filters are **Year** = 2024 and **Color** = Blue or Red. Since these two filters are on the same table, these filters are combined into one filter that only filters for the combinations that exist. Since there are no red products in 2024, the applied filter is **Year** = 2024 and **Color** \= Blue. Therefore, the number of products for all years now counts just the number of blue products, not the blue or red products. This returns five \[5\], as you can confirm in the table.

This month sees Power BI giving you the control over whether you want this behaviour in your semantic model, by using the ‘Value filter behavior’ setting on your semantic model in the Properties pane in the Model view:

![](<Base64-Image-Removed>)

Three options are available:

**Automatic:** this is the default setting and currently turns on the Coalesced behaviour. When Microsoft wraps up this Preview, new models set to ‘Automatic’ will use Independent. There will be an announcement at that time

1.  **Independent:** this forces filters on the same table to be kept separate. After setting the ‘Value filter behavior’ setting to ‘Independent’, the total number of products for all years returns six \[6\] as expected (see below)
2.  **Coalesced**: this forces the value filter behaviour to be enabled for the semantic model and will result in combining the filters on the same table into one. The number of products for all years in the above example will continue to return five \[5\].
3.  The table below shows the impact of this setting on the illustration:

![](<Base64-Image-Removed>)

It should be noted that setting the ‘Value filter behavior’ to Automatic, means it is equal to Coalesced for now, but will be switched to Independent for new semantic models in the future.

If you set the ‘Value filter behavior’ to Independent, the number of products for all returns six \[6\], as expected, since the filters are **Year** = 2024 and **Color** = Blue or Red and are no longer combined:

![](<Base64-Image-Removed>)

That’s it for this week. In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-value-filter-behavior-sic/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-value-filter-behavior-sic/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-value-filter-behavior-sic/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-value-filter-behavior-sic/#0)

[](https://sumproduct.com/blog/power-bi-blog-value-filter-behavior-sic/#0 "close")

top