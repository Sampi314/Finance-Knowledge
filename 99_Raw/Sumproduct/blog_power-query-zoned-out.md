# Power Query: Zoned Out

**Source:** https://sumproduct.com/blog/power-query-zoned-out/

---

[Home](https://sumproduct.com/)

\> Power Query: Zoned Out

*   February 12, 2019

Power Query: Zoned Out
======================

Power Query: Zoned Out
======================

13 February 2019

_Welcome to our Power Query blog. Last week’s blog looked at solving a particular problem by using DateTime.AddZone(). This week, I look at some of the M functionality for dealing with time zones._

There are a number of **DateTimeZone() M** functions which assist me when dealing with date / time data that has come from a variety of sources. I will look in detail at some of them.

**_#datetimezone_**

I use this function to demonstrate many of the other **DateTimeZone()** functions that follow, since it constructs a **datetimezone** from parameters passed to it.

**#datetimezone(year** as number, **month** as number, **day** as number, **hour** as number, **minute** as number, **second** as number, **offsetHours** as number, **offsetMinutes** as number**)** as any

The **offsetHours** and **offsetMinutes** parameters are the **timezone** hour and minute values respectively.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-487.jpg)

**_DateTimeZone.FixedLocalNow_**

This returns a **datetimezone** value set to the current date, time and **timezone** offset on the system. This value is fixed and will not change with successive calls, unlike **DateTime.LocalNow**, which may return different values over the course of execution of an expression.

**DateTimeZone.FixedLocalNow()** as **datetimezone**

![](<Base64-Image-Removed>)

**_DateTimeZone.FixedUtcNow_**

This returns the current date and time in “UTC” (Coordinated Universal Time, the GMT timezone). This value is fixed and will not change with successive calls.

**DateTimeZone.FixedUtcNow()** as **datetimezone**

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-474.jpg)

**_DateTimeZone.From_**

This returns a **datetimezone** value from a value.

**DateTimeZone.From(value** as any, optional **culture** as nullable text**)** as nullable **datetimezone**

The **value** parameter is required, and although it says datatype can be ‘any’, only the following datatypes are accepted (others will result in an error):

*   **text  
    **This returns a **datetimezone** value from a text **value**. For more details, see **DateTimeZone.FromText**_(below)_

*   **date  
    **A **datetimezone** with **value** as the date component, 12:0:00 AM as the time component and the offset corresponding the local time zone

*   **datetime  
    **A **datetimezone** with **value** as the datetime and the offset corresponding the local time zone

*   **time  
    **A **datetimezone** with the date equivalent of the OLE Automation Date of 0 as the date component, **value** as the time component and the offset corresponding the local time zone

*   **number  
    **A **datetimezone** with the datetime equivalent the OLE Automation Date expressed by **value** and the offset corresponding the local time zone

*   (**datetimezone** is also accepted, but it will return exactly the same value!).

It is also possible to specify an optional **culture** parameter. This is defined by Microsoft as

“…a text value corresponding to the culture values supported on your version of Windows, such as ‘en-US’…”. If the culture is not specified, the current user **culture** is used.

![](<Base64-Image-Removed>)

**_  
DateTimeZone.FromFileTime_**

This returns a **datetimezone** from a number value.

**DateTimeZone.FromFileTime(filetime** as nullable number**)** as nullable **datetimezone**

This function is more specialist – **filetime** has a specific definition:

“A Windows file time value that represents the number of 100-nanoseconds intervals that have elapsed since 12:00 midnight, January 1, 1601 A.D. (C.E.) Coordinated Universal Time (UTC)”. How did you ever live without knowing that?

![](<Base64-Image-Removed>)

**_  
DateTimeZone.FromText_**

This returns a **datetimezone** value from a set of date formats and **culture** value.

**DateTimeZone.FromText(datetimezone** as nullable text, optional **culture** as nullable text**)** as nullable **datetimezone**

A full list of acceptable **datetimezone** formats can be found in Microsoft’s help pages. The **culture** was previously defined for **DateTimeZoneFrom**.

![](<Base64-Image-Removed>)

**_  
DateTimeZone.LocalNow_**

This returns a **datetimezone** value set to the current system date and time.

**DateTimeZone.LocalNow()** as **datetimezone**

This will provide the current local date time and zone.

![](<Base64-Image-Removed>)

**_  
DateTimeZone.RemoveZone_**

This returns a **datetime** value with the zone information removed from the input **datetimezone** value.

**DateTimeZone.RemoveZone(datetimezone** as **datetimezone)** as nullable **datetime**

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

**_  
DateTimeZone.SwitchZone_**

Changes the **timezone** information for the input **datetimezone**.

**DateTimeZone(datetimezone** as **datetimezone**, **timezonehours** as number, optional **timezoneminutes** as nullablenumber**)** as nullable **datetimezone**

This adjusts the **timezone** information on the input **datetimezone** to **timezonehours** and **timezoneminutes**, where provided. This will also affect the time (and possibly the date), as shown in the example screens that follow:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

**_  
DateTimeZone.ToLocal_**

This returns a **datetimezone** value from the local time zone.

**DateTimeZone.ToLocal(datetimezone** as **datetimezone)** as nullable **datetimezone**  

This function also adjusts the time (and possibly the date) as the following examples show.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

**_  
DateTimeZone.ToRecord_**

This returns a record containing parts of a **datetimezone** value.

**DateTimeZone.ToRecord(datetimezone** as **datetimezone)** as record

This converts a **datetimezone** to a record – if any parts are missing from **datetimezone**, then they will be missing from the record.

![](<Base64-Image-Removed>)

**_  
DateTimeZone.ToText_**

This returns a text value from a **datetimezone** value.

**DateTimeZone.ToText(datetimezone** as nullable **datetimezone**, optional **format** as nullable text, optional **culture** as nullable text**)** as nullable text

The text output can be controlled by specifying a **format** (_e.g._ “yyyy/MM/ddThh:mm:sszzz”) and / or a **culture** (_e.g._ “US”).

![](<Base64-Image-Removed>)

**_  
DateTimeZone.ToUtc_**

This returns a **datetimezone** value to the UTC time zone.

**DateTimeZone.ToUtc(datetimezone** as **datetimezone)** as nullable **datetimezone**

As mentioned earlier, the Coordinated Universal Time is defined as ‘the primary time standard by which the world regulates clocks and time’. This will affect the time (and possibly the date) as shown in the following example:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

**_  
DateTimeZone.UtcNow_**

This returns a **datetimezone** value set to the current system date and time in the UTC timezone.

**DateTimeZone.UtcNow** as **datetimezone**

This function must receive no parameters; it gives the current **datetimezone** with reference to UTC.

![](<Base64-Image-Removed>)

**_  
DateTimeZone.ZoneHours_**

This returns a time zone hour value from a **datetimezone** value.

**DateTimeZone.ZoneHours(datetimezone** as **datetimezone)** as nullable number

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

**_  
DateTimeZone.ZoneMinutes_**

This returns a **Timezone** minute value from a **datetimezone** value.

**DateTimeZone.ZoneMinutes(datetimezone** as **datetimezone)** as nullable number.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-zoned-out/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-zoned-out/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-zoned-out/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-zoned-out/#0)

[](https://sumproduct.com/blog/power-query-zoned-out/#0 "close")

top