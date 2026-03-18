# A technique to Average last 3 values where the values > 0

**Source:** https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0

---

Formula Forensics No. 035 Average the last 3 values greater than 0
==================================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 17 comments

  

A couple of weeks ago **Amanda** asked a question at [Chandoo.org](http://chandoo.org/wp/2009/04/28/calculate-moving-average/#comment-446514 "Amanda's Question")

“I need to calculate a moving average of the last 3 months.

However, if one of the months contains 0%, I want it to ignore that and take the last month that didn’t have a zero.

For instance, my data is this: April = 100%, May=0%, June=97%,July=98%, August=0%.

My formula is only looking at June July and August, but since August has a 0 I would like it to look at May June and July.

And since May has a 0, I would like it to look at April, June and July.”

I offered a solution which is an array formula.

\=AVERAGE(AVERAGEIFS($B$3:F3,$B$2:F2,LARGE(IF($B$3:F3>0,$B$2:F2),{1,2,3}))) Ctrl+Shift+Enter

Today I am going to try and explain what it is doing and how it works.

As always at Formula Forensics you can follow along with a sample file: [Download Here](https://chandoo.org/wp/wp-content/uploads/2013/10/Average-last-3-values.xlsx "Download Sample File")

The Problem
-----------

How do we write a formula to extract the last 3 non zero values?

What if there is more than 1 zero value?

What if the zero values are non-contiguous?

This can all be shown by:

**Average of the last 3 records – No Zeroes**

[![FF35_1](https://chandoo.org/wp/wp-content/uploads/2013/10/FF35_1.png)](https://chandoo.org/wp/wp-content/uploads/2013/10/FF35_1.png)

**Average of the last 3 records – One Zero in Current Month  
**

[![FF35_5](https://chandoo.org/wp/wp-content/uploads/2013/10/FF35_5.png)](https://chandoo.org/wp/wp-content/uploads/2013/10/FF35_5.png)

**Average of the last 3 records – One Zero**  **in a Previous Month  
**

[![FF35_2](https://chandoo.org/wp/wp-content/uploads/2013/10/FF35_2.png)](https://chandoo.org/wp/wp-content/uploads/2013/10/FF35_2.png)

******Average of the last 3 records –** Multiple Zeroes  
****

[![FF35_3](https://chandoo.org/wp/wp-content/uploads/2013/10/FF35_3.png)](https://chandoo.org/wp/wp-content/uploads/2013/10/FF35_3.png)

A Solution
----------

\=AVERAGE(AVERAGEIFS($B$3:F3,$B$2:F2,LARGE(IF($B$3:F3>0,$B$2:F2),{1,2,3}))) Ctrl+Shift+Enter

Normally at Formula Forensics we start in the inside of a formula and work out, but today we are going to start at the outside and work our way in.

The solution: \=AVERAGE(AVERAGEIFS($B$3:F3,$B$2:F2,LARGE(IF($B$3:F3>0,$B$2:F2),{1,2,3})))

This function is the Average() of an Averageifs() function.

What is going on here you ask ?

We know that the Average() function will average the constituent numbers. eg: =Average(6, 8, 10) = 8

But doesn’t Averageifs return a single number? The average of its components!

We’ll mostly, but not always.

Lets have a look:

If we remove the outside average and just look at the inner Averageifs() function

In the sample file, Cell F15 you will see:

\=AVERAGEIFS($B$3:F3,$B$2:F2,LARGE(IF($B$3:F3>0,$B$2:F2),{1,2,3})) Press **F2** then **F9**,

Excel evaluates this as:

\={0.5,0.9,0.7}

So the Averageifs() function is returning 3 values being 0.5, 0.9 & 0.7

These are the last 3 values greater than 0 ranked from latest to earliest by date

Which is exactly what Amanda asked us to average

So we will need to look inside the Averageifs() function to see what is going on.

The Syntax for the Averageifs() function is:

**AVERAGEIFS(average\_range, criteria\_range1, criteria1, \[criteria\_range2, criteria2\], …)**

in our example

**Average\_range** : $B$3:F3 This is the Values we want to average from teh start of the data up to the current cell

**Criteria\_range1** : $B$2:F2 This is the Date Range from the start of teh data up to the current cell

**Criteria1** : LARGE(IF($B$3:F3>0,$B$2:F2),{1,2,3}) This is a function that will return the 3 largest values shown by the array {1,2,3}

So in in English, the Averageifs function is being asked to return a single value from the Value row where the Date row matches the largest, second largest and third largest criteria. In each case Averageifs will average the number but as it is a single number it returns the value by itself.

Lets now step into the Large() function and see what is going on.

LARGE(IF($B$3:F3>0,$B$2:F2),{1,2,3})

The Large() function has the syntax =Large(Array, k)

In our example:

**Array**: IF($B$3:F3>0,$B$2:F2)

**k**: {1,2,3} This is an array and hence asks for the Largest (1), Second largest (2) and Third Largest (3) values

So we are getting the 3 largest values from the formula: IF($B$3:F3>0,$B$2:F2)

What is the IF($B$3:F3>0,$B$2:F2) formula doing?

If you put the formula IF($B$3:F3>0,$B$2:F2)

into a blank cell say **F31** and press **F9**

Excel returns: {41275,41306,41334,41365,FALSE}

These are the date values of the date row up to the Column we are working in

You can see these in Row 1 of the sample file

[![FF35_4](https://chandoo.org/wp/wp-content/uploads/2013/10/FF35_4.png)](https://chandoo.org/wp/wp-content/uploads/2013/10/FF35_4.png)

You will notice that there is a False value in the position of the Column which has the Value of 0%

This is derived by the If() Function.

The If() function is saying: IF($B$3:F3>0,$B$2:F2)

If the Value Row >0 ($B$3:F3>0), return the Date Row ($B$2:F2) else return False

The False isn’t shown in the formula, it is returned by Default when a False argument doesn’t exist

The standard Syntax for If is \=If(Criteria, Value when true, Value when false)

In our case we don’t have a Value when false component and so Excel simply places a false in as the answer.

Applying the formula using **Ctrl+Shift+Enter** forces Excel to Evaluate the formula as an Array Formula

What this means in practice is that the Formulas are evaluated 3 times as per the array {1,2,3} effectively extracting the last 3 values that match the last 3 dates where the Value is >0

What if I want to Average a Different Number of Days?
-----------------------------------------------------

You have two choices

### 1\. Change the Array Manually

If say you want to average the previous 5 values

You can modify the array manually

\=AVERAGE(AVERAGEIFS($B$3:F3,$B$2:F2,LARGE(IF($B$3:F3>0,$B$2:F2),{1,2,3,4,5}))) Ctrl+Shift+Enter

This is ok if it is not done regularly or is only slightly different to the existing array.

But if you want to setup the top twenty you need to type {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

Which is quite clumsy!

Bad Hint: You can copy the array from above.

Or you can automate it using the technique below.

### 2\. Insert a Formula to Setup the Array

You can add a small function that will automatically setup the array like:

\=AVERAGE(AVERAGEIFS($B$3:F3,$B$2:F2,LARGE(IF($B$3:F3>0,$B$2:F2),ROW(OFFSET($A$1,,,F39,1))))) Ctrl+Shift+Enter

This assume that cell **F39** has a number which is the number of periods you want to average

You can read more about how the ROW(OFFSET($A$1,,,F39,1)) part works in previous Formula Forensics posts

Download
--------

You can download a copy of the above file and follow along, [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2013/10/Average-last-3-values.xlsx "Download Sample File")
.

**[Other Posts in this Series](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensuics Homepage")
  
**
---------------------------------------------------------------------------------------------------------------------

The Formula Forensics Series contains a wealth of useful solutions and information.

You can learn more about how to pull Excel Formulas apart in the following posts: [http://chandoo.org/wp/formula-forensics-homepage/](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensics Homepage")

Two Challenges
--------------

### 1\. Can you solve this another way

Just after I posted my solution, Chandoo posted an alternative solution which you can read at:

[http://chandoo.org/wp/2009/04/28/calculate-moving-average/#comment-446559](http://chandoo.org/wp/2009/04/28/calculate-moving-average/#comment-446559 "http://chandoo.org/wp/2009/04/28/calculate-moving-average/#comment-446559")

**Can you solve this problem another way ?**

Let us know in the comments below:

### 2\. Your Challenge?

If you have a clever formula and would like to become an author here at Chandoo.org please consider writing it up as I have done above. Alternatively you can send the formula to either [Chandoo](http://chandoo.org/wp/about/ "Contact Chandoo")
 or [Hui](http://chandoo.org/wp/about-hui/ "Contact Hui")
.

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
| Written by Hui...  <br>Tags: [average()](https://chandoo.org/wp/tag/average/)<br>, [averageifs](https://chandoo.org/wp/tag/averageifs/)<br>, [if()](https://chandoo.org/wp/tag/if/)<br>, [large](https://chandoo.org/wp/tag/large/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 17 Responses to “Formula Forensics No. 035 Average the last 3 values greater than 0”

1.  ![](https://secure.gravatar.com/avatar/27cde7a44cbe4067f41943198576f83f97e23475619fd24c23e0fc53029e2b49?s=64&d=mm&r=g) [Sajan](http://chandoo.org/wp/category/posts-by-sajan/)
     says:
    
    [October 3, 2013 at 2:58 pm](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-447924)
    
    Hi Hui,  
    Nice write up!
    
    Here is one more approach, as an array formula:  
    \=AVERAGE(LOOKUP(LARGE(IF(Values,COLUMN(Values)),{1,2,3}), COLUMN(Values), Values))
    
    Cheers,  
    Sajan.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-447924)
    
2.  ![](https://secure.gravatar.com/avatar/7bbd3375773d818af330ee8e3ea6b839409e5281c0b66372301352a10fff8ad6?s=64&d=mm&r=g) Jason M says:
    
    [October 3, 2013 at 4:35 pm](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-447931)
    
    \=SUM(G4:INDEX(rng,LARGE(IF(rng>0,COLUMN(rng)-MIN(COLUMN(rng))+1),3)))/3
    
    Array-entered.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-447931)
    
3.  ![](https://secure.gravatar.com/avatar/7bbd3375773d818af330ee8e3ea6b839409e5281c0b66372301352a10fff8ad6?s=64&d=mm&r=g) Jason M says:
    
    [October 3, 2013 at 7:18 pm](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-447941)
    
    Or take out the hard-coded G4 and go with:
    
    \=SUM(INDEX(rng,MAX(COLUMNS(rng))):INDEX(rng,LARGE(IF(rng>0,COLUMN(rng)-MIN(COLUMN(rng))+1),3)))/3
    
    Array-entered.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-447941)
    
4.  ![](https://secure.gravatar.com/avatar/fa372ae2ae0b4063c593f2508015a4e433646256996cbc07aec12ea8d88e4a05?s=64&d=mm&r=g) Andrew says:
    
    [October 4, 2013 at 12:51 pm](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448002)
    
    Here's one that lets you specify the number of values to average in a cell (AvgNum):
    
    \=SUMPRODUCT((COLUMN(Values)>=LARGE(COLUMN(Values)\*(Values>0),AvgNum))\*(Values))/AvgNum
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448002)
    
    *   ![](https://secure.gravatar.com/avatar/fa372ae2ae0b4063c593f2508015a4e433646256996cbc07aec12ea8d88e4a05?s=64&d=mm&r=g) Andrew says:
        
        [October 9, 2013 at 8:53 am](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448514)
        
        Forgot to say that as this is SUMPRODUCT it doesn't need to be array entered.
        
        Also rather rather than using the date values to discern the order it assumes oldest to most recent is left to right, if you wanted right to left then replace the >=LARGE with <=SMALL, and if the values were vertical then swap the COLUMN formulas for ROW.
        
        I opted for this way as all you need are the values, they don't need to be linked to dates, and it doesn't need to be in a table or formatted any particular way.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448514)
        
        *   ![](https://secure.gravatar.com/avatar/80addca864830a337039849fb45f3f543a12027f5cc408b2909ad313ba62f04a?s=64&d=mm&r=g) Randy says:
            
            [November 19, 2015 at 1:47 am](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-1083754)
            
            Thanks for the formula!
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-1083754)
            
5.  ![](https://secure.gravatar.com/avatar/4c5edeee3dbd64a0c2cc5ac5c805b4d2b20956be9182befcad2f74614c9e76e4?s=64&d=mm&r=g) Narayana Murthy says:
    
    [October 6, 2013 at 6:44 pm](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448257)
    
    This trick is really great. Actually i came to know about the array formula through this post. I have hooked to array formula for the past three days .. have read nearly all the posts on array formula on your site... 🙂
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448257)
    
6.  ![](https://secure.gravatar.com/avatar/7301d599671545ca183da76efe0e3153ea1a6f073471883c1671e019774720ef?s=64&d=mm&r=g) Micah Dail says:
    
    [October 7, 2013 at 8:18 pm](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448374)
    
    \=AVERAGEIFS(tbl\[Value\], tbl\[Date\],">"&LARGE(((tbl\[Value\]0)\*tbl\[Date\]),4),tbl\[Value\],"0")
    
    That's my solution. I took the liberty of adding the data to a table in order to standardize it. One can easily change the "4" in the formula to adjust the range of the moving average.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448374)
    
    *   ![](https://secure.gravatar.com/avatar/7301d599671545ca183da76efe0e3153ea1a6f073471883c1671e019774720ef?s=64&d=mm&r=g) Micah Dail says:
        
        [October 7, 2013 at 8:24 pm](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448375)
        
        I just realized that I was missing the "" in the formula I typed in. Please see updated formula. As with others in this thread, this is array-entered. Also, to clarify what I posted, changing the "4" in the formula to a referenced cell will make short work of adjusting the moving average range.
        
        `=AVERAGEIFS(tbl[Value], tbl[Date],">"&LARGE(((tbl[Value]0)*tbl[Date]),4),tbl[Value],"gt.lt 0")`  
        swap gt.lt for Not Equal codes
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448375)
        
        *   ![](https://secure.gravatar.com/avatar/7301d599671545ca183da76efe0e3153ea1a6f073471883c1671e019774720ef?s=64&d=mm&r=g) Micah Dail says:
            
            [October 7, 2013 at 8:27 pm](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448377)
            
            Well it seems that the comments do not accept a "less than greater than" \[does not equal\] notation. In the formula, just insert this before the "0" within the quotations.
            
            Sorry about the spamming of the comment section; I just wanted to clarify my formula.
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448377)
            
7.  ![](https://secure.gravatar.com/avatar/64f3ca9031d8d6d04048ec2f41499646f58129752d4e1e3646103e8684042a97?s=64&d=mm&r=g) zurman says:
    
    [October 8, 2013 at 1:05 pm](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448450)
    
    Array formula are truly handy
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-448450)
    
8.  ![](https://secure.gravatar.com/avatar/1f39c1e022a70944a0c86aa0d590932e3038d7d9e98e378efd92b78466f1ca90?s=64&d=mm&r=g) ??? says:
    
    [October 16, 2013 at 2:06 am](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-449289)
    
    how about "=SUM((LARGE(IF($B$3:D3,$B$2:D2),{1;2;3})=$B$2:D2)\*$B$3:D3)/3" ctrl+shift+enter
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-449289)
    
9.  ![](https://secure.gravatar.com/avatar/782d23aa6d4f0ab0f33d6dfca7ae915e5bc3f158160245068717db22528c35e5?s=64&d=mm&r=g) ??? says:
    
    [October 16, 2013 at 2:09 am](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-449290)
    
    how about  
    “=SUM((LARGE(IF($B$3:D3,$B$2:D2),{1;2;3})=$B$2:D2)\*$B$3:D3)/3?  
    ctrl+shift+enter
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-449290)
    
10.  ![](https://secure.gravatar.com/avatar/1f39c1e022a70944a0c86aa0d590932e3038d7d9e98e378efd92b78466f1ca90?s=64&d=mm&r=g) dannny says:
    
    [October 16, 2013 at 2:13 am](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-449291)
    
    how about  
    “=SUM((LARGE(IF($B$3:D3,$B$2:D2),{1;2;3})=$B$2:D2)\*$B$3:D3)/3  
    ctrl+shift+enter
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-449291)
    
11.  ![](https://secure.gravatar.com/avatar/8743b27f6ad13dd54e7e1ee6012d8b251dee48664a078c85eff2148fd5fca216?s=64&d=mm&r=g) Ankit says:
    
    [November 8, 2013 at 5:20 am](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-452984)
    
    This is nice:)
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-452984)
    
12.  ![](https://secure.gravatar.com/avatar/130d41931f00fe883856191f8ee349122c7ff3ad0a6a6aec7d80762af8dd0ae0?s=64&d=mm&r=g) Adam says:
    
    [May 17, 2019 at 1:45 pm](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-1647817)
    
    I have a column that i need the last moving average of the last 21 rows that are not 0 averaged. But i also need it to get the average even if there is only 1 cell that isn't 0. So it would be
    
    D3 - Average  
    D4:D87 data that gets updated daily.
    
    I am not sure how to get this to work.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-1647817)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [May 18, 2019 at 4:49 am](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-1647890)
        
        @Adam
        
        Try: =AVERAGE(OFFSET(INDIRECT("$D"&MAX(($D$4:$D$87>0)\*ROW($D$4:$D$87))),,,-21,1)) Ctrl+Shift+Enter
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#comment-1647890)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-035-average-the-last-3-values-greater-than-0/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [PowerPivot – the ULTIMATE anti-bloat feature](https://chandoo.org/wp/powerpivot-the-ultimate-anti-bloat-feature/) | [Chandoo.org produces it’s Second MVP.](https://chandoo.org/wp/chandoo-org-produces-its-second-mvp/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)