# Filter all records for November or 11AM or 2017 [quick tip] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/filter-all-records-for-november-or-11am-or-2017-quick-tip

---

Filter all records for November or 11AM or 2017 \[quick tip\]
=============================================================

[Quick Tip](https://chandoo.org/wp/category/quick-tip-2/)
 - 2 comments

  

_Imagine you are the first officer at ship terminal αε974F1 on remote planet Alderaan._ Your job involves looking at terminal log to see anomalies in time space continuum. So one day after getting to work late, thanks to crazy traffic on the floating super way in your settlement, you are looking at latest terminal log for αε974F1 on Excel (of course Excel, what else are you going to use? Notepad?!?) and **want to check all the records logged at 7 AM on _any day_**. You don’t have all the time in universe to filter records one at a time. You don’t want to write a formula or something else as it is too early in the morning and the nearest Starbucks is 7 light years away. So what would you do?

_**Use filters of course.**_

1.  Simply apply filters on your data (press CTRL+Shift+L to turn on filters)
2.  Click on the timestamp / data / time header and enter the time or date you want to search for.
3.  For example:
    1.  Type March to see all March entries
    2.  7AM to see all entries with 7AM  as hour part
    3.  2017 to see all entries logged in year 2017
    4.  Or use the arrow symbol at the end of search field to search by year / month / date etc.

Here is a quick demo of how date & time filtering works.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/filter-date-times-quick-tip-demo.gif)

**Wait a sec, what if I want to see all records for Monday?**

Alas, as of star date 11712.04 (that is December 4th, 2017), Excel hasn’t evolved to filter by Mondays. To do this, you have to extract weekday portion to another column and filter by that. You can use either =WEEKDAY(\[@Timestamp\]) or =TEXT(\[@Timestamp\],”DDDD”) to extract weekday portion of the date in numbers (1 to 7) or text (Sunday to Saturday).

**More filtering techniques**

It looks like a slow day at terminal αε974F1. Why not catch up on some Excel awesomeness while you wait for that hot brewed coffee from nearest starbucks to be teleported. Check out:

*   [Filter values where Fruit=Banana OR Sales >70. In Other Words, How to use Advanced Filters?](https://chandoo.org/wp/2011/10/10/how-to-use-advanced-filters/)
    
*   [How to Filter Odd or Even Rows only? \[Quick Tips\]](https://chandoo.org/wp/2011/01/05/how-to-filter-odd-or-even-rows-only-quick-tips/)
    
*   [Use Filter By Selected Cell’s Value to save time \[Quick Tips\]](https://chandoo.org/wp/2010/12/22/filter-by-selected-value/)
    
*   [What are Pivot Table Report Filters and How to use them?](https://chandoo.org/wp/2011/04/20/pivot-table-report-filters/)
    
*   More [quick tips](http://chandoo.org/wp/tag/quick-tip/)
    

_My job is here is done. Beam me up Scotty._

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Chandoo  <br>Tags: [data filters](https://chandoo.org/wp/tag/data-filters/)<br>, [date and time](https://chandoo.org/wp/tag/date-and-time/)<br>, [excel tables](https://chandoo.org/wp/tag/excel-tables/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [quick tip](https://chandoo.org/wp/tag/quick-tip/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 2 Responses to “Filter all records for November or 11AM or 2017 \[quick tip\]”

1.  ![](https://secure.gravatar.com/avatar/d190808411627ab069ca3991cb9c0b28024636299f1f0e8cc2f695c7aad7f496?s=64&d=mm&r=g) f(x)dx says:
    
    [December 4, 2017 at 10:09 am](https://chandoo.org/wp/filter-all-records-for-november-or-11am-or-2017-quick-tip/#comment-1526079)
    
    Well, indeed it is possible to filter all Mondays without additional column using conditional formatting.
    
    Assume dates are in column A, starting from cell A4.  
    Click Conditional formatting/ New rule/ Use a formula to determine which cells to format.  
    Then enter this formula =WEEKDAY(A4;2)=1 (relative reference!) and chose formating at your taste. For example yellow fill.  
    Copy paste format to all cells
    
    Then if you want to filter Mondays only - Filter by color and chose yellow filling
    
    [Reply](https://chandoo.org/wp/filter-all-records-for-november-or-11am-or-2017-quick-tip/#comment-1526079)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp/)
         says:
        
        [December 5, 2017 at 8:11 pm](https://chandoo.org/wp/filter-all-records-for-november-or-11am-or-2017-quick-tip/#comment-1526291)
        
        That is a good one. I would probably link the =1 part to a cell so that you can highlight other days.
        
        [Reply](https://chandoo.org/wp/filter-all-records-for-november-or-11am-or-2017-quick-tip/#comment-1526291)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-all-records-for-november-or-11am-or-2017-quick-tip/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Thank you, we have a home in New Zealand](https://chandoo.org/wp/thank-you-we-have-a-home-in-new-zealand/) | [5 conditional formatting top tips – Excel basics](https://chandoo.org/wp/conditional-formatting-top-tips/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)