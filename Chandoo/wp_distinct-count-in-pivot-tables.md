# Distinct Count & Blanks - Power Pivot Real Life Example » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/distinct-count-in-pivot-tables

---

Distinct Count & Blanks – Power Pivot Real Life Example
=======================================================

[Power Pivot](https://chandoo.org/wp/category/power-pivot/)
 - 4 comments

  

When it comes to analyzing business data, managers are always asking, _**“so how many distinct x each y is doing?”**_

And that sends us, data analysts & reporting professionals running from pillar to post figuring out the best way to do it.

*   We can use variations of SUMPRODUCT, COUNTIFS etc, but the methods are not flexible..
*   We can use VBA, but it would become slow as you add more data.
*   We can use Pivot tables, but it only gives half of what we want _ie each y part, but not distinct count of x._
*   We might as well shave our head with a shovel before manually counting values.

**And that brings us to 2 distinctly simple solutions:**

*   Using Power Pivot & Excel 2010
*   Using regular pivot tables in Excel 2013

**Today, lets talk about these 2 approaches** & see why they are so better than anything else for distinct count situations.

### Distinct count problem faced by Joanne:

_**Joanne**_, one our readers sent me this email few days ago,

Here is something that I thought your readers might be interested in, as a real life business example. I always have the need for unique counts in my Excel sheets and was elated to find out that MS had built this function into 2013 pivot tables. I generally [use SUMPRODUCT](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
 to get to my answer, but some of my files take hours to calculate with this formula. Since I am still waiting for my 2013 CD to arrive, I took advantage of the addin to 2010 to play around with this new technology. At first, I was very excited at the ease of use to get to a unique number. But then looking into the results a little more, I found out it was skewed. Here is what I mean.

This is my data, simplified a little and any confidential information has been taken out. The last two columns are “helper” columns for my pivot. They basically return the agreement number if the proposal type is a certain value. If it doesn’t find a match, it leaves it blank. Data is sorted only so its easier to see how the pivot tables arrive at the answers.

![Distinct count using Excel Power Pivot - Sample data](https://img.chandoo.org/power-pivot/distinct-count-agreements-by-person-data.png)

The blank is what messes it up. Doing a simple pivot with DistinctCount, the numbers are definitely wrong. Its counting the blank fields as one of the items, so everything increases by one. The Grand Total is correct, sort of, but its misleading. There are 4 unique MBP accounts, 3 with actual agreement numbers and one blank, but looking at the numbers in the column, it doesn’t add up to 4 visually.

![Distinct count using Excel Power Pivot - including blanks](https://img.chandoo.org/power-pivot/distinct-count-including-blanks.png)

So there was my challenge, to get a DistinctCount, but ignoring all the blank fields within the data set. Using a New Measure, I was able to create a formula for the pivot that ignored the blank cells. It’s a little complex, but what good Excel formula isn’t? Once that was created, the pivot worked and the grand totals are more accurate. I did try using the DistintCount-1, but it didn’t come to the same answer. When it did work and the total was 1, it showed zero, which is correct. But I like the clean look below of showing nothing, thus not tempting the user to click on the zero.

`MBP formula: calculate(distinctcount(('Implemented'[MBP Accounts])), filter(Implemented,Not(isblank('Implemented'[MBP Accounts]))))`

![Distinct count using Excel Power Pivot - excluding blanks](https://img.chandoo.org/power-pivot/discintc-count-excluding-blanks-power-pivot-excel-2010.png)

### Distinct Count Problem & various solutions

**I think Joanne’s measure for Distinct count is excellent**. It shows how easily we can calculate anything we want [using Power Pivot](http://chandoo.org/wp/2013/01/21/introduction-to-power-pivot/ "What is Power Pivot – an Introduction ")
.

But do you know we can modify it and use various other solutions as well?

In the below video, I have explained 3 different solutions and how they fare.

1.  Joanne’s original CALCULATE (… FILTER(…)) solution
2.  Improved CALCULATE(…) solution
3.  Using Excel 2013 regular pivot tables to calculate DISTINCT Counts

### Watch the Distinct Count using Power Pivot & Pivot tables video \[17 min\]

**Go ahead and [watch this video](http://chandoo.org/wp/resources/distinct-count-power-pivot/)
**. This is just a sample of what you get when you join our Power Pivot course.

[![Distinct Count calculations using Power Pivot for Excel & more](https://img.chandoo.org/power-pivot/distinct-count-examples-using-power-pivot-video.png)](http://chandoo.org/wp/resources/distinct-count-power-pivot/)

### Download Example workbooks:

Click below links to download example workbooks shown in this lesson:

*   [Excel 2010 version](https://img.chandoo.org/power-pivot/DistinctCount%20Sample.xlsm)
    
*   [Excel 2013 version](https://img.chandoo.org/power-pivot/distinct-count-of-accounts.xlsx)
    

### Thank you Joanne

Thank you so much Joanne for sharing this example with us. It was fun learning from your example & exploring alternative solutions.

**If you enjoyed this example, say thanks to _Joanne_**.

### Want to learn more? Join our Power Pivot Classes

**If you would like to learn more about Power Pivot, then please consider joining my new course – Power Pivot online classes.** The objective of this class is to make you a data analysis & dashboarding monster.

We are in enrollment stage now and we will be starting online classes from 18th of February. All classes will be pre-recorded so that you can watch them at your own time.

[**Click here to learn more & join us**](http://chandoo.org/wp/resources/learn-power-pivot/ "Advanced Excel & Power Pivot Training Classes")
.

[![Online Power Pivot & Excel Dashboard classes from Chandoo.org](https://cache.chandoo.org/images/pp/power-pivot-course-ex-m2.png)](http://chandoo.org/wp/resources/learn-power-pivot/)

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
| Written by Chandoo  <br>Tags: [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)<br>, [calculate()](https://chandoo.org/wp/tag/calculate/)<br>, [distinct count](https://chandoo.org/wp/tag/distinct-count/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [duplicates](https://chandoo.org/wp/tag/duplicates/)<br>, [excel 2013](https://chandoo.org/wp/tag/excel-2013/)<br>, [FILTER()](https://chandoo.org/wp/tag/filter/)<br>, [measures](https://chandoo.org/wp/tag/measures/)<br>, [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)<br>, [powerpivot](https://chandoo.org/wp/tag/powerpivot/)<br>, [slicers](https://chandoo.org/wp/tag/slicers/)<br>, [videos](https://chandoo.org/wp/tag/videos/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 4 Responses to “Distinct Count & Blanks – Power Pivot Real Life Example”

1.  ![](https://secure.gravatar.com/avatar/f95eecbaa06ecc214b848a46793deb2d7264beb153ee07a9443bd61926e6808f?s=64&d=mm&r=g) [Manish Jain](http://aapkapoll.com/)
     says:
    
    [February 19, 2013 at 4:08 am](https://chandoo.org/wp/distinct-count-in-pivot-tables/#comment-414796)
    
    Nice !!!
    
    [Reply](https://chandoo.org/wp/distinct-count-in-pivot-tables/#comment-414796)
    
2.  ![](https://secure.gravatar.com/avatar/e55043f60fc157b472d9d56bb26d33e17ad87d342e80c6294fbbfa3d52ee8924?s=64&d=mm&r=g) Nikolay says:
    
    [March 28, 2013 at 9:51 am](https://chandoo.org/wp/distinct-count-in-pivot-tables/#comment-421413)
    
    If you do the text to columns function (this way the pivot table treats the blanks as blanks), on the data and pivot it afterwords you get the right results. No need for the complex formulas
    
    [Reply](https://chandoo.org/wp/distinct-count-in-pivot-tables/#comment-421413)
    
3.  ![](https://secure.gravatar.com/avatar/2927db86f52b04d3b427a7e6c4f664bede4e63a5a0d1e9a69bb40d414a86f689?s=64&d=mm&r=g) Colin says:
    
    [April 30, 2013 at 11:45 pm](https://chandoo.org/wp/distinct-count-in-pivot-tables/#comment-428157)
    
    i think we're trying to find a way to leave the formula(ae) intact and not count blanks. the only way text-to-columns works is if you turn the offending cell(s) into text first, which defeats the purpose.
    
    [Reply](https://chandoo.org/wp/distinct-count-in-pivot-tables/#comment-428157)
    
4.  ![](https://secure.gravatar.com/avatar/16d8436dd78a031be9792507a5ecd0342f4e88df961e20d245596366b1b45313?s=64&d=mm&r=g) ray says:
    
    [June 2, 2020 at 4:24 am](https://chandoo.org/wp/distinct-count-in-pivot-tables/#comment-1803665)
    
    I spent AGES trying to get this to work! THANK YOU!!!!!!!!! BLYAAAAAAAAAAAAAT
    
    [Reply](https://chandoo.org/wp/distinct-count-in-pivot-tables/#comment-1803665)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/distinct-count-in-pivot-tables/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Formula Forensics No. 033 – Interpolation](https://chandoo.org/wp/formula-forensics-no-033/) | [Shading above or below a line in Excel charts \[tutorial\]](https://chandoo.org/wp/shaded-line-charts-excel/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)