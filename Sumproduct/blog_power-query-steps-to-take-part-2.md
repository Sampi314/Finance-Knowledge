# Power Query: Steps to Take – Part 2

**Source:** https://sumproduct.com/blog/power-query-steps-to-take-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Steps to Take – Part 2

*   September 20, 2022

Power Query: Steps to Take – Part 2
===================================

Power Query: Steps to Take – Part 2
===================================

21 September 2022

_Welcome to our Power Query blog. This week, I continue with my worked example by looking at dates._

The tent business has a new administrative assistant, who used to work in the United States. George has provided some information, but it’s not yet in a format I can use:

![](https://sumproduct.com/wp-content/uploads/2025/05/9f1d49df9a60ef61547ee3714359aacf.jpg)

Last time, I extracted the data and created a **Base** query. I took a Reference copy of **Base**.

![](https://sumproduct.com/wp-content/uploads/2025/05/18e02a2c3dfb5b099a530d8e00af3def.jpg)

This query was transformed and called **Quantities**:

![](https://sumproduct.com/wp-content/uploads/2025/05/2d9436ed556cb999c2b5a21e20f06d4f.jpg)

This week, I will create another query for the date information. As I said last week, there are a number of approaches I could take for this. I could ‘Merge as New’ **Base** and **Quantities** and take the ‘Left Anti’ option:

![](https://sumproduct.com/wp-content/uploads/2025/05/9668deb5c845b469f337efdec3c26ead.jpg)

(Note that to achieve this result I should first change the data type of **week 1** of **Base** to Text.  Whilst it will work for this data despite the datatype of **week 1** of **Base** being Any, it is not Best Practice to link columns where the datatype is not the same.  If I had a number in a column where the column type is Any, it would be treated like a number whereas if the column type was text, it would be treated as  text and therefore the join would fail.)

This would leave me with the rows of **Base** that are NOT in **Quantities**. Instead, for this example, I will make a Duplicate of **Quantities**:

![](https://sumproduct.com/wp-content/uploads/2025/05/06b3ab83d7f433a26fdce820a790bcbe.jpg)

The reason I have taken a duplicate this time, is that I want to change one of the steps. I want to amend the ‘Filtered Rows’ step to filter those rows that do contain the forward slash (**/**). I also rename the duplicate query **Dates**.

![](https://sumproduct.com/wp-content/uploads/2025/05/11c425472e9a91e8d60b30de58e5ef31.jpg)

I have further work to do on **Dates**, as the dates themselves do not look quite right: they are certainly not consistent.

![](https://sumproduct.com/wp-content/uploads/2025/05/e21df34c06e9e2c4948344c93c65a947.jpg)

Next time, I will transform the data so that the dates are in the correct format for my region.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-steps-to-take-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-steps-to-take-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-steps-to-take-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-steps-to-take-part-2/#0)

[](https://sumproduct.com/blog/power-query-steps-to-take-part-2/#0 "close")

top