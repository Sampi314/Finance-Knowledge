# Power Query: Fabulously Fiddly Fill Down

**Source:** https://sumproduct.com/blog/power-query-fabulously-fiddly-fill-down/

---

[Home](https://sumproduct.com/)

\> Power Query: Fabulously Fiddly Fill Down

*   July 14, 2020

Power Query: Fabulously Fiddly Fill Down
========================================

Power Query: Fabulously Fiddly Fill Down
========================================

15 July 2020

_Welcome to our Power Query blog. This week, I again look at the fill down problem I have considered for the past two weeks this time using a column copy solution._

You know the drill. I have some data on tents supplied by my imaginary company:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-181-1.jpg)

I would like to get this into a more standard format, by filling down the tent and awning types. I begin by extracting my data to Power Query by using the ‘From Table’ option on the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-170-1.jpg)

I accept the defaults and tick the box to indicate that my table does indeed have headers.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-165-1.jpg)

I create a copy of the **Awning** column.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-145-1.jpg)

I fill down my copied column by selecting it and then right-clicking to choose ‘Fill’ and then ‘Down’.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-124-1.jpg)

Now, I may either use the value in **Awning – Copy** or **Awning** to create a new conditional column based on the value in **Tent**.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-105-1.jpg)

If the value in **Tent** is _null_, I am using the value in **Awning – Copy**, otherwise I am using the value in **Awning**. Once satisfied, I click ‘OK’ to create my **Awning Rename** column.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-91-1.jpg)

I can now remove **Awning – Copy** and remove **Awning**, so that I may use **Awning Rename** as my **Awning** column.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-72-1.jpg)

Finally, I select **Tent** and fill down, before moving **Awning** next to **Tent.**

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-58-1.jpg)

I now have my data in the format I require.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fabulously-fiddly-fill-down/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fabulously-fiddly-fill-down/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fabulously-fiddly-fill-down/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fabulously-fiddly-fill-down/#0)

[](https://sumproduct.com/blog/power-query-fabulously-fiddly-fill-down/#0 "close")

top