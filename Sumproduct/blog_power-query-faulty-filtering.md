# Power Query: Faulty Filtering

**Source:** https://sumproduct.com/blog/power-query-faulty-filtering/

---

[Home](https://sumproduct.com/)

\> Power Query: Faulty Filtering

*   July 6, 2021

Power Query: Faulty Filtering
=============================

Power Query: Faulty Filtering
=============================

7 July 2021

_Welcome to our Power Query blog. This week I look at an issue with filtering._

I have some simple tent data which I am going to upload and process in Power Query. What could possibly go wrong?

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-168.jpg)

I upload the data to Power Query using ‘From Table/Range’ on the ‘Get & Transform Data’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-221.jpg)

I am prompted to choose the data for the table; I take the default area and select ‘My table has headers’.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-179.jpg)

My very simple table is created. I opt to filter on **Tent Type** to remove the _null_ values.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-174.jpg)

This is a simple process; just untick the _null_ values and click ‘OK’.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-146.jpg)

That all looks fine, so I close and load the data. For this example, I will load the data to the same sheet as the source data.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-129.jpg)

I can now view the tables side by side.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-121.jpg)

John has news. He sold a Medium tent in May. I add this to the table and refresh the query:

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-101.jpg)

John is not happy: his tent is missing!

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-91.jpg)

So, what happened? I need to go to my Power Query steps and check why the tent is missing.

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-78.jpg)

The **Changed Type** step looks fine: all the data is there. Something is wrong with the **Filtered Rows** step.

![](<Base64-Image-Removed>)

Here is the problem. The **M** code for this step has kept data where **Tent Type** is “Large” instead of removing _null_ values:

_**\= Table.SelectRows(#”Changed Type”, each (\[Tent Type\] = “Large”))**_

To be clear, I haven’t asked Power Query to do this. And yet, if I click on the gear icon next to the **Filtered Rows** step, it shows that only values equal to “Large” have been selected. Since Power Query is designed to process substantial amounts of data, it contains algorithms to create the most efficient code for each step. When I only had values of “Large” and _null,_ it took less processing to keep “Large”, rather than remove _null._ This is something to watch out for. I need to check that the **M** code is doing what I asked for. The cog next to a step will present this information in a user-friendly way, and I can change this so that I remove _null_ values.

![](<Base64-Image-Removed>)

Clicking ‘OK’ will give me the data I want.

![](<Base64-Image-Removed>)

The **M** code for the **Filtered Rows** step is now:

**\= Table.SelectRows(#”Changed Type”, each \[Tent Type\] <> null)**

which is what I wanted from the start. Now John is happy!

![](<Base64-Image-Removed>)

I could also have achieved this for the extended table by deleting and recreating the **Filtered Rows** step now that I have three values to choose from.

![](<Base64-Image-Removed>)

Now that removing the _null_ values is a more efficient route, Power Query is happy to oblige!

![](<Base64-Image-Removed>)

One last point here: there is a way to do this so that Power Query will write the **M** code in the way that I want for the **Filtered Rows** step for the original data.

![](<Base64-Image-Removed>)

The **M** code here is:

            **= Table.SelectRows(#”Changed Type”, each \[Tent Type\] <> null and \[Tent Type\] <> “”)**

I didn’t write the **M** code for this step; I made a different choice from the user interface:

![](<Base64-Image-Removed>)

This pushes Power Query to specifically take out nulls and empty entries, which will work as long as I want to get rid of the empty values too.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-faulty-filtering/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-faulty-filtering/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-faulty-filtering/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-faulty-filtering/#0)

[](https://sumproduct.com/blog/power-query-faulty-filtering/#0 "close")

top