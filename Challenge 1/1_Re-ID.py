
"""
foobar:~/re-id vedron007$ cat readme.txt
Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme.

She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113".

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(0)
Output:
    23571

Input:
Solution.solution(3)
Output:
    71113

-- Python cases --
Input:
solution.solution(0)
Output:
    23571

Input:
solution.solution(3)
Output:
    71113

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

"""
"""
foobar:~/re-id vedron007$ verify solution.py
Verifying solution...
All test cases passed. Use submit solution.py to submit your solution
foobar:~/re-id vedron007$ submit solution.py
Are you sure you want to submit your solution?
[Y]es or [N]o: Y
Submitting solution...
You survived a week in Commander Lambda's organization, and you even managed to get yourself promoted. Hooray! Henchmen still don't have the kind of security access you'll need to take down Commander Lambda, though, so you'd better keep working. Chop chop!
Submission: SUCCESSFUL. Completed in: 28 mins, 24 secs.






                                           @\
                                  @@     @@\~@
                                 @%$@    % \~~@
                                @\\\\\%  %)))))~@
                                @~~\\~~@\\\\\\))@
                                 @\\\\\\@  \\\)@
                                @~\~~~ @ %\\@
                                @\~~\\\@  $$$@\
                               @@\\$\\% @\%   @
                              @  ~\)))))\\\\    $@
                              @\\\\))))@@@\\\    $@
                @@\\\\\\%\\\  \\%%\\\))))@  @)\\   $@
    \\$@\\     @\\\\\\~~~\\@@@     \\\))))@@@))\     @
 \@\$   $@\ @@\\\~~~~~~~ %%%      ))))))))))     ~ @
 @         $@\\\\\\\\~~~~~~~           )))))        @
 @$       @\\\\~~~~~~~~~~~~~~               $\@@
  @$   @@$@\\\\\\~~~~~~~~~          ~~\%%@@@\\
    @@@\\\\~~~~)~~~~~~~               ~$
        @\\\\\\\\))))~~~~~~              $$$
         @$))\\\\\\\\)~~~~~~  \    %%%  ~~~~$
          @%%%))))))~~~~~~    \$$    @ ~~$$@
           @%%%%%))))))))))        %   @@@@//
             @%%%%%%%%$$$$    \  @
                @@@@@@@@@@@@@\\\@
Level 1 complete
You are now on level 2
Challenges left to complete level: 2

Level 1: 100% [==========================================]
Level 2:   0% [..........................................]
Level 3:   0% [..........................................]
Level 4:   0% [..........................................]
Level 5:   0% [..........................................]

Type request to request a new challenge now, or come back later.
"""


def solution(x):
    s = ''
    for num in range(1, 25000):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            s += str(num)

    return s[x + 1:x + 6]


print(solution(3))
