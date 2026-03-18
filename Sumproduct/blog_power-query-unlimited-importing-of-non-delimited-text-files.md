# Power Query: Unlimited Importing of Non-Delimited Text Files

**Source:** https://sumproduct.com/blog/power-query-unlimited-importing-of-non-delimited-text-files/

---

[Home](https://sumproduct.com/)

\> Power Query: Unlimited Importing of Non-Delimited Text Files

*   March 9, 2017

Power Query: Unlimited Importing of Non-Delimited Text Files
============================================================

Power Query: Unlimited Importing of Non-Delimited Text Files
============================================================

10 March 2017

_Welcome to our Power Query blog. Today I look at importing data from non-delimited text files._

As a programmer, I was often asked to produce delimited versions of reports which could easily be picked up by Excel. Whilst it is possible to clean non-delimited files in Excel, it’s a laborious and repetitive process, which is why it made more sense to pay for a programmer to automate it. Power Query is a **free** method of cleaning up these files, and since the steps are recorded, it can be reapplied.

I begin by creating a new query from my file, as shown below:

![](https://sumproduct.com/wp-content/uploads/2025/05/f69a0d9fd50a89ab6f02b9f08555dc2b.jpg)

I browse to my file and select it. Power Query has had a valiant effort at delimiting my data as there happened to be a colon between the ‘Name’ title and the name, but most of it is in one column. My goal is to split the data into more columns.

![](https://sumproduct.com/wp-content/uploads/2025/05/11ac921c4a078e6b2fd8cf0c6140873d.jpg)

The first four rows don’t include any data I want, so I am going to edit and get rid of these. In the ‘Home’ tab, there is a section to do just this:

![](https://sumproduct.com/wp-content/uploads/2025/05/6fdfdf55ed0962ecf69a51ccf8164f69.jpg)

I remove the first four rows and then the blank row after the Name row. I could have done this in one step by just removing the blank rows, as shown below:

![](https://sumproduct.com/wp-content/uploads/2025/05/d8bf31c64901869a2734b7bc875b948e.jpg)

Now I want to populate **_Column2_** all the way down. I described this process in detail in **_[Getting Started](https://sumproduct.com/blog/power-query-getting-started/)
_** where I replace the blank names with null and then fill down. I can then remove the first row and rename the column:

![](https://sumproduct.com/wp-content/uploads/2025/05/8993de5dd33606568b75339f6b735b7f.jpg)

In order to make sure my data in **_Column1_** is as clean as it can be, I trim and clean it in order to remove any leading and trailing spaces, along with any annoying escape codes. Right-clicking the column reveals these options:

![](<Base64-Image-Removed>)

The next step is to break up the data in column 1, and to do this, there is a ‘Split Column’ option in the ‘Home’ section:

![](<Base64-Image-Removed>)

I make a guess at where to split my data – since I can edit the step by clicking on the gear next to the step in the ‘APPLIED STEPS’ window, I can adjust this until my data looks right.

![](<Base64-Image-Removed>)

My date data looks good. For my new column **_Column1.2_**, I use the ‘£’ sign as a delimiter instead of using a count because my expense codes vary in length:

![](<Base64-Image-Removed>)

The end result looks promising.

![](<Base64-Image-Removed>)

There’s not much point trying to use my top row as headings, so I delete the top row and rename the columns.

![](<Base64-Image-Removed>)

The data looks ready to load. This query can be applied to another delimited expenses text file that comes through in a similar format, and the steps can be adjusted as required.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-unlimited-importing-of-non-delimited-text-files/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-unlimited-importing-of-non-delimited-text-files/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-unlimited-importing-of-non-delimited-text-files/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-unlimited-importing-of-non-delimited-text-files/#0)

[](https://sumproduct.com/blog/power-query-unlimited-importing-of-non-delimited-text-files/#0 "close")

top