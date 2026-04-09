# Power Query: Power Query Online – Part 9

**Source:** https://sumproduct.com/blog/power-query-power-query-online-part-9/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query Online – Part 9

*   October 3, 2023

Power Query: Power Query Online – Part 9
========================================

Power Query: Power Query Online – Part 9
========================================

4 October 2023

_Welcome to our Power Query blog. Today, I look at the use of keys in Power Query Online._

In the current series, I am looking at Power Query Online, which I have accessed from Power Apps:

![](https://sumproduct.com/wp-content/uploads/2025/05/0554ee67d50fbe0d6ae9b31d809bf205.jpg)

[Last week](https://sumproduct.com/blog/power-query-power-query-online-part-8/)
, I looked at the functionality on the ‘Schema tools’ tab, which allowed me to set a column as a key.

![](https://sumproduct.com/wp-content/uploads/2025/05/a98905ec14dbf023a27d38fd25b362b7.jpg)

I chose to do this for **Country Code**:

![](https://sumproduct.com/wp-content/uploads/2025/05/a747193be7c6b0ed76da0d33ca7e8adb.jpg)

To see how keys can be useful in making processes more efficient, I note how long it takes for me to refresh the **Merge** query that I created in [part 7](https://sumproduct.com/blog/power-query-power-query-online-part-7/)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/93b27341d0b5187c3df29b3eec8a15bb.jpg)

The key symbol now appears next to the **Country Code** column. The key icons make it much easier to see where the keys are when I am merging data. Note the time at the bottom-left of the screen:

![](https://sumproduct.com/wp-content/uploads/2025/05/2efe1912cb6758f6cd53e70295e7b130.jpg)

On the query **Population Data**, I mark the column **2-alpha code** as a key, using the option on the ‘Schema tools’ tab in the schema view. This was the column I selected in **Population Data** when I merged it with **Region Data**.

![](https://sumproduct.com/wp-content/uploads/2025/05/c2da2836be5a420cf6c72f076f850f69.jpg)

Then, in the query **Region Data**, I again mark **2-alpha code** as a key:

![](https://sumproduct.com/wp-content/uploads/2025/05/95d1dbaa3413d94d34b40dcdd94e4995.jpg)

Now, I go back to the data view, and refresh **Merge** again:

![](https://sumproduct.com/wp-content/uploads/2025/05/a3fc25620ebe53fa82a14f2174b0306e.jpg)

Notice first that the column **2-alpha code** on the merged table is now marked as a key (since it came from **Population Data**). The time has improved:

![](https://sumproduct.com/wp-content/uploads/2025/05/723c7c9437ed52133a6349035dde7188.jpg)

Ideally all the keys should be numeric, as these are more efficient to store, but this simple example has shown that marking the correct columns as keys can help when loading data. That’s it for this week; next time, I will look at how I can use the diagram view when analysing my queries.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-power-query-online-part-9/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-online-part-9/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-online-part-9/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-online-part-9/#0)

[](https://sumproduct.com/blog/power-query-power-query-online-part-9/#0 "close")

top