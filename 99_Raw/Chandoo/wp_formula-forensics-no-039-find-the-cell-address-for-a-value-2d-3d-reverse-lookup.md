# Formula Forensics 039- 2D & 3D Reverse Lookup

**Source:** https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup

---

Formula Forensics No. 039 – Find the Cell Address for a value (2D & 3D Reverse Lookup)
======================================================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 7 comments

  

Yesterday in [Formula Forensics 038](http://chandoo.org/wp/2015/10/14/formula-forensics-no-038-find-which-worksheet-a-max-or-min-value-is-on/)
 we looked at an example of how to find a value or the Max/Min across a number of worksheets.  
Then we looked at how to find out which worksheet the value was on.

At the end I posed the question – _How do you find out which cell has the Maximum or Minimum value once we know which worksheet it is on?_

Today we will answer that question:

As always at Formula Forensics we will use a sample file which you can use to follow along: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2015/10/2D-3D-Reverse-Lookup.xlsx)

The sample file contains 3 worksheets of data Sheet1, Sheet2 and Sheet3 and a 2D Results and 3D Result worksheets.

2D Reverse Lookup
-----------------

### (How to find the cell which contains a value in a 2D Range)

Before we answer the above question, we will first look at a simpler example of finding a values address in a 2D range on the existing worksheet before expanding that logic into the third dimension.

Open the sample file and goto the **2D Result** worksheet.

[![FF39b](https://chandoo.org/wp/wp-content/uploads/2015/10/FF39b2.png)](https://chandoo.org/wp/wp-content/uploads/2015/10/FF39b2.png)

You will see a simple range of values **A1:D4** where all cells contain the value **5**  
The Minimum value of **3** is in **B2**  
The Maximum value of **10** is in **C3**

To find the Address of the cells containing the minimum and maximum values we will use the Excel Address() function

[![FF39a](https://chandoo.org/wp/wp-content/uploads/2015/10/FF39a.png)](https://chandoo.org/wp/wp-content/uploads/2015/10/FF39a.png)

If we look at the formula in cell **G9** we will see:  
\=ADDRESS(INDEX(ROW(A1:A4),SUMPRODUCT((A1:D4=G6)\*(ROW(A1:D4)))), INDEX(COLUMN(A1:D1),SUMPRODUCT((A1:D4=G6)\*(COLUMN(A1:D4)))),1,1)

Referring to the Address() syntax above:  
**Row\_Number**: INDEX(ROW(A1:A4),SUMPRODUCT((A1:D4=G6)\*(ROW(A1:D4))))

**Column\_Number**:  INDEX(COLUMN(A1:D1),SUMPRODUCT((A1:D4=G6)\*(COLUMN(A1:D4))))

**ABS\_Number**: 1

**A1**: 1

First thing to note is that the two formulas for the Row and Column Numbers are very similar  
The Row\_Number formula looks at the Row of the range **A1:D4**  
The Column\_Number formula looks at the Column of the range **A1:D4**  
and so the logic of each is the same we will only examine the Row derivation.

You can check the logic of the column to ensure you understand what is going on there.

The second thing to note is that the Value for the Row is determined using an Index function.

The Excel Index() function has the syntax:

[![FF39b](https://chandoo.org/wp/wp-content/uploads/2015/10/FF39b.png)](https://chandoo.org/wp/wp-content/uploads/2015/10/FF39b.png)

In our formula above we have

INDEX(ROW(A1:A4), SUMPRODUCT((A1:D4=G6)\*(ROW(A1:D4))))  
where  
**Array**: ROW(A1:A4)  
**Row\_Number**: SUMPRODUCT((A1:D4=G6)\*(ROW(A1:D4)))  
\[**Column\_Number**\]: Is Optional and not used in the example

If we Select Cell **G9**, Edit the cell with **F2**  
Select the first **Row(A1:A4)** component and then press **F9**  
Excel will display: {1;2;3;4}  
this clearly is an array of the rows of the cells **A1:A4**

The Row\_Number component SUMPRODUCT((A1:D4=G6)\*(ROW(A1:D4)))  
This is returning the Row Number for use in the Index function and in our case will return the value 2 for the Minimum value of 3  
But How?

Look at the formula: SUMPRODUCT((A1:D4=G6)\*(ROW(A1:D4))))  
you will see it is a Sumproduct function containing: (A1:D4=G6)\*(ROW(A1:D4)))

Select the entire internal part “(A1:D4=G6)\*(ROW(A1:D4)))” of the sumproduct() function and press **F9**  
Excel will display: {0,0,0,0;0,2,0,0;0,0,0,0;0,0,0,0}

The , in the above string denotes Columns and the ; denotes Rows  
This would be better written as:  
{0,0,0,0;  
 0,2,0,0;  
 0,0,0,0;  
 0,0,0,0}

This is derived from the multiplication of the two internal components of the sumproduct

The first part A1:D4=G6 

This is saying return an array of values where A1:D4=G6

Select **(A1:D4=G6)**, press **F9**  
{False,False,False,False;  
False,True ,False,False;  
False,False,False,False;  
False,False,False,False}

and multiply that by the Row number of each cell in A1:D4

Select **ROW(A1:D4)**, Press **F9**  
{1,1,1,1;  
2,2,2,2;  
3,3,3,3;  
4,4,4,4}

We can see that A1:D4=G6 only occurs in the minimum cell **B2** and in this case the Row number is **2**

{False\*1, False\*1, False\*1, False\*1;  
False\*2, **True\*2**, False\*2, False\*2;  
False\*3, False\*3, False\*3, False\*3;  
False\*4, False\*4, False\*4, False\*4}

Sumproduct multiplies the two arrays and adds all the values up and gets the value **2**

You can read more about using [Advanced Sumproduct](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/)
 and derivation of this type of logic at: [FF007](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/)

The same logic is now applied to the Columns, which for the Minimum also returns 2

So our original formula:  
\=ADDRESS(INDEX(ROW(A1:A4),SUMPRODUCT((A1:D4=G6)\*(ROW(A1:D4)))),INDEX(COLUMN(A1:D1),SUMPRODUCT((A1:D4=G6)\*(COLUMN(A1:D4)))),1,1)

is simplified to: \=ADDRESS(2,2,1,1)  
For which excel displays as **$B$2**  
The address of the minimum value.

3D Reverse Lookup
-----------------

Now change to the **3D Results** Worksheet

We can extend the Reverse Lookup to 3D by using a combination of multiple worksheet Ranges and the fact that we already know the Worksheet where the Minimum is located from our work in FF038

The basic formula for finding the address we saw above is:  
\=ADDRESS(INDEX(ROW(A1:A4),SUMPRODUCT((A1:D4=G6)\*(ROW(A1:D4)))), INDEX(COLUMN(A1:D1),SUMPRODUCT((A1:D4=G6)\*(COLUMN(A1:D4)))), 1, 1)

This needs to be extended to 3D by changing the references to the Ranges **A1:D4**  
Referring to E11

This is done via the use of the Excel Indirect() function:  
\=ADDRESS(INDEX(ROW(INDIRECT(D3&”!A1:A4″)), SUMPRODUCT((INDIRECT(D3&”!A1:C4″)=C3) \* (ROW(INDIRECT(D3&”!A1:C4″))))), INDEX(COLUMN(INDIRECT(D3&”!A1:C1″)), SUMPRODUCT((INDIRECT(D3&”!A1:C4″)=C3) \* (COLUMN(INDIRECT(D3&”!A1:C4″))))), 1, 1)

Excel returns **$B$2**

In the above you can see that we have replaced all the references to ranges eg: **A1:A4** etc with an Indirect() Function  
**INDIRECT(D3&”!A1:A4″)**

Indirect takes the text, in this case the Worksheets name in cell **D3** and appends the text “**!A1:A4**” to it to form the 3D range  
**Sheet2!A1:A4**

We can now add the final optional component to the Address() function

As we already know the worksheet in Cell **D3**

\=ADDRESS(INDEX(ROW(INDIRECT(D3&”!A1:A4″)), SUMPRODUCT((INDIRECT(D3&”!A1:C4″)=C3)\*(ROW(INDIRECT(D3&”!A1:C4″))))), INDEX(COLUMN(INDIRECT(D3&”!A1:C1″)), SUMPRODUCT((INDIRECT(D3&”!A1:C4″)=C3) \* (COLUMN(INDIRECT(D3&”!A1:C4″))))), 1, 1, D3)  
Excel returns: **Sheet1!$B$2**

Download
--------

You can download a copy of the above file and follow along, [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2015/10/2D-3D-Reverse-Lookup.xlsx "Download Sample File")
.

A Challenge
-----------

Can you solve the problem another way ?

Post your solutions in the comments below.

**[Other Posts in this Series](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensuics Homepage")
  
**
---------------------------------------------------------------------------------------------------------------------

The Formula Forensics Series contains a wealth of useful solutions and information specifically about how Normal Formula and specifically Array Formula work.

You can learn more about how to pull Excel Formulas apart in the following posts: [http://chandoo.org/wp/formula-forensics-homepage/](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensics Homepage")

If you have a formula and you want to understand how it works contact [Hui](http://chandoo.org/wp/about-hui/)
 and it may be featured in future posts.

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
| Written by Hui...  <br>Tags: [address](https://chandoo.org/wp/tag/address/)<br>, [column()](https://chandoo.org/wp/tag/column/)<br>, [INDEX()](https://chandoo.org/wp/tag/index/)<br>, [INDIRECT()](https://chandoo.org/wp/tag/indirect/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>, [sumproduct](https://chandoo.org/wp/tag/sumproduct/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 7 Responses to “Formula Forensics No. 039 – Find the Cell Address for a value (2D & 3D Reverse Lookup)”

1.  ![](https://secure.gravatar.com/avatar/e104df5b5a25b31cd17eba86e4a06cc9eda302f8a7242d14866107cf5e3c47a7?s=64&d=mm&r=g) guillermo barreda says:
    
    [October 15, 2015 at 3:23 pm](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1062203)
    
    this link will be helpful  
    [http://www.excel-easy.com/examples/consolidate.html](http://www.excel-easy.com/examples/consolidate.html)
      
    i have an excel group in facebook "Trucos Excel Peru" with 2,000 suscribers its in spanish  
    thank you for being awesome!!!
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1062203)
    
2.  ![](https://secure.gravatar.com/avatar/00c7b8ecb9920ce45cef23984c99c5fc6c62c27b65f5d11746e9745b57bd156a?s=64&d=mm&r=g) LAM says:
    
    [October 15, 2015 at 6:37 pm](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1062474)
    
    on the 2D part  
    changing static numbers with rand() and hitting F9 I've noticed that some of addresses could not be calculated  
    by changing sumproduct() to large() I've been able to always find the addresses, the only downside (or not) is that in case of doubles it will show the last value's address
    
    Min Address: {=ADDRESS(INDEX(ROW(A1:A4);LARGE((A1:D4=G6)\*(ROW(A1:D4));1));INDEX(COLUMN(A1:D1);LARGE((A1:D4=G6)\*(COLUMN(A1:D4));1));1;1)}  
    Max Address: {=ADDRESS(INDEX(ROW(A1:A4);LARGE((A1:D4=G7)\*(ROW(A1:D4));1));INDEX(COLUMN(A1:D1);LARGE((A1:D4=G7)\*(COLUMN(A1:D4));1));1;1)}
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1062474)
    
3.  ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
     says:
    
    [October 15, 2015 at 6:58 pm](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1062493)
    
    Hi Hui.
    
    Perhaps it should be pointed out that the SUMPRODUCT set-up will only work if the maximum (or minimum) value occurs precisely once across all worksheets?
    
    Based on the workbook provided, this alternative set-up will work even if the maximum (or minimum) value occurs more than once, giving the first occurrence in such cases (where leftmost and row-position are given preference over rightmost and column-position):
    
    \="'"&D3&"'!"&CELL("address",INDIRECT(TEXT(AGGREGATE(15,6,(10^5\*ROW(A1:C4)+COLUMN(A1:C4))/(INDIRECT("'"&D3&"'!A1:C4")=C3),1),"R0C00000"),0))
    
    For pre-Excel 2010, it's a simple CSE version of the above.
    
    The "R" and "C" in TEXT's format\_text parameter ("R0C00000") may require amending for Excel versions whose default language is not English.
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1062493)
    
4.  ![](https://secure.gravatar.com/avatar/9041859041cd28e5aa9263fddc22e53b0075f637771e934134f1982b756bfab9?s=64&d=mm&r=g) [Kevin Lehrbass](https://www.youtube.com/user/MySpreadsheetLab)
     says:
    
    [October 16, 2015 at 3:19 am](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1063133)
    
    Thanks Hui for these challenges!  
    Regarding the 2D challenge: Yes, the tricky part is if there are duplicates! Row and Column could get confused and the incorrect value could be returned.  
    I came up with this: =ADDRESS(MIN(IF(A1:D4=G6,ROW(A1:D4),"")),MIN(IF(A1:D4=G6,IF(ROW(A1:D4)=MIN(IF(A1:D4=G6,ROW(A1:D4),"")),COLUMN(A1:D4)))))  
    (array formula requiring Control Shift Enter).  
    It appears that it works if there are duplicates picking the 1st occurrence of min or max starting in top row from left to right.  
    I'm staying away from the 3D challenge for now!!  
    Cheers,  
    Kevin Lehrbass
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1063133)
    
5.  ![](https://secure.gravatar.com/avatar/3cdf9fe7a585c56d99c879d6e062c94cd52587814f8098379acf39d946fd145b?s=64&d=mm&r=g) [XOR LX](http://excelxor.com/)
     says:
    
    [October 16, 2015 at 8:17 am](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1063416)
    
    Another option for the 3D address, which is a touch longer than that I gave previously but has the advantage of being non-volatile:
    
    \="'"&D3&"'!"&ADDRESS(INT(1+MOD(MATCH(1,FREQUENCY(C3,Sheet1:Sheet3!A1:C4),0)-1,COUNT(Sheet1!A1:C4))/COUNTA(wsheets)),1+MOD(MATCH(1,FREQUENCY(C3,Sheet1:Sheet3!A1:C4),0)-1,COLUMNS(Sheet1!A1:C4)))
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1063416)
    
6.  ![](https://secure.gravatar.com/avatar/09e4099244803711f769d7bff2d77b5df5486c2731d82f93d3b4469d96d413c9?s=64&d=mm&r=g) Ajeet kumar Chauhan says:
    
    [November 10, 2015 at 7:21 am](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1078104)
    
    For MIN value:  
    \=ADDRESS(SMALL(IF($A$1:$F$6=MIN($A$1:$F$6),ROW($A$1:$F$6)),1),SMALL(IF($A$1:$F$6=MIN($A$1:$F$6),COLUMN($A$1:$F$6)),1)) with CSE
    
    For MAX value:  
    \=ADDRESS(SMALL(IF($A$1:$F$6=MAX($A$1:$F$6),ROW($A$1:$F$6)),1),SMALL(IF($A$1:$F$6=MAX($A$1:$F$6),COLUMN($A$1:$F$6)),1))
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1078104)
    
7.  ![](https://secure.gravatar.com/avatar/39758785b76618cbff2290d92ba7e63047379b49cf9e913405a6b80abdfd18b3?s=64&d=mm&r=g) Vishwas K V says:
    
    [January 7, 2016 at 6:49 am](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1117138)
    
    Hi,
    
    This is with regard to your post on 2D reverse lookup.
    
    I think still we can simplify the formula.
    
    Below is my formula. Please let me know if I am wrong.
    
    \=ADDRESS(SUMPRODUCT(((A1:D4=G7)\*ROW(A1:D4))),SUMPRODUCT(((A1:D4=G7)\*COLUMN(A1:D4))))
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#comment-1117138)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-039-find-the-cell-address-for-a-value-2d-3d-reverse-lookup/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Formula Forensics No. 038 – Find Which Worksheet a Max or Min Value is located on](https://chandoo.org/wp/formula-forensics-no-038-find-which-worksheet-a-max-or-min-value-is-on/) | [CP047: Best Excel tools for Entrepreneurs](https://chandoo.org/wp/cp047-excel-for-entrepreneurs/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)