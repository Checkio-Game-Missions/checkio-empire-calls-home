The bill is represented as an array with information about the calls that our accountant has made.
Write a function to calculate the cost of these calls.

Each call is represented as a string with the date, time and duration of the call in seconds in the follow format:

`"YYYY-MM-DD hh:mm:ss duration"`

The date and time in this information describes the start of the call.

Space-Time Communications Co. has several rules on how it calculates the cost of calls made on their network:
- First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
- After the first 100 minutes in one day, each minute costs 2 coins per minute;
- All calls are rounded up to the nearest minute. For example 59 sec &asymp; 1 min, 61 sec &asymp; 2 min;
- Calls are billed based on the day when they began
So if a call was started at 2014-01-01 23:59:59, then it counts as having started on 2014-01-01.



Here's an example communications bill:

```
2014-01-01 01:12:13 181
2014-01-02 20:11:10 600
2014-01-03 01:12:13 6009
2014-01-03 12:13:55 200
```

- First day -- 181s≈4m -- 4 coins;
- Second day -- 600s=10m -- 10 coins;
- Third day -- 6009s≈101m + 200s&asymp;4m -- 100 + 5 * 2 = 110 coins;
- Total -- 124 coins.
