# Formula Forensics looks at Is my number a Prime Number?

**Source:** https://chandoo.org/wp/formula-forensics-024

---

Formula Forensics 024. Is this number a Prime Number ?
======================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 16 comments

  

Since Formula Forensics commenced I have received a number of requests for a formula to check if a number is a Prime Number. Although a test for Prime Numbers has been posted before at Chandoo.org, [Refer here](http://chandoo.org/wp/2009/05/29/array-formula-to-check-if-a-number-is-prime-just-for-fun/ "Prime Numbers at Chandoo.org")
, this is a good chance to build up an array formula from scratch using the Primality Test as an example.

So today in Formula Forensics we will examine Prime Numbers and a formula to determine if a given number is how this works and then how it can be extended to Sum the values in another field as well.

As always at Formula Forensics you can follow along using a Worked Example which you can download here: [Excel 97-2010 Sample File](https://chandoo.org/wp/wp-content/uploads/2012/07/Prime-Test.xls "Prime Number Test")
.

Whats a Prime Numbers
---------------------

Prime Numbers occur in nature in an amazing number of situations from Plant Growth to the occurrence of Cicadas  in a Forrest. Prime Numbers are extensively used in mathematics and form the basis of modern Cryptography.

Before we jump into the formula it is worth explaining a little bit about [Prime Numbers](http://en.wikipedia.org/wiki/Prime_number "Wikipedia")
 and there properties as this will aid us in developing a formula to check if a number is Prime, its Primality.

The definition of a Prime Number is an integer number greater than 1, which is only evenly divisible by two integers, being one and itself.

### Lets look at two numbers.

**16** – Sixteen isn’t a prime number as it is evenly divisible by the numbers 1, 2, 4, 8 and 16.

**17** – Seventeen is a prime number as it is only evenly divisible by the numbers 1 and 17.

We can see that we need to check all the integers from 1 through to the square root of the number.

Integers greater than the square root cannot divide into the original number evenly by default.

We can now also now see that if a number is a prime number then only one Integer between 1 and the square root of the number will divide into the number, that number is one.

Lets look at our two numbers again.

**16** (non Prime) – Square Root is 4, But integers 1, 2, & 4 can divide into 16 evenly

**17** (Prime) – Square Root is 4, But only the integer 1 can divide into 17 evenly

So we can use that property to check if a number is a prime.

That is the count of the integers which can be evenly divided into the number between 1 and the Integer of the Square Root of the number will be 1 if the number is a prime.

So we will test each Integer between 1 and the Square root of the number.

If any of those integers (except for the number 1) divide into the test number evenly with no remainder, then we know the test number is not a prime number.

If the count of numbers that divide into the number is 1 then the number is a prime.

How to Develop a Prime Number Test Formula
------------------------------------------

We have used a method in Formula Forensics several times for setting up an array of integers and that is Row(Offset($A$1,,,n,1))

This establishes an array of the numbers 1 .. n

We established above that n is the square root of the Prime Candidate. In fact it is the integer of the square root of the Prime Candidate.

That is the largest Integer which is less than the Square Root of the Prime Candidate.

If our prime candidate is 16, n = Square root (16) = 4

If our prime candidate is 17, n = Integer(Square root (17)) = 4

If cell B2 contains our Prime Candidate, lets use 100

In a Blank cell **E2**, enter \=Row(Offset($A$1,,,Int(Sqrt(B2)),1)) where n = int(Sqrt(B2)); **Don’t** press Enter press **F9**

Excel will display: \={1;2;3;4;5;6;7;8;9;10}

We next need to check if each of these numbers is evenly divisible into our Prime Candidate.

Excel has a function Mod() that will assist us.

Mod() has the syntax:

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Prime01.png "Prime01")](https://chandoo.org/wp/wp-content/uploads/2012/07/Prime01.png)

Mod returns 0 when a number can divide into another number evenly

So we can use the formula:

\=MOD(B2, ROW(OFFSET($A$1,,, Int(Sqrt(B2)),1)) )

Where B2 is the number we are checking for Primality

If We make **B2 =100** and in a Blank cell **F4** enter:

\=MOD(B2, ROW(OFFSET($A$1,,, Int(Sqrt(B2)),1)) ) **Don’t** press Enter press **F9**

Excel responds with \={0;0;1;0;0;4;2;4;1;0}

We can see that Mod(100, 1) = 0, Mod(100, 2) = 0, Mod(100, 3) = 1 etc

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Prime02.png "Prime02")](https://chandoo.org/wp/wp-content/uploads/2012/07/Prime02.png)

If the value is 0 in the above Table or Array it is evenly divisible into the Prime Candidate

We can convert these into a True/False using a quick = 0 addition to the formula

If we make **B2 =100** and in a Blank cell **F6** enter:

\=MOD(B2, ROW(OFFSET($A$1,,, Int(Sqrt(B2)),1)) )=0 **Don’t** press Enter press **F9**

Excel responds with \={TRUE;TRUE;FALSE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE}

We will use Sumproduct to count the number of True values by converting them to 1 using:

1\*MOD(B2, ROW(OFFSET($A$1,,, Int(Sqrt(B2)),1)) )=0

and we will use Sumproduct to add up the individual array elements  

\=SUMPRODUCT(1\*MOD(B2, ROW(OFFSET($A$1,,, Int(Sqrt(B2)),1)) )=0)

The 1\* forces each element of the Array to be evaluated as 1 \* True/False resulting in an array of 1/0’s.

In a blank cell **F8,** enter \=SUMPRODUCT(1\*MOD(B2, ROW(OFFSET($A$1,,, Int(Sqrt(B2)),1)) )=0)

Excel will respond with 5

This tells us there are 5 numbers between 1 and 10, the Sqrt(100), which are even divisible into 100

We saw this above with

“Excel responds with \={0;0;1;0;0;4;2;4;1;0}”

These 5 integers are 1, 2, 4, 5, 10

[![](https://chandoo.org/wp/wp-content/uploads/2012/07/Prime03.png "Prime03")](https://chandoo.org/wp/wp-content/uploads/2012/07/Prime03.png)

Finally to check if the number is a Prime this answer should be 1

This gives us our final formula of:

\=SUMPRODUCT(1\*(MOD(B2,ROW(OFFSET(A1,,,INT(SQRT(B2)),1)))=0))=1

Refer to cell **F10** or **C2**

You can try out any number in cell b2 and see if it evaluates as a Prime Number

More Prime Number Formulas
--------------------------

You can look at other Prime Number solutions using Formulas and VBA at the following links:

[Chandoo.org](http://chandoo.org/wp/2009/05/29/array-formula-to-check-if-a-number-is-prime-just-for-fun/ "Prime Numbers at Chandoo.org")

[Daily Dose of Excel](http://www.dailydoseofexcel.com/archives/2005/06/30/is-this-number-prime/ "DDOE")

[Newton Excel Bach](http://newtonexcelbach.wordpress.com/2008/11/18/finding-prime-numbers-with-excel-and-using-array-formulas/ "Newton Excel Bach")

[Microsoft](http://support.microsoft.com/kb/202782 "Microsoft")

Download
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/07/Prime-Test.xls "Prime Number Test")
.

Formula Forensics “The Series”
------------------------------

This is the 24th post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following catalog [Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
 or [Chandoo](http://chandoo.org/wp/contact/ "Contact Chandoo")
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
| Written by Hui...  <br>Tags: [INT()](https://chandoo.org/wp/tag/int/)<br>, [MOD()](https://chandoo.org/wp/tag/mod/)<br>, [OFFSET()](https://chandoo.org/wp/tag/offset/)<br>, [Prime number](https://chandoo.org/wp/tag/prime-number/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>, [SQRT()](https://chandoo.org/wp/tag/sqrt/)<br>, [sumproduct](https://chandoo.org/wp/tag/sumproduct/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 16 Responses to “Formula Forensics 024. Is this number a Prime Number ?”

1.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
    
    [July 12, 2012 at 1:25 pm](https://chandoo.org/wp/formula-forensics-024/#comment-226872)
    
    Hui - great post. Couple of thoughts
    
    Your download spreadsheet is an .xls file, so is limited to 65k rows. THis means the largest number it can check is this:  
    4,295,098,368  
    ...which is the square of the number of rows in 'old' excel.   
    IF the file is resaved as an .xlsx then the largest NUMBER it can check is this:  
    1,099,511,627,776  
    ...and the largest PRIME it will find is this:  
    1,099,513,724,917  
    It fails on the next largest prime, which is this:  
    1,099,513,724,941  
    I've got a formula up my sleeve that I thought in theory would  check numbers up to this:  
    72,057,594,037,927,900  
    ...although Excel gives up if I exceed this:  
    44,929,149,915,683  
    ...and I've actually managed to successfully check this prime:  
    44,929,149,915,581  
    ...which I'm pretty happy with. Expecting the FBI to knock on my door pretty soon 🙂  
    There's a handly prime number checker and generator at [http://www.numberempire.com/primenumbers.php](http://www.numberempire.com/primenumbers.php)
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226872)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
        
        [July 13, 2012 at 2:40 am](https://chandoo.org/wp/formula-forensics-024/#comment-226908)
        
        Interesting: I can get my formula to correctly return primes up to 199,999,999,999,903. But past 200,000,000,000,000 it fails. I wonder if 200,000,000,000,000 is significant somehow in regards to Excel's calculation engine?
        
        [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226908)
        
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
            
            [July 13, 2012 at 2:51 am](https://chandoo.org/wp/formula-forensics-024/#comment-226909)
            
            Whoops, I meant the largest prime I've been able to find is 199,999,999,999,**997** but it fails past 200,000,000,000,000
            
            [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226909)
            
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 13, 2012 at 5:12 am](https://chandoo.org/wp/formula-forensics-024/#comment-226911)
        
        @Geoff  
        Thanx for the comments   
        I wrote this last week and saved the sample file as an \*.xls file to be compatible with all readers and then forgot to make the qualification about the Row limit in Excel 97/03 and impact on the Primality Test in previous versions of Excel.  
        There are several techniques for testing primality of which this method (the Brute Force approach) is easiest to implement and explain.  
         
        
        [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226911)
        
2.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
    
    [July 12, 2012 at 1:32 pm](https://chandoo.org/wp/formula-forensics-024/#comment-226873)
    
    Good discussion of whether 1 is a prime at [http://en.wikipedia.org/wiki/Prime\_number](http://en.wikipedia.org/wiki/Prime_number)
      
    You might need to amend your formula to discount 1 in order to please the purists!  
       
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226873)
    
3.  ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) David Hager says:
    
    [July 12, 2012 at 4:00 pm](https://chandoo.org/wp/formula-forensics-024/#comment-226880)
    
    This array formula returns TRUE if the number in cell A1 is a prime number.
    
    \=OR(A1=2,A1=3,ISNA(MATCH(TRUE,A1/ROW(INDIRECT("2:"&INT(SQRT(A1))))=  
    INT(A1/ROW(INDIRECT("2:"&INT(SQRT(A1))))),0)))
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226880)
    
4.  ![](https://secure.gravatar.com/avatar/36c7cfd20dcf1a5c2b642c6b3b8d921070b3ebd488feddc80ba697dcd4a36483?s=64&d=mm&r=g) [daffy333](http://www.gregjury.ca/)
     says:
    
    [July 12, 2012 at 4:29 pm](https://chandoo.org/wp/formula-forensics-024/#comment-226881)
    
    {=SUM(--(MOD(A1,ROW($A$1:INDEX($A:$A,A1)))=0))<3}  
    This formula includes 1 as a prime number.  
    Cheers!
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226881)
    
5.  ![](https://secure.gravatar.com/avatar/8ceae07ad389f92037be72df1988137e1d17a29339ab2d5c34385d27a027ad2f?s=64&d=mm&r=g) Ola says:
    
    [July 12, 2012 at 11:07 pm](https://chandoo.org/wp/formula-forensics-024/#comment-226902)
    
    Good to see.  
    I was just asking at 'Daily Dose of Excel' if this formula was valid:  
    \=SUMPRODUCT(--(MOD(A2;ROW(INDIRECT("2:"&A2)))=0))=1  
    And now I found the above formula which seams to confirm it is.  
    Also interesting that virtually the same formula pops up just 1 day apart.  
    //Ola
    
    ...the formula works for all numbers from 1 to infinity...in princip, since Excel can't address rows below 1.048.576.  
    As a speed test; to calculate one number of 1.000.000 is no problem but to check all 1.000 numbers between 100.000 -101.000 is a bit slow.
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226902)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
        
        [July 13, 2012 at 5:35 am](https://chandoo.org/wp/formula-forensics-024/#comment-226913)
        
        @Ola: it's worth noting that - paraphrasing Hui's post above - a number can't be a prime number if any integers between 2 and the square root of the number will divide into it.  
        This means that you don't have to test every number up to the number itself, as you do with ROW(INDIRECT(“2:”&A2))  
        Instead, you can use ROW(INDIRECT(“2:”&SQRT(A2)))  
        Which also means that you are no longer limited to checking numbers up to Excel's row limit of 1,048,576 but instead can now check them up to the **square** of excel's row limit: 1,099,513,724,917  
        And if you're really crafty,  you can check numbers well beyond this too (although not with any of the formulas posted above). As per my comment above, I've got a formula that correctly returns primes up to 199,999,999,999,903. But past 200,000,000,000,000 it fails. I'm in the process of writing up a blog post on this, and will share it when I'm done.  
         
        
        [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226913)
        
6.  ![](https://secure.gravatar.com/avatar/aade450ee4034589d08bca25fdb38fd1dd7b95910f1d52b395c912226f4fe2ca?s=64&d=mm&r=g) jomili says:
    
    [July 13, 2012 at 12:43 pm](https://chandoo.org/wp/formula-forensics-024/#comment-226937)
    
    Hui,
    
    I think you have an error in your instructions.  The instructions say to put this formula in F8:  
    \=SUMPRODUCT(1\*MOD(B2, ROW(OFFSET($A$1,,, Int(Sqrt(B2)),1)) )=0)  
    The formula in your example file in F8 is this:  
    \=SUMPRODUCT(1\*(MOD(B2,ROW(OFFSET(A1,,,INT(SQRT(B2)),1)))=0))
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226937)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 13, 2012 at 1:43 pm](https://chandoo.org/wp/formula-forensics-024/#comment-226940)
        
        @Jomili
        
        I think I may fire my proof reader!
        
        The $ signs aren't important in this instance, provided the formula isn't dragged somewhere else. The Formula must refer to a cell in Row 1 instead of A1 wherever it is located.
        
        The spacing is added so that that I have some control over the word wrapping that wordpress uses, where if i remove the spacing in the formula i get word wrapping that isn't in good locations.
        
        [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-226940)
        
7.  ![](https://secure.gravatar.com/avatar/3a11f8067f286e6e10fdd46eb8791523ca3ac9028262757cf5e60aabbc043d51?s=64&d=mm&r=g) JIALIN says:
    
    [July 13, 2012 at 8:32 pm](https://chandoo.org/wp/formula-forensics-024/#comment-227000)
    
    \=AND(MOD(L19,ROW(INDIRECT("2:"&INT(SQRT(L19))))))
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-227000)
    
8.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
    
    [July 13, 2012 at 10:09 pm](https://chandoo.org/wp/formula-forensics-024/#comment-227011)
    
    @Jialin: that use of AND is sheer genius. It completely does away with the need to use SUM or SUMPRODUCT. Just awesome!
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-227011)
    
9.  ![](https://secure.gravatar.com/avatar/61f2ab768ae2a6381c5c5e7fc0c819cfb5be2c4520a27a6aa505cf431c3ef58d?s=64&d=mm&r=g) Michael says:
    
    [July 18, 2012 at 11:22 pm](https://chandoo.org/wp/formula-forensics-024/#comment-227257)
    
    Hi Hui - A bit off-topic, but you may be interested in this entry for the global TED Conference by Adam Spencer about his passion for prime numbers. He's a mathematician, and also a broadcaster on ABC Radio.  
    [http://talentsearch.ted.com/video/Adam-Spencer-A-lifelong-passion;TEDSydney](http://talentsearch.ted.com/video/Adam-Spencer-A-lifelong-passion;TEDSydney)
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-227257)
    
10.  ![](https://secure.gravatar.com/avatar/5d7cdba3b4b16115b6093f02d780868ddd048ddf27ddac08974ddae4af6851bb?s=64&d=mm&r=g) [Peter Mown](http://numberworld.info/)
     says:
    
    [August 21, 2012 at 1:09 pm](https://chandoo.org/wp/formula-forensics-024/#comment-229092)
    
    Here is a great online prime number checker which can check numbers up to 5000 digits [http://numberworld.info/primeCheck](http://numberworld.info/primeCheck)
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-229092)
    
11.  [Anonymous](http://www.ayudaexcel.com/foro/cafeteria-ayuda-excel-72/retos-programacion-26580/index2.html#post129759)
     says:
    
    [December 7, 2012 at 8:53 am](https://chandoo.org/wp/formula-forensics-024/#comment-335697)
    
    \[...\] \[...\]
    
    [Reply](https://chandoo.org/wp/formula-forensics-024/#comment-335697)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-024/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Highlight Row & Column of Selected Cell using VBA](https://chandoo.org/wp/highlight-row-column-of-selected-cell-using-vba/) | [How do you explain Excel to a small kid? \[poll\]](https://chandoo.org/wp/how-do-you-explain-excel-to-a-small-kid-poll/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)