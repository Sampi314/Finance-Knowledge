# Power Query: Candid Columns

**Source:** https://sumproduct.com/blog/power-query-candid-columns/

---

[Home](https://sumproduct.com/)

\> Power Query: Candid Columns

*   May 29, 2018

Power Query: Candid Columns
===========================

Power Query: Candid Columns
===========================

30 May 2018

_Welcome to our Power Query blog. This week, I look at an example where data comes in one Excel column and needs to be converted to a table._

Not all data arrives in Excel in nicely organised tables. John the imaginary salesperson has sent in some new contacts, which he has copied to a worksheet:

![](https://sumproduct.com/wp-content/uploads/2025/05/ea4fc2b2ef1b22221354272315e5f995.jpg)

I have a list of names and addresses in a column. I would like them to be in a table, where I can extract the name, address, country and post code (aka zip code). I start by creating a new query from my data using the ‘From Table’ option in the ‘Get & Transform’ section on the ‘Data’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/acb97c5c06e976dd42a9f9d21d4a8c47.jpg)

Power Query asks me to confirm where my table is, and whether it has headers (no, thanks to John, it doesn’t!). The default looks fine so I click ‘OK’.

![](https://sumproduct.com/wp-content/uploads/2025/05/2baa5c6842ca34fc2a3832cd55f87f6f.jpg)

My data is extracted, and now I can set about transforming it into a useful table. Since my data is grouped into five rows for each address (and in this case I can rely on this being consistent because it comes from a database which ensures this), it would be useful to count which row I am on. I can do this by creating an index column. In the ‘Add Column’ tab, I choose ‘Index Column’ in the ‘General’ section, and start my column from 1.

![](https://sumproduct.com/wp-content/uploads/2025/05/97c2b92fc75a0e225164b0754b25b0e0.jpg)

Having created my column I now have some mathematical possibilities.

![](https://sumproduct.com/wp-content/uploads/2025/05/b02852bcd312a3dbe5f5cd19025cc824.jpg)

I am going to use the function **Number.Mod()** to determine where each address starts. **Number.Mod()** divides one number by another number and gives the remainder. This is similar to the [**MOD** function](https://www.sumproduct.com/thought/a-modicum-of-mod)
 in Excel.

`**Number.**`**Mod**`**(number**` **as** `**nullable number, divisor**` **as** `**nullable number,**` **optional** `**precision**` **as** `**nullable number)**` **as** `**nullable number**`

It’s much clearer to see it in practice. To see where each address starts, I divide the index by five and look at the remainder. I create a new ‘Custom Column’ _viz._

![](<Base64-Image-Removed>)

I click ‘OK’ to create my new column.

![](https://sumproduct.com/wp-content/uploads/2025/05/107340169076ca8a52d5b3668e96230b.jpg)

My aim is to indicate which address lines belong together, by giving them the same value. I am going to do this with a running total (for more details on how to create a running total, please see [Power Query: One Route to a Running Total](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-one-route-to-a-running-total)
.

My first step is to only count at the beginning of each address, and to do this I create another column, which this time is a ‘Conditional Column’:

![](https://sumproduct.com/wp-content/uploads/2025/05/11d67a2b8bbf65325b37984a20bf9f8c.jpg)

This column will be 1 for the first line and zero for the rest.

![](https://sumproduct.com/wp-content/uploads/2025/05/72f14c43040806988167fdcdbda21851.jpg)

I can now create another ‘Custom Column’ for my running total.

![](https://sumproduct.com/wp-content/uploads/2025/05/4bd8bfa7ea02a00e96a6f55755726c0c.jpg)

This gives me the same value for each line belonging to the same address.

![](https://sumproduct.com/wp-content/uploads/2025/05/41e9a6429ccc88fb96bcd14470b4797d.jpg)

Now I have a way to identify each address, I am ready to pivot my data. I no longer need my **_index_** or **_Address\_Key_** columns, so I can remove these first.

On the ‘Transform’ tab I select **_Address\_Line_** and choose to pivot my data. The values will be in **_Column1_** and I don’t want to aggregate.

![](<Base64-Image-Removed>)

I click ‘OK’ to see my data.

![](<Base64-Image-Removed>)

This is looking much better. My **Address\_ID** column is populated correctly, so I just need to rename my other columns.

![](<Base64-Image-Removed>)

This data is now ready to ‘Close & Load’ to Excel from the ‘File’ tab. If John uses the same Excel worksheet and adds more addresses (or updates any existing ones) then they can be refreshed into the table too.

![](<Base64-Image-Removed>)

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-candid-columns/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-candid-columns/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-candid-columns/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-candid-columns/#0)

[](https://sumproduct.com/blog/power-query-candid-columns/#0 "close")

top