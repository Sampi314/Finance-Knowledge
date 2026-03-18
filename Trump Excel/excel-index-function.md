# Excel INDEX Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-index-function

---

[Skip to content](https://trumpexcel.com/excel-index-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-index-function/#below-title)

Excel INDEX Function (Examples + Video)
---------------------------------------

![Excel INDEX Function](https://trumpexcel.com/wp-content/uploads/2014/03/INDEX-FORMULA-EXCEL.png)

### When to use Excel INDEX Function

Excel INDEX function can be used when you want to fetch the value from a tabular data and you have the row number and column number of the data point. For example, in the example below, you can use the INDEX function to get the marks of ‘Tom’ in Physics when you know the row number and the column number in the data set.

##### ![Excel INDEX Funtion - Example 1](https://trumpexcel.com/wp-content/uploads/2014/03/Excel-INDEX-Funtion-Example-1.png)

### What it Returns

It returns the value from a table for the specified row number and column number.

### Syntax

\=INDEX (array, row\_num, \[col\_num\])  
\=INDEX (array, row\_num, \[col\_num\], \[area\_num\])

INDEX function has 2 syntax. The first one is used in most cases, however, in case of three-way lookups, the second one is used (covered in Example 5).

### Input Arguments

*   **array –** a range of cells or an array constant.
*   **row\_num –** the row number from which the value is to be fetched.
*   **\[col\_num\] –** the column number from which the value is to be fetched. Although this is an optional argument, but if row\_num is not provided, it needs to be given.
*   **\[area\_num\] –** (Optional) If array argument is made up of multiple ranges, this number would be used to select the reference from all the ranges.

### Additional Notes (Boring Stuff.. But Important to Know)

*   If the row number or the column number is 0, it returns the values of the entire row or column respectively.
*   If INDEX function is used in front of a cell reference (such as A1:) it returns a cell reference instead of a value (see examples below).
*   Most widely used along with the [MATCH function](https://trumpexcel.com/excel-match-function/)
    .
*   Unlike [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
    , INDEX function can return a value from the left of the lookup value.
*   INDEX function have two forms – Array form and the Reference form
    *   ‘Array form’ is where you fetch a value based on row and column number from a given table.
    *   ‘Reference form’ is where there are multiple tables, and you use the area\_num argument to select the table and then fetch a value within it using the row and column number (see live example below).

Excel INDEX Function – Examples
-------------------------------

Here are six examples of using Excel INDEX Function.

### **Example 1 – Finding Tom’s Marks in Physics (a two-way lookup)**

Suppose you have a dataset as shown below:

![Excel INDEX Funtion - Example 1](https://trumpexcel.com/wp-content/uploads/2014/03/Excel-INDEX-Funtion-Example-1.png)

To find Tom’s marks in Physics, use the below formula:

\=INDEX($B$3:$E$10,3,2)

This INDEX formula specifies the array as $B$3:$E$10 which has the marks for all the subjects. Then it uses the row number (3) and column number (2) to fetch Tom’s marks in Physics.

### **Example 2 – Making the LOOKUP Value Dynamic using MATCH Function**

It may not always be possible to specify the row number and the column number manually. You may have a huge data set, or you may want to make it dynamic so that it automatically identifies the name and/or subject specified in cells and give the correct result.

Something as shown below:

![Excel INDEX Function - Example 2 - Dynamic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20288'%3E%3C/svg%3E)

This can be done using a combination of the INDEX and the [MATCH](https://trumpexcel.com/excel-match-function/)
 function.

Here is the formula that will make the lookup values dynamic:

\=INDEX($B$3:$E$10,MATCH($G$5,$A$3:$A$10,0),MATCH($H$4,$B$2:$E$2,0))

In the above formula, instead of hard-coding the row number and the column number, MATCH function is used to make it dynamic.

*   Dynamic Row Number is given by the following part of the formula – MATCH($G$5,$A$3:$A$10,0). It scans the name of students and identifies the lookup value ($G$5 in this case). It then returns the row number of the lookup value in the dataset. For example, if the lookup value is Matt, it’ll return 1, if it is Bob, it’ll return 2 and so on.
*   Dynamic Column Number is given by the following part of the formula – MATCH($H$4,$B$2:$E$2,0). It scans the subject names and identifies the lookup value ($H$4 in this case). It then returns the column number of the lookup value in the dataset. For example, if the lookup value is Math, it’ll return 1, if it is Physics, it’ll return 2 and so on.

### **Example 3 – Using Drop Down Lists as Lookup Values**

In the above example, we have to manually enter the data. That could be time-consuming and error-prone, especially if you have a huge list of lookup values.

A good idea in such cases is to create a drop down list of the lookup values (in this case, it could be student names and subjects) and then simply choose from the list. Based on the selection, the formula would automatically update the result.

Something as shown below:

![Excel INDEX Function - Example 3 - Dynamic Drop Downs](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20288'%3E%3C/svg%3E)

This makes a good dashboard component as you can have a huge data set with hundreds of students at the back end, but the end user (let’s say a teacher) can quickly get the marks of a student in a subject by simply making the selections from the drop down.

**How to make this:**

The formula used in this case is the same used in Example 2.

\=INDEX($B$3:$E$10,MATCH($G$5,$A$3:$A$10,0),MATCH($H$4,$B$2:$E$2,0))

The lookup values have been converted into drop-down lists.

Here are the steps to create the [Excel drop down list](https://trumpexcel.com/excel-drop-down-list/)
:

*   Select the cell in which you want the drop-down list. In this example, in G4, we want the student names.
*   Go to Data –> Data Tools –> Data Validation.
*   In the Data Validation Dialogue box, within the settings tab, select List from the Allow drop-down.
*   In the source, select $A$3:$A$10
*   Click OK.

Now you’ll have the drop-down list in cell G5. Similarly, you can create one in H4 for the subjects.

### **Example 4 – Return Values from an Entire Row/Column**

In the above examples, we’ve used Excel INDEX function to do a 2-way lookup and get a single value.

Now, what if you want to get all the marks of a student. This can enable you to find the maximum/minimum score of that student, or the total marks scored in all subjects.

In simple English, you want to first get the entire row of scores for a student (let’s say Bob) and then within those values identify the highest score or the total of all the scores.

Here is the trick.

In Excel INDEX Function, when you enter the **_column number as 0_**, it will return the values of that entire row.

So the formula for this would be:

\=INDEX($B$3:$E$10,MATCH($G$5,$A$3:$A$10,0),0)

Now this formula. if used as is, would return the #VALUE! error. While it displays the error, in the backend, it returns an array that has all the scores for Tom – {57,77,91,91}.

If you select the formula in the edit mode and press F9, you’ll be able to see the array it returns (as shown below): ![Excel INDEX Function - Example 4 Entire Row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20288'%3E%3C/svg%3E)

Similarly, based on what the lookup value is, when the column number is specified as 0 (or is left blank), it returns all the values in the row for the lookup value

Now to calculate the total score obtained by Tom, we can simply use the above formula within the SUM function.

\=SUM(INDEX($B$3:$E$10,MATCH($G$5,$A$3:$A$10,0),0))

On similar lines, to calculate the highest score, we can use MAX/LARGE and to calculate minimum, we can use MIN/SMALL.

![Excel INDEX Function - Example 4 Entire Row Highest SUM](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20726%20223'%3E%3C/svg%3E)

### **Example 5 – Three Way Lookup Using INDEX/MATCH**

Excel INDEX function is built to handle three-way lookups.

What is a three-way lookup?

In the above examples, we’ve used one table with scores for students in different subjects. This is an example of a two-way lookup as we use two variables to fetch the score (student’s name and the subject).

Now, suppose in a year, a student has three different levels of exams, Unit Test, Midterm, and Final Examination (that’s what I had when I was a student).

A three-way lookup would be the ability to get a student’s marks for a specified subject from the specified level of exam. This would make it a three-way lookup as there are three variables (student’s name, subject’s name, and the level of examination).

Here is an example of a three-way lookup:

![Excel INDEX Function - Example 5 - Three Way Lookup](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20688%20500'%3E%3C/svg%3E)

In the example above, apart from selecting the student’s name and subject name, you can also select the level of exam. Based on the level of exam, it returns the matching value from one of the three tables.

Here is the formula used in cell H4:

\=INDEX(($B$3:$E$7,$B$11:$E$15,$B$19:$E$23),MATCH($G$4,$A$3:$A$7,0),MATCH($H$3,$B$2:$E$2,0),IF($H$2="Unit Test",1,IF($H$2="Midterm",2,3)))

Let’s break down this formula to understand how it works.

This formula takes four arguments. INDEX is one of those functions in Excel that has more than one syntax.

\=INDEX (array, row\_num, \[col\_num\])  
\=INDEX (array, row\_num, \[col\_num\], \[area\_num\])

So far in all the example above, we have used the first syntax, but to do a three-way lookup, we need to use the second syntax.

Now let’s see each part of the formula based on the second syntax.

*   array – ($B$3:$E$7,$B$11:$E$15,$B$19:$E$23): Instead of using a single array, in this case, we have used three arrays within parenthesis.
*   row\_num – MATCH($G$4,$A$3:$A$7,0): MATCH function is used to find the position of the student’s name in cell $G$4 in the list of student’s name.
*   col\_num – MATCH($H$3,$B$2:$E$2,0): MATCH function is used to find the position of the subject name in cell $H$3 in the list of subject’s name.
*   \[area\_num\] – IF($H$2=”Unit Test”,1,IF($H$2=”Midterm”,2,3)): The area number value tells the INDEX function which array to select. In this example, we have three arrays in the first argument. If you select Unit Test from the drop-down, the IF function returns 1 and the INDEX functions select 1st array from the three arrays (which is $B$3:$E$7).

### Example 6 – Creating a Reference Using the INDEX Function (Dynamic Named Ranges)

This is one wild use of the Excel INDEX function.

Let’s take a simple example.

I have a list of names as shown below:

![Excel Index Function - Example 6 - Reference](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20138%20260'%3E%3C/svg%3E)

Now I can use a simple INDEX function to get the last name on the list.

Here is the formula:

\=INDEX($A$2:$A$9,COUNTA($A$2:$A$9))

This function simply counts the number of cells that are not empty and returns the last item from this list (it works only when there are no blanks in the list).![Excel INDEX Function - Reference 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20268'%3E%3C/svg%3E)

Now, what here comes the magic.

If you put the formula in front of a cell reference, the formula would return a cell reference of the matching value (instead of the value itself).

\=A2:INDEX($A$2:$A$9,[COUNTA](https://trumpexcel.com/excel-functions/counta-function/)
($A$2:$A$9))

You would expect the above formula to return =A2:”Josh” (where Josh is the last value in the list). However, it returns =A2:A9 and hence you get an array of names as shown below:![Excel INDEX Functions - References 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20424%20316'%3E%3C/svg%3E)

One practical example where this technique can be helpful is in creating [dynamic named ranges](https://trumpexcel.com/named-ranges-in-excel/)
.

That’s it in this tutorial. I’ve tried to cover major examples of using the Excel INDEX function. If you would like to see more examples added to this list, let me know in the comments section.

Note: I’ve tried my best to proof read this tutorial, but in case you find any errors or spelling mistakes, please let me know 🙂

Excel INDEX Function – Video Tutorial
-------------------------------------

**Related Excel Functions:**

*   [Excel VLOOKUP Function](https://trumpexcel.com/excel-vlookup-function/)
    .
*   [Excel HLOOKUP Function](https://trumpexcel.com/excel-hlookup-function/)
    .
*   [Excel INDIRECT Function](https://trumpexcel.com/excel-indirect-function/)
    .
*   [Excel MATCH Function](https://trumpexcel.com/excel-match-function/)
    .
*   [Excel OFFSET Function](https://trumpexcel.com/excel-offset-function/)
    .

**You May Also Like the Following Excel Tutorials:**

*   [VLOOKUP Vs. INDEX/MATCH](https://trumpexcel.com/vlookup-vs-index-match/)
    
*   [Excel Index Match](https://trumpexcel.com/index-match/)
    
*   [Lookup and Return Values in an Entire Row/Column](https://trumpexcel.com/lookup-and-return-values-entire-row-column-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

10 thoughts on “Excel INDEX Function | Formula Examples + FREE Video”
---------------------------------------------------------------------

1.  your explanation is very clear and helpful.
    
    I need many exercises for index and match functions
    
    [Reply](https://trumpexcel.com/excel-index-function/#comment-41355)
    
2.  what is the practical use of Example 6?
    
    [Reply](https://trumpexcel.com/excel-index-function/#comment-14581)
    
3.  Example 5 IS NOT WORKING… if you have a video explaining about Three Way Lookup Using INDEX/MATCH will be great..  
    Tried many times but it is showing error….
    
    [Reply](https://trumpexcel.com/excel-index-function/#comment-14268)
    
4.  how can use index function to compare my student’s mark correct or not?
    
    [Reply](https://trumpexcel.com/excel-index-function/#comment-11745)
    
5.  Thanks for your helpful resource. Please do option to download the practice sheet in this regard. That will helps easily particle on above mention examples.
    
    [Reply](https://trumpexcel.com/excel-index-function/#comment-11261)
    
6.  hi  
    can you please help me in putting all non blank values from different column to one column.  
    i have values in 30 columns (coming by another formula – and changing each time) i wants to put all non blank values in one column (better if it ignore duplicate)
    
    [Reply](https://trumpexcel.com/excel-index-function/#comment-10767)
    
7.  These resources are quite helpful
    
    [Reply](https://trumpexcel.com/excel-index-function/#comment-10738)
    
8.  Thanks for the helpful resource. I ran across what seems like a bug in Excel’s INDEX() function, and am curious if others have run into this.
    
    In the attached image, note how Excel’s treatment of a value of 0 for row or column depends on the location of the function. In call B3, a reference to row 1, col 0 results in an unexpected/unwanted result of 2 (the contents at row 1, column 2). In cell C1, a reference to row 0, col 1 results in an unexpected/unwanted result of 1 (the contents at row 1, column 1).
    
    If, however, the same function calls are located outside of the row and column range of the array, the function returns #VALUE!, as expected, for an out of range reference. See cells D5 and E3, which are the exact same function calls as B3 and C1, respectively.
    
    Is there any known reason why the function behaves differently depending on where it is placed relative to the target array? Is this behavior documented?
    
    Thanks for any insight.
    
    [https://uploads.disquscdn.com/images/2b5614ecfaed959af45c64b066ab9d8e7ea330f1c6f4aaece611d6c9598005ab.jpg](https://uploads.disquscdn.com/images/2b5614ecfaed959af45c64b066ab9d8e7ea330f1c6f4aaece611d6c9598005ab.jpg)
    
    [Reply](https://trumpexcel.com/excel-index-function/#comment-5626)
    
9.  \=SUM(INDEX($B$3:$E$10,MATCH($G$5,$A$3:$A$10,0),0),1) , in this formula why did you use “,1” at the end.
    
    [Reply](https://trumpexcel.com/excel-index-function/#comment-3925)
    
    *   Hey Deepak.. Thanks for pointing out.. It was a typo.. have corrected it.
        
        [Reply](https://trumpexcel.com/excel-index-function/#comment-3926)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-index-function/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK