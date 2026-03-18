# Power Query: Update with Caution

**Source:** https://sumproduct.com/blog/power-query-update-with-caution/

---

[Home](https://sumproduct.com/)

\> Power Query: Update with Caution

*   December 18, 2018

Power Query: Update with Caution
================================

Power Query: Update with Caution
================================

19 December 2018

_Welcome to our Power Query blog. This week, I look at how to update data in an SQL database._

When I saw a blog where someone had looked at updating data in an SQL database I just had to try it out for myself. I would stress that this is not a documented and supported use for Power Query, but it’s fun to push the boundaries of what it can do!

I begin in my SQL database where I create a new simple table:

![](<Base64-Image-Removed>)

Seasonal data! I create a new Excel workbook, and load the data from my SQL database to test the connections.

![](<Base64-Image-Removed>)

I create a blank query, where I will enter the **M** code to update my database.

![](<Base64-Image-Removed>)

Once in my new blank query, I can call the Advanced Editor.

![](<Base64-Image-Removed>)

I enter some **M** code that will update a row in my database.

![](<Base64-Image-Removed>)

I intend to change the present for Lucy…

**let**

    **fix\_christmas = Sql.Database(“DESKTOP-nnnnnSQLEXPRESS”,”KTNSQL”,\[Query=”UPDATE \[Christmas\] SET \[Present\]=’Coal’**\
\
                                                                                **WHERE \[Name\] = ‘Lucy'”\])**

 **in**

    **fix\_christmas**

This uses the **M** function **Sql.Database()**:

**Sql.Database(“server” as text, “database” as text, optional options as nullable record) as table**

This function allows manipulation of an SQL database. In this case, I have provided a server name (which I have amended here to protect my computer!), my database name ‘KTNSQL’ and an SQL query to update a row on my database.

Since I am updating the database, Power Query needs permission:

![](<Base64-Image-Removed>)

I allow the query to run.

![](<Base64-Image-Removed>)

I can check the data by refreshing my ‘Christmas’ query to extract data from the table:

![](<Base64-Image-Removed>)

I have successfully updated a row on my database.

I would stress that this is what programmers refer to as ‘an undocumented feature’! This means that it can only be used with caution. The help page on **Sql.Database()** does not mention updating the database, and it is entirely possible that this feature could be removed in the future. On the other hand, it could be developed into a supported function and add another string to the bow that is Power Query. Currently, it is not the most efficient way to update a database, but it’s interesting to know what’s possible!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-update-with-caution/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-update-with-caution/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-update-with-caution/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-update-with-caution/#0)

[](https://sumproduct.com/blog/power-query-update-with-caution/#0 "close")

top