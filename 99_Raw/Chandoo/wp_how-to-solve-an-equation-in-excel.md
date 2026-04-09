# How to Solve an Equation in Excel

**Source:** https://chandoo.org/wp/how-to-solve-an-equation-in-excel

---

How to Solve an Equation in Excel
=================================

[Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 31 comments

  

This week at the [Chandoo,org Forums](http://chandoo.org/forum/threads/how-to-solve-an-equation-in-excel.12071/)
, **Usman** asked,

_“ I have a curve. I did its fitting using Excel and got an equation._

_y = 2E+07x^-2.146_

_For y=60 what will be the value of x?_

_How can we solve this equation using Excel? ”_

Lets look at how this can be solved using Excel.

### Define the Problem

Usman formula is y = 2E+07x^-2.146

or expanded y = 2\*10^7\*x^-2.146

We can use Excel’s Goal Seek function to assist us here

Goal Seek is located in the **Data**, **What-If Analysis**, **Goal Seek** menu

[![GS00](https://chandoo.org/wp/wp-content/uploads/2013/09/GS00.png)](https://chandoo.org/wp/wp-content/uploads/2013/09/GS00.png)

Goal Seek is an inbuilt function in Excel that searches for a solution to a model/formula by iteratively trying source cell values until a solution is found.

Before we start, Excel doesn’t understand the concepts of x and y, but we can use cells for these instead

To use Goal Seek we need to put our formula into a cell.

Start a new file and in **C3** (our y cell) type:  = 2\*10^7\*B3^-2.146

In **B3** (our x cell): Put a value say 10

[![GS02](https://chandoo.org/wp/wp-content/uploads/2013/09/GS02.png)](https://chandoo.org/wp/wp-content/uploads/2013/09/GS02.png)

Note that **C3** will show the solution of the formula for when x=10 or = 2\*10^7\*10^-2.146 = 142,899.277

[![GS01](https://chandoo.org/wp/wp-content/uploads/2013/09/GS01.png)](https://chandoo.org/wp/wp-content/uploads/2013/09/GS01.png)

### Using Goal Seek

To use Goal Seek to find what value of x (**B3**) will result in y (**C3**) = 60,

Select **C3**

Goto the **Data**, **What-If Analysis**, **Goal Seek** menu

[![GS03](https://chandoo.org/wp/wp-content/uploads/2013/09/GS03.png)](https://chandoo.org/wp/wp-content/uploads/2013/09/GS03.png)

Set Cell: **C3**  – This is our y value cell

To value: **60**  This is the value we want to achieve

By changing cell: **B3** – This is our x value cell

Click OK when ready

[![GS04](https://chandoo.org/wp/wp-content/uploads/2013/09/GS04.png)](https://chandoo.org/wp/wp-content/uploads/2013/09/GS04.png)

Excel shows us that it has found a solution and that y (**C3**) \=60 when x (**B3**) = 374.60

Select **OK** to save the result

Select **Cancel** to return to the previous value

You can download a sample of the above here: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2013/09/Goal-Seek-Sample.xls "Goal seek sample File")

How have you solved Formulas using Excel or other techniques
------------------------------------------------------------

How have you solved Formulas using Excel or other techniques?

Let us know in the comments below:

**Learn more about Goal seek and solver:**

*   [Introduction to Goal seek and building a retirement calendar](http://chandoo.org/wp/2009/07/29/excel-goal-seek-tutorial/)
    
*   [Introduction to Solver](http://chandoo.org/wp/2010/10/15/excel-solver-tutorial/)
    
*   [Using solver to assign items to buckets](http://chandoo.org/wp/2011/05/11/using-solver-to-assign-item/)
    

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
| Written by Hui...  <br>Tags: [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [goal seek](https://chandoo.org/wp/tag/goal-seek/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 31 Responses to “How to Solve an Equation in Excel”

1.  ![](https://secure.gravatar.com/avatar/5d411a6140d6a66f801426c213d9fee20987de54bd392b3c9c8c7b1e38c7b0cc?s=64&d=mm&r=g) Vitalie says:
    
    [September 19, 2013 at 8:06 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-446447)
    
    I've used goal seek to solve equations, but it is not very useful when there are several possible solutions and one needs them all. I also have used trendlines in charts to find the equation for the line of best fit. Not quite the same as solving equations, but easier than running linear regressions to find the same result.
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-446447)
    
2.  ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
    
    [September 19, 2013 at 8:09 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-446449)
    
    Yes! I have solved a variety of equations using various techniques. The one I like to demonstrate, though, is the solution of relatively complexsimultaneous equations using
    
    \=MINVERSE() and =MMULT() functions
    
    I also solve simultaneous equations in a work sheet using the substitution method as it is direct and easy to program!
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-446449)
    
3.  ![](https://secure.gravatar.com/avatar/18373c8c92f400b42228a5fe419268fa23a1a13d2a06e34d9b2fbed4288ddef0?s=64&d=mm&r=g) [Mike Woodhouse](http://grumpyop.wordpress.com/)
     says:
    
    [September 19, 2013 at 9:32 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-446455)
    
    I tried two alternative approaches:
    
    first, good old algebra (my kids are doing a lot of expression rearranging at school just now)...
    
    So x = (y / 2\*10E+07) ^ (-1/2.146)
    
    second, I've been playing with a little program called "Calca" ([http://calca.io](http://calca.io/)
    ). It's a little hard to describe (but only costs $9.99 to try) but think of a text document that understands math and recalculates on the fly. Something like that. So I start by typing:
    
    y = 2\*10^7\*x^-2.146
    
    which let's me use the "evaluate" operator, "=>". I type "x =>" (without the quotes) and calca adds what it knows:
    
    x => 2524.3961/y^0.466
    
    .. so it restates the expression in terms of y. Pretty cool. For a solution, I typed
    
    60 = 2\*10^7\*x^-2.146
    
    and then asked for x:
    
    x=> 374.6009
    
    It's a fun little program. The Windows version is only semi-officially available and there's no obvious link on the site, but I found it here: [http://calca.io/store](http://calca.io/store)
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-446455)
    
    *   ![](https://secure.gravatar.com/avatar/e2cda6bb869114f1dc685c4e3ac122530a01cd08b5ecce786b213a259374dec9?s=64&d=mm&r=g) Andreas says:
        
        [September 20, 2013 at 8:51 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-446565)
        
        This.
        
        While I appreciate the craftiness of teaching to use Excel's Goal Seek function to solve an equation, I find it somewhat dangerous. I'm aware that the question explicitly asked to use Excel for this, but I would liken the answer to teaching a hungry man to fish -- with dynamite!
        
        If you need to do algebra but have trouble dealing with formulas, you should try to polish up your algebra, ask someone who does, or use a software package like suggested above. When you are handling algebraic formulas by applying tricks and hacks, you are bound to make mistakes which will bite you later.
        
        So, how do you arrive at a solution by using school algebra?
        
        The goal is to have x standing on one side, and the rest on the other side.
        
        Starting with  
        y = 2\*10^7\*x^-2.146,  
        you can move the factor "2\*10^7" to the left by dividing by 2\*10^2:  
        y/(2\*10^7) = (2\*10^7\*x^-2.146)/(2\*10^7)  
        y/(2\*10^7) = x^-2.146  
        The next step is a little trickier. You need to get rid of the exponent "-2.146" on the right side. If the exponent were "2", we know that we could simply extract the square root. Analogously, in our case, we would need to extract the "-2.146"th root. But there's no function to extract an arbitrary root. We need to know that, in the example of square roots, "extracting the square root of a value" is the same as "raising the value to 1/2". In short, sqrt(4)=4^(1/2). Correspondingly, "extracting the '-2.146'th root" is the same as raising to "1/-2.146", which is the same as -1/2.146. That's what we need to do to get rid of the exponent on the right side:  
        (y/(2\*10^7))^(-1/2.146) = (x^-2.146)^(-1/2.146)  
        (y/(2\*10^7))^(-1/2.146) = x  
        Swap left and right sides and we get:  
        x = (y/(2\*10^7))^(-1/2.146)
        
        [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-446565)
        
4.  ![](https://secure.gravatar.com/avatar/7c9167d17902152de4206e1887176da2c241e7aae92c86a960c9a9e837ca5127?s=64&d=mm&r=g) Kiev says:
    
    [September 24, 2013 at 5:29 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-447021)
    
    I heard of this function but never tried it before, but this simple explanation give me more thought about it, i will dig into it further & learn more your other related posts. thanks so much. chandoo...
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-447021)
    
5.  ![](https://secure.gravatar.com/avatar/7bbd3375773d818af330ee8e3ea6b839409e5281c0b66372301352a10fff8ad6?s=64&d=mm&r=g) Jason M says:
    
    [September 25, 2013 at 3:24 pm](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-447139)
    
    I learned how to solve simultaneous equations in Excel from Alan Beban's posts many years ago using MINVERSE and MMULT (same thing Duncan is describing). I have actually used it a few time in my work.
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-447139)
    
6.  ![](https://secure.gravatar.com/avatar/b31bf9ec58a49fe8fbdb95f0304ab1675a708031b5b48c37b8df71b704effdfc?s=64&d=mm&r=g) Ryan C says:
    
    [August 27, 2015 at 6:52 pm](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1032082)
    
    Great stuff!! I really appreciate the step by step with images!! Super helpful!!
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1032082)
    
7.  ![](https://secure.gravatar.com/avatar/8a7dbf08c27ed6f415b5f670d1f5018742c319457d382f5c48f6b161c5086b77?s=64&d=mm&r=g) Monika says:
    
    [December 31, 2015 at 2:25 pm](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1114597)
    
    used the goal seek function to solve for equation  
    a= CF\*1/(1+x)^1+CF\*1/(1+x)^2+.......+CF\*1/(1+x)^n for a changing 'a'.  
    Quite clean and helpful.  
    Thanks !
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1114597)
    
8.  ![](https://secure.gravatar.com/avatar/2a680d6038bfd85bc5bcd439d575e97910251fa39af0f2a3b063d03c84c8ce61?s=64&d=mm&r=g) rahul sudan says:
    
    [January 6, 2016 at 7:16 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1116767)
    
    I need to create a function with regular addition and subtraction of digits to/from a variable, say "x". as I type x in the cell i get result as "#value!" instead of "x-2" . What should i do?
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1116767)
    
    *   ![](https://secure.gravatar.com/avatar/2a680d6038bfd85bc5bcd439d575e97910251fa39af0f2a3b063d03c84c8ce61?s=64&d=mm&r=g) rahul sudan says:
        
        [January 6, 2016 at 7:25 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1116770)
        
        This is urgent. If you can help!
        
        [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1116770)
        
        *   ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
            
            [January 6, 2016 at 3:47 pm](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1116892)
            
            This is probably a formatting error where Excel thinks a number is a text character. If you post an example of your work it will help us to help you
            
            [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1116892)
            
            *   ![](https://secure.gravatar.com/avatar/2a680d6038bfd85bc5bcd439d575e97910251fa39af0f2a3b063d03c84c8ce61?s=64&d=mm&r=g) rahul sudan says:
                
                [January 7, 2016 at 10:13 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1117184)
                
                Sorry. I do not know how to post my excel sheet here for example. I have made .jpg but how to post?
                
                [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1117184)
                
                *   ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
                    
                    [January 8, 2016 at 6:31 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1117482)
                    
                    Send it to me at duncanwil at gmail dot com and I will report back here
                    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [January 8, 2016 at 8:06 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1117529)
        
        @Rahul
        
        For urgent questions start a post at the Chandoo.org Forums  
        [http://forum.chandoo.org/](http://forum.chandoo.org/)
        
        Attaching a sample file will get you a quicker response
        
        [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1117529)
        
        *   ![](https://secure.gravatar.com/avatar/2a680d6038bfd85bc5bcd439d575e97910251fa39af0f2a3b063d03c84c8ce61?s=64&d=mm&r=g) rahul sudan says:
            
            [January 8, 2016 at 9:35 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1117541)
            
            I have sent excel jpg at [duncanwil@gmail.com](mailto:duncanwil@gmail.com)
            . Please check and reply!
            
            [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1117541)
            
9.  ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
    
    [January 11, 2016 at 1:34 pm](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1118704)
    
    I have replied to Rahul off list but have not had a response as yet.
    
    I accept that Rahul could have uploaded his work here but since he didn't, all's still well I think.
    
    I have to wait for Rahul to reply otherwise anything I say might be pointless ... and not the answer to his question!
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1118704)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [January 14, 2016 at 2:56 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1119723)
        
        Duncan
        
        I have responded to you and Rahul directly via email  
        with no response?
        
        [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1119723)
        
        *   ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) Duncan Williamson says:
            
            [January 14, 2016 at 3:01 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1119726)
            
            Rahul and I are still chatting. I think the problem is solved but I am waiting for Rahul's final say so.
            
            [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1119726)
            
        *   ![](https://secure.gravatar.com/avatar/2a680d6038bfd85bc5bcd439d575e97910251fa39af0f2a3b063d03c84c8ce61?s=64&d=mm&r=g) rahul sudan says:
            
            [January 14, 2016 at 8:14 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1119861)
            
            Thanks a lot.
            
            My problem is solved through another method.
            
            Kudos!
            
            [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1119861)
            
10.  ![](https://secure.gravatar.com/avatar/3aa7292f77370e4f7df554994191edbc044cee18311009cdb45c18371797fb89?s=64&d=mm&r=g) oihonde says:
    
    [August 5, 2016 at 6:05 pm](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1246816)
    
    Hi,
    
    I have a table in excel. I have a total sum with 6 countries and % each of these countries represent of the whole. Also within same table I have 5 segments with percent of of segment as a whole and then percent by each country with breakdown % allocated by segment. I know the total value and I am trying to populate table so values tie out on coulmns to equal country sum and then on rows to sum to segment sum. Not sure if this makes sense but been struggling for hours with this!!! Help please
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1246816)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [August 6, 2016 at 7:21 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1247496)
        
        @Oihonde
        
        Can you please ask the question in the chandoo.org Forums  
        [http://forum.chandoo.org/](http://forum.chandoo.org/)
        
        Please attach a sample file to give a more targetted answer
        
        [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1247496)
        
11.  ![](https://secure.gravatar.com/avatar/0d33e885ff97846cc943206fa785f7089f60bde4302476b5a285d512272c7267?s=64&d=mm&r=g) Brainapsyl Review says:
    
    [January 25, 2017 at 11:42 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1398691)
    
    Some genuinely fantastic posts on this web site, thanks for contribution.
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1398691)
    
12.  [#Excel Super Links #10 – shared by David Hager | Excel For You](https://dhexcel1.wordpress.com/2017/04/21/excel-super-links-10-shared-by-david-hager/)
     says:
    
    [April 21, 2017 at 2:39 pm](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1438948)
    
    \[…\] [http://chandoo.org/wp/2013/09/19/how-to-solve-an-equation-in-excel/](http://chandoo.org/wp/2013/09/19/how-to-solve-an-equation-in-excel/)
     \[…\]
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1438948)
    
13.  ![](https://secure.gravatar.com/avatar/bd45763c1b9e337766d093af39506d707e098cc9aca67561e7efd2655e0cf265?s=64&d=mm&r=g) jithin says:
    
    [July 12, 2017 at 6:42 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1478853)
    
    how i find x and y value in the following equation by use of excel
    
    x+y =136.96  
    28x/100+18y/100 =16  
    then what is the value of x and y  
    how it find
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1478853)
    
14.  ![](https://secure.gravatar.com/avatar/bd45763c1b9e337766d093af39506d707e098cc9aca67561e7efd2655e0cf265?s=64&d=mm&r=g) jithin says:
    
    [July 12, 2017 at 7:06 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1478860)
    
    how i find x and y value in the following equation by use of excel
    
    x+y =120.56  
    28x/100+18y/100 =32.4  
    then what is the value of x and y  
    how it find
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1478860)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 12, 2017 at 8:09 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1478882)
        
        @Jithin
        
        This is a simultaneous equation
        
        I would solve this manually like:
        
        (1) x+y =120.56  
        (2) 28x/100+18y/100 =32.4
        
        (3) = (1) x 18/100  
        \= 18x/100 +18y/100 = 18\*120.56/100  
        \= 18x/100 +18y/100 = 21.7008
        
        (4) = (2) - (3)  
        28x/100+18y/100 =32.4  
        \- 18x/100 +18y/100 = 21.7008  
        \= 10x/100 + 0 = 32.4 - 21.7008  
        \= x/10 = 10.6992
        
        (5) Multiply both sides by 10  
        x = 106.992
        
        (6) Substitute x into (1)  
        x+y =120.56  
        106.992 + y = 120.56  
        y = 120.56 - 106.992  
        y = 13.568
        
        Enjoy
        
        [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1478882)
        
15.  ![](https://secure.gravatar.com/avatar/23e0b47b251c9af3b654aef8860fbe24cab309ed746c2212fb141fd448640b40?s=64&d=mm&r=g) g\*G-Anfy Jensen says:
    
    [July 13, 2017 at 10:40 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1479755)
    
    Thanks so much for your response to my inquiry, but I will appreciate a further detailed information in a vivid description.
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1479755)
    
16.  ![](https://secure.gravatar.com/avatar/983bef718d25ef115a1644e13c0bff9c27d4d727f7854bca4b4dde6061a9fffe?s=64&d=mm&r=g) San says:
    
    [June 26, 2018 at 4:33 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1555177)
    
    i just want to put a formula like below:
    
    Ex. 1  
    time- 2:30  
    formula want to make : =2+30/60
    
    Ex 2  
    Time - 0.30  
    formula : =0+30/60
    
    Help me if possible
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1555177)
    
17.  ![](https://secure.gravatar.com/avatar/90d1f2db464918505d1c245fcbe2be93abd2b0612290ca7e78278077bd6a9515?s=64&d=mm&r=g) Chirayu Shakya says:
    
    [November 27, 2019 at 1:31 pm](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1716991)
    
    I need to solve 2a+7a=9a in excel. So, How can I do it??
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1716991)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 28, 2019 at 8:41 pm](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1717353)
        
        hmm, I am confused. What is there is to solve. 2a+7a **is** 9a
        
        [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-1717353)
        
18.  ![](https://secure.gravatar.com/avatar/f51e33cea9b0cd2696f8d3ca85a207b80f317a62151c43efeaecca3a39a238bf?s=64&d=mm&r=g) radhika says:
    
    [December 27, 2022 at 6:25 am](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-2112925)
    
    Emp. MONTH Date BEAT NAME DISTR-NAME  
    xyz jan 1-1-2022 LEAVE LEAVE
    
    entire year record is here in excel .  
    suggest formula for each Employee every month how many leaves are there???
    
    [Reply](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#comment-2112925)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/how-to-solve-an-equation-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [7 reasons why you should use INDEX() formula in Excel](https://chandoo.org/wp/index-formula-usage-and-tips/) | [What are best Excel interview questions? \[survey\]](https://chandoo.org/wp/best-excel-interview-questions/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)