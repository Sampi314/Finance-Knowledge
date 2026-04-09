# Power Query: Seeded Accommodating Accumulating

**Source:** https://sumproduct.com/blog/power-query-seeded-accommodating-accumulating/

---

[Home](https://sumproduct.com/)

\> Power Query: Seeded Accommodating Accumulating

*   March 27, 2018

Power Query: Seeded Accommodating Accumulating
==============================================

Power Query: Seeded Accommodating Accumulating
==============================================

28 March 2018

_Welcome to our Power Query blog. This week, I look at the M function List.Accumulate and its uses where the seed is not zero._

As I described [last week](https://sumproduct.com/blog/power-query-seedless-accommodating-accumulating/)
, the **List.Accumulate** function can transform data by performing several steps at once, and the description is below:

“…Accumulates a result from the list. Starting from the initial value seed this function applies the **accumulator** function and returns the final result…”

**List.Accumulate(list as list, seed as any, accumulator as function) as any** 

where

**list** = The list to check

               **seed** = the initial value seed

               **accumulator** = the value accumulator function

[Last week](https://sumproduct.com/blog/power-query-seedless-accommodating-accumulating/)
, I looked at some examples where the ‘seed’ is usually set to zero (summing and counting). This time, I am looking at examples where the ‘seed’ is not zero. I am going to provide some examples as a demonstration here: maximum, multiplication, concatenation and record conditions.

**_Maximum_**

There is a **List.Max** function in **M** language which could be used to do achieve this goal, so I will be comparing the results from this with my **List.Accumulate** calculation. I begin with another list, just for a change:

![](<Base64-Image-Removed>)

I create a new blank query which uses **List.Accumulate**.

![](<Base64-Image-Removed>)

And, just to show that **List.Max** gives me the same value:

![](<Base64-Image-Removed>)

Going back to my **List.Accumulate** syntax, I have:

**\= List.Accumulate(Simple\_List2, 0,(state,current)=>if state>current then state else current)**

This time, **List.Accumulate** goes through each item in my list and updates ‘**state**‘ if the ‘**current**‘ value is greater than the greatest so far

**Current State New Value for State**

10 0 10

100 10 100

20 100 100

50 100 100

100 100 100

30 100 100

40 100 100

In this case, I have set the ‘seed’ to zero (0), but it just needs to be less than or equal to the maximum for the function to work. For minima, it would be necessary to set the ‘seed’ to a value higher or equal to the minimum (so this is not a seedless example!).

**_Multiplication (or Division)_**

When using **List.Accumulate** to perform calculations involving multiplication or division, the ‘seed’ is important. It can’t be zero because it will either render the product zero or invalidate the division. Allow me to illustrate with another list.

![](<Base64-Image-Removed>)

This time my blank query will look at the product of the items on my list.

![](<Base64-Image-Removed>)

This time, my function is

**\= List.Accumulate(Simple\_List3,1,(state,current)=>state\*current)**

which acts on my list as follows:

**Current State State\*current**

10 1 10

2 10 20

100 20 2000

In this case, ‘**seed**‘ is a factor in my calculation. If I change it to zero, then my result is zero, because the first value for the state will be zero.

![](<Base64-Image-Removed>)

If I change ‘**seed**‘ to 2, the first value of ‘**state**‘ will be 2, and the whole calculation will be multiplied by 2.

![](<Base64-Image-Removed>)

The division is similar:

![](<Base64-Image-Removed>)

where **List.Accumulate** acts on my list accordingly:

**Current State State/current**

10 1 0.1

2 0.1 0.05

100 0.05 0.0005

Clearly, the seed can’t be nought as my first step would result in an error caused by dividing by zero.

**_Concatenating_**

I will use my text list ‘**Simple\_List4**‘ for this, which was a list of tent equipment. I can concatenate all my items using **List.Accumulate**:

![](<Base64-Image-Removed>)

This has extracted all the items in my list and put them into a single string.

**\= List.Accumulate(Simple\_List4,” “, (state,current)=>state&current)**

I could add a delimiter to make it clearer. The delimiter would only be needed after the first item, so I would need to check if it was the first item, and if not, add my delimiter.

**\= List.Accumulate(Simple\_List4,” “, (state,current)=> if state = ” ” then state&current else state&” : “&current)**

The results are shown below:

![](<Base64-Image-Removed>)

**_Conditions on Records_**

The examples so far show how **List.Accumulate** works, but one area where it can be very useful, is when I have a list of records. I have an example below where my list is made up of records:

![](<Base64-Image-Removed>)

Each record has some item data, but I want to know the position of records that mention a ‘**Tent**‘. This would take several steps, as I can’t see the contents of the records in the list, but I can use **List.Accumulate**.

![](<Base64-Image-Removed>)

I haven’t tried to stop the comma delimiter appearing before the first record found as I want to keep the syntax as simple as it can be.

**\= List.Accumulate(List\_Records,””,(state,current)=>if Record.HasFields(current,”Tent”) then state&” , “&Text.From(List.PositionOf(List\_Records,current)) else state)**

This looks at each item on the list, and checks for the field ‘**Tent**‘. If it is found then the function returns the position number of the record (which starts at 0, not 1). As the function loops round each item, the delimiter is placed between each result.

**Current state new value for state**

Record (1) ” ” ,0

Record (2) ,0 ,0

Record (3) ,0 ,0,2

which tells me that records 1 and 3 have the field ‘**Tent**‘ in them.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found here. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-seeded-accommodating-accumulating/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-seeded-accommodating-accumulating/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-seeded-accommodating-accumulating/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-seeded-accommodating-accumulating/#0)

[](https://sumproduct.com/blog/power-query-seeded-accommodating-accumulating/#0 "close")

top