# Cummulative Price increases using an Array Formula

**Source:** https://chandoo.org/wp/formula-forensic-no-015

---

Formula Forensic No. 015 – Cornelia’s Price Rises
=================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 17 comments

  

In March Cornelia asked a question at [Chandoo.org](http://chandoo.org/wp/2010/09/16/excel-circular-references/#comment-220977 "Cornelias Question")
:

“_I Want to create a formula for my price list, every time the prices goes up a certain %, I just want to edit the % sell, then my entire spread sheet needs to change accordingly._”

I responded with a simple array formula

\=A2\*PRODUCT(1+PriceRises/100)

[![](https://chandoo.org/wp/wp-content/uploads/2012/03/CO1.png "CO1")](https://chandoo.org/wp/wp-content/uploads/2012/03/CO1.png)

So today we will pull Hui’s Solution apart to see what’s inside.

**Hui’s Solution**
------------------

As usual we will work through this formula using a sample file for you to follow along. [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/03/Cornelia-Example.xls "Example File")
.

Hui’s formula is an array formula

{\=A2\*PRODUCT(1+PriceRises/100)}

This formula is a simple Original Price \* Factor style formula

Where the Factor is PRODUCT(1+PriceRises/100)

Which is calculating the cumulative price rise based on a list of individual price rises in a Named Formula called “PriceRises”

Going into the Name Manager we can see that the Named Formula “Price Rises” is made up of the formula

\=OFFSET(Sheet1!$E$2,,,COUNTA(Sheet1!$E:$E)-1,1)

This is a simple offset formula which will return the list of Price Rises from Column E

Offset uses the Reference **E2** and the counts the number of entries in Column **E** and subtracts **1** (for the header row)

In a Blank cell say **L8** enter \=OFFSET(Sheet1!$E$2,,,COUNTA(Sheet1!$E:$E)-1,1) Then press **F9**

Excel will return \={4,5,6}

Which is a list of the 3 Price Rises in the Price Rise column.

So back to the equation PRODUCT(1+PriceRises/100)

We can see that it consists of a Product() function which will multiply the values of the constituent numbers together.

PRODUCT(1+PriceRises/100)

But the constituent numbers consists of a Formula 1+PriceRises/100

In a spare cell say **L10** enter the formula \=1+PriceRises/100  Then press **F9**

Excel will return \={1.04, 1.05, 1.06}

We can see here that Excel has taken each entry from the Price Rises Named Formula and divided it by 100 and then added 1 to it

Product then multiplies the numbers together to return the Price Rise factor of **1.15752 = (1.04 \* 1.05 \* 1.06)**

This is finally used to multiply the Original price to arrive at the new sale price

The benefit of using a Named Formula here is that if you add an entry to Column E ie: another price rise, that the PriceRises named formula expands to include that entry and a new Price Rise factor is hence applied to all the entries

**Download**
------------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/03/Cornelia-Example.xls "Example File")
.

**Formula Forensics “The Series”**
----------------------------------

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics Series")

**We Need Your Help**
---------------------

Formula Forensics is running out of ideas for future Formula Forensics Posts and so I need your help.

If there is an Excel Function that you want explained as in FF07 – Sumproduct let me know

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained but don’t want to write a post also send it to [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
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
| Written by Hui...  <br>Tags: [OFFSET()](https://chandoo.org/wp/tag/offset/)<br>, [product](https://chandoo.org/wp/tag/product/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 17 Responses to “Formula Forensic No. 015 – Cornelia’s Price Rises”

1.  ![](https://secure.gravatar.com/avatar/278ed91a3a617c2c6bf856541e1e874df8469ee8784cdb350c4d8eeaa461cbdb?s=64&d=mm&r=g) Fred says:
    
    [March 8, 2012 at 5:59 pm](https://chandoo.org/wp/formula-forensic-no-015/#comment-221043)
    
    I like the neat trick and I think I can apply it at work somewhere. but I have a question for this particular situation.
    
    Why not just Product a range of cells suh as H2:H100 and H1 being =product(H2:H100)? this way cornelia have 99 slots to enter the future changes in %.
    
    Then have all the numbers in column A multiply H1 in column B. Wouldn't it be simple?
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221043)
    
2.  ![](https://secure.gravatar.com/avatar/58bf5cd3bbd589957d7732e65913b2a9ed3b9f09b259c43777d82f0b765cadea?s=64&d=mm&r=g) Anita says:
    
    [March 8, 2012 at 6:12 pm](https://chandoo.org/wp/formula-forensic-no-015/#comment-221044)
    
    Fred,
    
    It may be simpler, but this solution is very elegant and you don't have floating numbers anywhere (meaning the number in H1). It also lets you enter even 100 price rises, and you still don't have to worry about it. If you created the sheet with your solution and someone takes it over, after entering the 100th increase, there could be problems if the person is not paying attention. We always try to create a solution that includes the least hard-coding to guarantee future perfection.
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221044)
    
    *   ![](https://secure.gravatar.com/avatar/278ed91a3a617c2c6bf856541e1e874df8469ee8784cdb350c4d8eeaa461cbdb?s=64&d=mm&r=g) Fred says:
        
        [March 8, 2012 at 11:06 pm](https://chandoo.org/wp/formula-forensic-no-015/#comment-221056)
        
        Hi Anita,
        
        I agree that it is a very elegant solution. What I want to say is that this solution still require a column, in this case column E, as the input column for the % increase. So it doesn't seem to me that it would hurt the integrity of the calculation by adding a helper column in a hidden worksheet, that's all. Plus if you hand this to another person it is much easier to understand what is going on.
        
        Frankly, I didn't know what Cornelia was asking and what Hui was fixing until I read "Product then multiplies the numbers together to return the Price Rise factor of 1.15752 = (1.04 \* 1.05 \* 1.06)".
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221056)
        
        *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
             says:
            
            [March 9, 2012 at 3:32 am](https://chandoo.org/wp/formula-forensic-no-015/#comment-221065)
            
            @Fred, Anita
            
            You could store the Individual Price Rises in a Named Formula like  
            PriceRises ={4,5,6}  
            But this hides the numbers out of site.
            
            Generally in any reasonable spreadsheet you will have a input/assumptions worksheet where this would be stored and then it is very transparent.
            
            [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221065)
            
3.  ![](https://secure.gravatar.com/avatar/58bf5cd3bbd589957d7732e65913b2a9ed3b9f09b259c43777d82f0b765cadea?s=64&d=mm&r=g) Anita says:
    
    [March 8, 2012 at 6:21 pm](https://chandoo.org/wp/formula-forensic-no-015/#comment-221045)
    
    In some of our analyses we have to calculate the average factor increases for a set of groups. I have the original premium PMPMs in one column, and the factor increases by premium PMPM in another column (like 4.3%). Today I create a third column where I add 1 to the factor increase and then calculate the average by taking the SUMPRODUCT of the premium PMPMs and the third column, divide it by the total premium PMPMs and substract 1 from the result.
    
    After looking at this solution, I thought I could use this in my analyses, but it is not working for me. Does anyone know how I can skip the third column and calculate the average straight from the first two columns?
    
    Thank you for your help.
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221045)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [March 9, 2012 at 12:54 am](https://chandoo.org/wp/formula-forensic-no-015/#comment-221063)
        
        Hi Anita
        
        I'll assume you have data in Columns A:B at present and have a Third Column C where you add 1  
        and a Formula similar to: =Sumproduct(A2:A10,C2:C10)/Counta(B2:B10)-1
        
        This can be replaced by  
        \=Sumproduct(A2:A10,1+B2:B10)/Counta(B2:B10)-1  
        and remove the Third Column
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221063)
        
        *   ![](https://secure.gravatar.com/avatar/58bf5cd3bbd589957d7732e65913b2a9ed3b9f09b259c43777d82f0b765cadea?s=64&d=mm&r=g) Anita says:
            
            [March 9, 2012 at 3:49 pm](https://chandoo.org/wp/formula-forensic-no-015/#comment-221086)
            
            Hi Hui,
            
            I tried this, but the result is not the same than if I did it with the third column. I will keep trying and let you know if I found a nice solution.
            
            Thanks for your reply.
            
            [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221086)
            
4.  ![](https://secure.gravatar.com/avatar/d75b2dded123620d1ff6dfa9b7a458edb6eaa3f87950e3daa6570cc253e0163b?s=64&d=mm&r=g) John Hackwood says:
    
    [March 8, 2012 at 9:08 pm](https://chandoo.org/wp/formula-forensic-no-015/#comment-221054)
    
    Hi, Hui first time I have ever seen Product used and it's perfect for this situation. Appreciate being made aware of it. Thank you and thanks Chandoo for these kinds of posts.
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221054)
    
5.  ![](https://secure.gravatar.com/avatar/2db9620a90e89c987a67bcd9240c5d0cec04030c7f24718b49e157a62e6c450d?s=64&d=mm&r=g) Jay Hunnemeyer says:
    
    [March 9, 2012 at 12:12 am](https://chandoo.org/wp/formula-forensic-no-015/#comment-221059)
    
    Great use of the Product function in an array formula, Hui! I was curious as to how you were using this when I saw the example, I was quite impressed when I opened the file and ran it through my formula evaluation. Thanks for your great examples, and thanks Chandoo for your series.
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221059)
    
6.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [March 9, 2012 at 4:19 am](https://chandoo.org/wp/formula-forensic-no-015/#comment-221067)
    
    Excellent use of PRODUCT(). Thank you so much for sharing this with all of us Hui...
    
    Just another tip - you can move the A2 inside PRODUCT as we are multiplying like this: PRODUCT(A2,1+PriceRises/100) and it works too (of course, you need to array enter).
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221067)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [March 9, 2012 at 9:33 am](https://chandoo.org/wp/formula-forensic-no-015/#comment-221075)
        
        Thanx Chandoo
        
        I realise that you can put A2 inside the product, I just think it reads better when it's outside
        
        Similarly If you store the formulas as actual percentages you can remove the /100 to get:  
        \=A2\*PRODUCT(1+PriceRises)
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221075)
        
7.  ![](https://secure.gravatar.com/avatar/7e2302981d3ab84e1e159b3d207aa03504b45e0b3328f1678b5722688dd9c3de?s=64&d=mm&r=g) Benito Merino says:
    
    [March 9, 2012 at 7:52 am](https://chandoo.org/wp/formula-forensic-no-015/#comment-221070)
    
    Excellent.
    
    It will be interesting to use this formula with some temporal restrictions. It means that changes in prices are usually limited between a beginning period and an ending period.
    
    Thank you everybody!
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221070)
    
8.  ![](https://secure.gravatar.com/avatar/adf684a131f430f8b4b8f57d80283cfcab9c8dd16a1899b738abdbded43aa1ad?s=64&d=mm&r=g) Marninei says:
    
    [March 9, 2012 at 10:11 am](https://chandoo.org/wp/formula-forensic-no-015/#comment-221077)
    
    Hi all,
    
    Although the solution is elegant and creative, I'm not sure it was necessary to begin with. Not for the calculation part anyway.
    
    Excel has a function called FVSCHEDULE that does the exact same thing, i.e. multiplying a series of percentages.
    
    The only thing I see relevant here is the OFFSET for the data range.
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221077)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [March 9, 2012 at 2:29 pm](https://chandoo.org/wp/formula-forensic-no-015/#comment-221082)
        
        @Marninei  
        Many thanx for pointing out FVSchedule, yes it does exactly what this post is about in one succinct function.  
        I tend to derive all the Financial Functions I use myself natively and really should bother learning a few more of the built in ones.
        
        Thanx Again
        
        Hui...
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221082)
        
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [March 12, 2012 at 4:00 am](https://chandoo.org/wp/formula-forensic-no-015/#comment-221164)
        
        Good find on FVSCHEDULE... thanks for sharing Marninei...
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221164)
        
9.  ![](https://secure.gravatar.com/avatar/adf684a131f430f8b4b8f57d80283cfcab9c8dd16a1899b738abdbded43aa1ad?s=64&d=mm&r=g) Marninei says:
    
    [March 9, 2012 at 8:33 pm](https://chandoo.org/wp/formula-forensic-no-015/#comment-221105)
    
    I know exactly what you mean.  
    Every once in a while I find myself going over the different functions, realizing yet again that I didn't use a built in function when I had the chance.  
    Especially financial ones.
    
    Old habits die hard...
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-221105)
    
10.  ![](https://secure.gravatar.com/avatar/f08c33d1d73fa954d9c520cb983a06afde390bc5124875aa6606c7ea46909b19?s=64&d=mm&r=g) Mitch says:
    
    [August 7, 2012 at 3:07 pm](https://chandoo.org/wp/formula-forensic-no-015/#comment-228482)
    
    As was said above, I also would have done this with the FVSchedule function.  
    If you want, you can array enter this and it will do the trick:
    
    \=FVSCHEDULE(A2,INDIRECT("E2:E"&COUNTA(E:E))/100)
    
    The indirect will make an array out of everything that has a value in the E column so you don't need the named range.  
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-015/#comment-228482)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensic-no-015/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [In Cell Text Formats – 2 Quick Tips](https://chandoo.org/wp/in-cell-text-formats-2-quick-tips/) | [What is so special about Go To Special? \[15 tips\]](https://chandoo.org/wp/go-to-special/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)