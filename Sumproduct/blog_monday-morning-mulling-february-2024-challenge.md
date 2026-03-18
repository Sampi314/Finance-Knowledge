# Monday Morning Mulling: February 2024 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-february-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: February 2024 Challenge

*   February 25, 2024

Monday Morning Mulling: February 2024 Challenge
===============================================

Monday Morning Mulling: February 2024 Challenge
===============================================

26 February 2024

_On the final Friday of each month, set an Excel for you to puzzle over for the weekend. On the Monday, we publish one suggested solution. No-one is stating this is the best approach, it’s just the one we selected. If you don’t like it, lump it – or contact us with your preferred solution._

**_The Challenge_**

On Friday, we asked you to imagine you had a Table named **Data** in Excel, containing a list of names under the column **Name** and corresponding numerical data under the column **Grade** as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/ab80197a60a601b3d04aed560f4d795b.jpg)

Your task was to write a single Excel formula that summed the **Grade** data between two \[2\] names exclusively, which we referred to as **Name\_1** (Cell **G28**) and **Name\_2** (Cell **G29**). These names were inputs that could be changed, and the sum was to dynamically update to reflect the range of data between these two \[2\] names in the **Data** table. You could download the original question file[here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/Feb/sp-sum-if-between---starter-file.xlsx)
.

As always, there were some requirements:

*   the formula needs to be within just one \[1\] column (no “helper” cells)
*   the solution must work even if the order of **Name\_1** and **Name\_2** is swapped in the list
*   the formula should be dynamic so that it updates when a new entry is added.

**_Suggested Solution for Modern Excel Users (Excel 365 and Later Versions)_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/Feb/sp-sum-if-between---suggested-solutions.xlsx)
, which shows our suggested solution. The steps are detailed below.

**_Crafting a Data Range with XLOOKUP and Colon_**

We begin our formula with the [**XLOOKUP**](https://www.sumproduct.com/thought/xlookup-and-xmatch-two-new-x-men-for-excel)
 function, deploying it twice to accurately retrieve the grades corresponding to **Name\_1** and **Name\_2**.

**\=XLOOKUP(Name\_1,Data\[Name\],Data\[Grade\])**

**\=XLOOKUP(Name\_2,Data\[Name\],Data\[Grade\])**

This will return us the respective grades for **Name\_1** and **Name\_2**:

![](<Base64-Image-Removed>)

The real magic happens when we introduce a colon ‘:’ between these two \[2\] [**XLOOKUP**](https://www.sumproduct.com/thought/xlookup-and-xmatch-two-new-x-men-for-excel)
 functions. This action forms a dynamic array that spans from the grade of **Name\_1** to that of **Name\_2**.

**\=XLOOKUP(Name\_1,Data\[Name\],Data\[Grade\]):XLOOKUP(Name\_2,Data\[Name\],Data\[Grade\])**

![](<Base64-Image-Removed>)

Even if the names selected from the dropdown are not in sequential order, this formula dynamically adjusts, ensuring the correct range is captured:

![](<Base64-Image-Removed>)

**_Refining the Range with DROP_**

At this stage, while we could directly sum the array and then subtract the two \[2\] values of the lookup, we opt for a more refined approach by incorporating the [**DROP**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-drop-function)
 function. This function is instrumental in sculpting our dynamic range further before performing the summation.

We can use:

**\=DROP(Range,1)**

and

**\=DROP(Range,-1)**

to remove the first and last entries in our range, the grades directly associated with **Name\_1** and **Name\_2**.

Let’s combine all of that in this formula:

**\=DROP(DROP(Range,1),-1)**

This formula removes the first and last row of our **Range**. When we substitute **Range** with our earlier [**XLOOKUP**](https://www.sumproduct.com/thought/xlookup-and-xmatch-two-new-x-men-for-excel)
 array, this returns the exact range we wish to sum:

**\=DROP(DROP(XLOOKUP(Name\_1,Data\[Name\],Data\[Grade\]):XLOOKUP(Name\_2,Data\[Name\],Data\[Grade\]),1),-1)**

![](<Base64-Image-Removed>)

**_SUM and Error Trapping_**

The penultimate step here is to **SUM**, hence we quickly add the **SUM** functionhere:

**\=SUM(DROP(DROP(XLOOKUP(Name\_1,Data\[Name\],Data\[Grade\]):XLOOKUP(Name\_2,Data\[Name\],Data\[Grade\]),1),-1))**

![](<Base64-Image-Removed>)

However, we must consider edge cases, such as the non-selection of names or the selection of adjacent names, which could lead to errors in our formula:

![](<Base64-Image-Removed>)

To address this, we wrap our summation formula within an [**IFERROR**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-iferror-function)
 statement.

**\=IFERROR(SUM(DROP(DROP(XLOOKUP(Name\_1,Data\[Name\],Data\[Grade\]):XLOOKUP(Name\_2,Data\[Name\],Data\[Grade\]),1),-1)),0)**

![](<Base64-Image-Removed>)

This formula not only performs the desired summation but also ensures that in cases where our formula would return an error, it returns a zero \[0\] instead.

We have created a resilient, dynamic and accurate formula that sums the data between the specified names whilst avoiding any errors.

**_Suggested Solution for Legacy Excel Users (Older Versions of Excel)_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/Feb/sp-sum-if-between---suggested-solutions.xlsx)
, which shows our suggested solution. The steps are detailed below.

**_Using INDEX MATCH and Colon to Create a Data Range_**

In a manner akin to the approach for modern Excel users, we will use the [**INDEX MATCH**](https://www.sumproduct.com/thought/index-match)
 partnership combined with a colon to define the data range. This method uses

**\=INDEX(Data\[Grade\],MATCH(Name\_1,Data\[Name\],0))**

to locate the grade for **Name\_1**. Similarly,

**\=INDEX(Data\[Grade\],MATCH(Name\_2,Data\[Name\],0))**

The above formula is employed to find the grade for **Name\_2**.

Placing a colon between these two \[2\] formulae creates a range spanning from the grade of **Name\_1** to **Name\_2**, _viz._

**\=INDEX(Data\[Grade\],MATCH(Name\_1,Data\[Name\],0)):INDEX(Data\[Grade\],MATCH(Name\_2,Data\[Name\],0))**

![](<Base64-Image-Removed>)

**_Making it Exclusive_**

To exclusively select the data between **Name\_1** and **Name\_2**, we introduce the [**MAX**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-max-function)
 and [**MIN**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-min-function)
 functions. These functions are employed to determine the endpoints of our data range:

**\=MAX(MATCH(Name\_1,Data\[Name\],0),MATCH(Name\_2,Data\[Name\],0))**

This formula is used to find the last position in the data range.

**\=MIN(MATCH(Name\_1,Data\[Name\],0),MATCH(Name\_2,Data\[Name\],0))**

Similarly, this above formula identifies the first position.

Subsequently, we modify our original **INDEX:INDEX** formula to replicate the effect of the [**DROP**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-drop-function)
 function used in the modern Excel solution:

**\=INDEX(Data\[Grade\],MIN(MATCH(Name\_1,Data\[Name\],0),MATCH(Name\_2,Data\[Name\],0))+1):  
INDEX(Data\[Grade\],MAX(MATCH(Name\_1,Data\[Name\],0),MATCH(Name\_2,Data\[Name\],0))-1)**

![](<Base64-Image-Removed>)

**_Addressing Specific Selection Scenarios_**

While effective, our method may not be perfect in all cases. For instance, if **Name\_1** and **Name\_2** are adjacent, the same name is selected twice or the input cells are left empty, the formula might produce an incorrect range or result in an error.

![](<Base64-Image-Removed>)

To address this, we implement the following formula:

**\=IFERROR(ABS(MATCH(Name\_1,Data\[Name\],0)-MATCH(Name\_2,Data\[Name\],0)),0)<=1**

![](<Base64-Image-Removed>)

This formula utilises **ABS** and [**MATCH**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-match-function)
 functions to detect if **Name\_1** and **Name\_2** are adjacent or identical. Additionally, the [**IFERROR**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-iferror-function)
 function will intercept any _#N/A_ errors from the [**MATCH**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-match-function)
 function being unable to match any name and then convert them to zero \[0\]. The subsequent comparison (**<=1**) checks if the range is suitable for summation. We encapsulate this logic within a comprehensive [**IF**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-if-function)
 statement:

**\=IF(IFERROR(ABS(MATCH(Name\_1,Data\[Name\],0)-MATCH(Name\_2,Data\[Name\],0)),0)<=1,  
0, SUM(INDEX(Data\[Grade\],  
MIN(MATCH(Name\_1,Data\[Name\],0),MATCH(Name\_2,Data\[Name\],0))+1) :  
INDEX(Data\[Grade\],  
MAX(MATCH(Name\_1,Data\[Name\],0),MATCH(Name\_2,Data\[Name\],0))-1)))**

![](<Base64-Image-Removed>)

This approach ensures an accurate and exclusive summation between the selected names, catering to the nuances of legacy Excel.

**_Word to the Wise_**

We appreciate there are many, many ways this could have been achieved. If you have come up with an alternative, radically different approach, congratulations – that’s half the fun of Excel!

_The Final Friday Fix will return on Friday 29 March 2024 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-february-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-february-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-february-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-february-2024-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-february-2024-challenge/#0 "close")

top