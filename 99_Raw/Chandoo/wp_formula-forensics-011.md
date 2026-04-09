# Count how many times a list of letters is in a text string

**Source:** https://chandoo.org/wp/formula-forensics-011

---

Formula Forensics 011. Lykes Formula
====================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 14 comments

  

Lykes, a Chandoo.org follower, submitted this problem for analysis by Formula Forensics.

“I have a list of words and I want to find out how many times each record in the list contains an entry from another list of single characters. I use the following equation, but how does it work? ”

\=SUMPRODUCT(COUNTIF(B3,”\*”&$E$3:$E$6&”\*”))

So today we will pull this apart to see what’s inside.

**Lyke’s Formula**
------------------

As usual we will work through this formula using a sample file for you to follow along. You can download it here. [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/01/Lykes-Sample-File.xls "Sample File - Excel 97-2010")
.

Lykes has a Sumproduct based formula

\=SUMPRODUCT(COUNTIF(B3,”\*”&$E$3:$E$6&”\*”))

Lets look at cell **C3** as our example.

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/Lyke01.png "Lyke01")](https://chandoo.org/wp/wp-content/uploads/2012/01/Lyke01.png)

In **C3** we see the formula: \=SUMPRODUCT(COUNTIF(B3,”\*”&$E$3:$E$6&”\*”))

Which consists of a Sumproduct and a Countif.

We know from [Formula Forensics 007](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/ "FF07")
 that Sumproduct, Sums the Product of the Arrays, and that when there is only 1 array it simply sums the array elements.

In this case Sumproduct only has a single array as an element

\=SUMPRODUCT(COUNTIF(B3,”\*”&$E$3:$E$6&”\*”))

and so the COUNTIF(B3,”\*”&$E$3:$E$6&”\*”) component must return an Array of elements for the Sumproduct to sum.

If we now look at the COUNTIF(B3,”\*”&$E$3:$E$6&”\*”) component.

The Excel Countif() function has the format COUNTIF(Range, Criteria).

Countif() will look through a Range and Count the occurrences of the Criteria.

In our case:

The Range is: B3, The Source Cell

The Criteria is: “\*”&$E$3:$E$6&”\*”

The Criteria is a Text Concatenation or Joining of a \* and the cells in the range $E$3:$E$6 and a Final \*. It is saying I want the value/s from E3:E6 with any value in front or after the value from E3:E6.

This is where the magic of Sumproduct kicks in.

Sumproduct forces this to be evaluated as an Array and so each cell in the Criteria has a \* added to each end and is then compared against the Range in the Countif.

So in other words, Countif is looking for any occurrence of the characters in the Criteria Range $E$3:$E$6 with any characters preceding or trailing them, in the Cell B3.

We can see this if in a blank cell say **E12**: we enter the following:

\=COUNTIF(B3,”\*”&$E$3:$E$6&”\*”) press **F9** not Enter.

Excel will respond with \={1;1;1;0}

This is showing us that the 1st, 2nd and 3rd elements in $E$3:$E$6, are found in **B3**, which we can see below:

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/Lyke02.png "Lyke02")](https://chandoo.org/wp/wp-content/uploads/2012/01/Lyke02.png)

Sumproduct now only has to add up the Array

\=Sumproduct({1;1;1;0})

Which it does returning **3**.

Examine the other cells in the Text range and see what is happening.

### Your Challenge

Try changing the values in the Text or Word List Column and see what effects it has on the answers.

**Download**
------------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/01/Lykes-Sample-File.xls "Sample File - Excel 97-2010")
.

**Formula Forensics “The Series”**
----------------------------------

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series:](https://chandoo.org/wp/tag/formula-forensics/ "Taruns problem")

**We Need Your Help**
---------------------

I have received a few more ideas since last week and these will feature in coming weeks.

I do need more ideas though and so I need your help.

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
| Written by Hui...  <br>Tags: [countif()](https://chandoo.org/wp/tag/countif/)<br>, [sumproduct](https://chandoo.org/wp/tag/sumproduct/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 14 Responses to “Formula Forensics 011. Lykes Formula”

1.  ![](https://secure.gravatar.com/avatar/01bbdf718b6885a901c037b6519967b0b4e09adbcf6d24a728b0f60cbd7ce994?s=64&d=mm&r=g) Kurt says:
    
    [February 9, 2012 at 3:58 pm](https://chandoo.org/wp/formula-forensics-011/#comment-220117)
    
    Interesting....
    
    How would you do the reverse? Count how many times the text contains the word list? So
    
    Word List Freg  
    a 12  
    b 6  
    etc
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-220117)
    
2.  ![](https://secure.gravatar.com/avatar/24bec80b5bc92a9e21369fca0db9632b7d728a0bf2832672e115c80d8715b4bd?s=64&d=mm&r=g) Sachin says:
    
    [February 9, 2012 at 4:45 pm](https://chandoo.org/wp/formula-forensics-011/#comment-220118)
    
    I couldn't downlload the sample file so I recreated it and have some questions about the formula.
    
    They way I understand it, the formula counts the number of times any of the 4 single letters in E3:E6 appear in the target cell - one of B3 through B9.
    
    But starting in B6, you get multiple instances of the same letter - mostly f. The formula counts it as one appearance. I would have guessed that the correct answer for B6 would be 2, B7 would be 2, B8 would be 4 and B9 would be 2.
    
    Perhaps I'm misreading the problem we are trying to solve.
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-220118)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [February 10, 2012 at 3:54 am](https://chandoo.org/wp/formula-forensics-011/#comment-220135)
        
        @Sachin  
        The question maybe should have been put as "How many of the small list appear in the text"
        
        [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-220135)
        
3.  ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
     says:
    
    [February 9, 2012 at 11:58 pm](https://chandoo.org/wp/formula-forensics-011/#comment-220130)
    
    @All  
    The download and other links have been fixed
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-220130)
    
4.  ![](https://secure.gravatar.com/avatar/8c7a45c1b40aba6138103d76acd3ecda6ff16bbf27e06bb9c407103327e1bf2f?s=64&d=mm&r=g) ahmed says:
    
    [February 10, 2012 at 5:08 pm](https://chandoo.org/wp/formula-forensics-011/#comment-220154)
    
    Hi  
    In the forum Hui said that the all the links have been fixed. No they have not. They are still not working, sir
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-220154)
    
5.  ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
     says:
    
    [February 11, 2012 at 12:52 am](https://chandoo.org/wp/formula-forensics-011/#comment-220159)
    
    @Ahmed  
    They are all working  
    You may have to Clear your web browsers Cache
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-220159)
    
6.  ![](https://secure.gravatar.com/avatar/250142da3b1bbbfbd631651d53ec8204ab628274d0fcaf21b5e11075f368191d?s=64&d=mm&r=g) Joe Carsto says:
    
    [February 15, 2012 at 4:19 pm](https://chandoo.org/wp/formula-forensics-011/#comment-220245)
    
    Thanks Hui for another great article. I understand (and often use) how press F9 will display the array results, but is there a way to display the F9 results in a cell?
    
    For example, when you press F9 (in the example above), you see {1;1;1;0}. Is there a formula or function that would display this whole array in a cell? Entering the formula as an array (Ctrl-Shift-Enter) only displays the first element of the array. I would like to see the whole array displayed, not just the first element.
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-220245)
    
7.  ![](https://secure.gravatar.com/avatar/40676cbf2ff9a4635eeea258740d238598b5eec37bfca9d769651bc0d844dc98?s=64&d=mm&r=g) John Hackwood says:
    
    [February 16, 2012 at 3:26 am](https://chandoo.org/wp/formula-forensics-011/#comment-220263)
    
    Thanks Hui good practical one.  
    John@ReddyBay
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-220263)
    
8.  ![](https://secure.gravatar.com/avatar/282cf11c9c3b23ed5b9cb69761581541d5f7ae29c90f86b97f788ef4a60c9f6a?s=64&d=mm&r=g) Narinder Kumar says:
    
    [May 16, 2012 at 4:42 am](https://chandoo.org/wp/formula-forensics-011/#comment-223957)
    
    want a massage then i close my excel work sheet.   anybody help me regading this ?
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-223957)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [May 16, 2012 at 4:53 am](https://chandoo.org/wp/formula-forensics-011/#comment-223958)
        
        @Nerinder
        
        You can have a message appear as you save or Close by adding some code to the workbook module in the VBA Editor  
        Copy the code below  
        Alt F11  
        Find the Workbook object for your workbook  
        Paste the code into that module  
        You will now have to save the model as a \*.xlsm or \*.xlsb file
        
        `Private Sub Workbook_BeforeClose(Cancel As Boolean)   a = MsgBox("My Message", vbOKOnly, "My Message Title")   End Sub`
        
        `   or   `
        
        `Private Sub Workbook_BeforeSave(ByVal SaveAsUI As Boolean, Cancel As Boolean)   a = MsgBox("My Message", vbOKOnly, "My Message Title")   End Sub   `
        
        [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-223958)
        
9.  ![](https://secure.gravatar.com/avatar/f10ca4627388b69f45ab7ca865fff83802bed2fdf705c1759ba8a39422a70fb3?s=64&d=mm&r=g) Robert Mika says:
    
    [May 17, 2012 at 8:05 pm](https://chandoo.org/wp/formula-forensics-011/#comment-224022)
    
    This array equivalent of SUM will give the same result:  
    {=SUM(COUNTIF(B3,"\*"&$E$3:$E$6&"\*"))}
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-224022)
    
10.  ![](https://secure.gravatar.com/avatar/8155470e0a4285712eb7439362494794e576806d984d38fa1cba090b9198cf96?s=64&d=mm&r=g) MechEngr02 says:
    
    [October 30, 2014 at 5:59 pm](https://chandoo.org/wp/formula-forensics-011/#comment-832470)
    
    Back to what Sachin said...
    
    How can I count the # of occurrences of each character from the list appears totaled?
    
    So that:  
    B9 = 2 (2 "f"s)  
    B8 = 4 (2 "f"s + 1 "d")
    
    For instance, this formula used on this example:  
    abcde\*123\*io\*def<  
    Where the criteria is \* ( ) !  
    Results in 3. It's only counting the "\*" 2x.  
    The answer should be 4.
    
    Can we make this work?
    
    Everything I find online only works for one criterion or counts over a range.
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-832470)
    
    *   ![](https://secure.gravatar.com/avatar/8155470e0a4285712eb7439362494794e576806d984d38fa1cba090b9198cf96?s=64&d=mm&r=g) MechEngr02 says:
        
        [October 30, 2014 at 6:01 pm](https://chandoo.org/wp/formula-forensics-011/#comment-832471)
        
        The criteria should have been:
        
        \* ( ) !
        
        [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-832471)
        
11.  ![](https://secure.gravatar.com/avatar/8155470e0a4285712eb7439362494794e576806d984d38fa1cba090b9198cf96?s=64&d=mm&r=g) MechEngr02 says:
    
    [October 30, 2014 at 6:03 pm](https://chandoo.org/wp/formula-forensics-011/#comment-832473)
    
    Ok, lesson learned. I can't post less-than & greater-than symbols by their selves.
    
    The criteria should include them, in order to make sense.
    
    [Reply](https://chandoo.org/wp/formula-forensics-011/#comment-832473)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-011/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Using external software packages to manage your spreadsheet risk \[Part 4 of 4\]](https://chandoo.org/wp/spreadsheet-risk-management-software-review/) | [How would you customize Excel after installing? \[poll\]](https://chandoo.org/wp/how-would-you-customize-excel-after-installing-poll/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)