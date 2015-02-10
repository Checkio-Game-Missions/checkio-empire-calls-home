The bill is represented as an array with information about the calls.
Write a function to calculate the cost of calls.

Each call is represented as a string with date, time and duration of the call in seconds in the follow format:

`"YYYY-MM-DD hh:mm:ss duration"`

The date and time in this information are the start of the call.

Space-Time Communications Co. has several rules on how to calculate the cost of calls:
- First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
- After 100 minutes in one day, each minute costs 2 coins per minute;
- All calls are rounded up to the nearest minute. For example 59 sec &asymp; 1 min, 61 sec &asymp; 2 min;
- Calls count on the day when they began. 
  For example if a call was started 2014-01-01 23:59:59, then it counted to 2014-01-01;

For example:

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
