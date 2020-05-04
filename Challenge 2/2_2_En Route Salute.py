def answer1(s):
    l = []
    for i in s:
        l.append(i)

    if len(l) == 0:
        print(0)
        return
    while l[0] == "<":
        l = l[1:]
    while l[-1] == ">":
        l = l[:-1]

    count = 0
    for i in range(len(l)):
        if l[i] == ">":
            for j in range(i, len(l)):
                if l[j] == "<":
                    count += 1
        if l[i] == "<":
            for j in range(i, -1, -1):
                if l[j] == ">":
                    count += 1
    return count


def answer2(s):
    count = 0
    for i, c in enumerate(s):
        if c == ">":
            count += 2 * s.count("<", i)
    return count


def solution(s):
    return answer1(s)


print(solution("<<>><"))
"""
foobar:~/ vedron007$ request
Requesting challenge...
The latest gossip in the henchman breakroom is that "LAMBCHOP" stands for "Lambda's Anti-Matter Biofuel Collision Hadron Oxidating Potentiator". You're pretty sure it runs on diesel, not biofuel, but you can at least give the commander credit for trying.
New challenge "En Route Salute" added to your home folder.
Time to solve: 72 hours.

foobar:~/ vedron007$ ls
en-route-salute
journal.txt
start_here.txt
foobar:~/ vedron007$ cd en-route-salute
foobar:~/en-route-salute vedron007$ ls
Solution.java
constraints.txt
readme.txt
solution.py
foobar:~/en-route-salute vedron007$ cat readme.txt
En Route Salute
===============

Commander Lambda loves efficiency and hates anything that wastes time. She's a busy lamb, after all! She generously rewards henchmen who identify sources of inefficiency and come up with ways to remove them. You've spotted one such source, and you think solving it will help you build the reputation you need to get promoted.

Every time the Commander's employees pass each other in the hall, each of them must stop and salute each other - one at a time - before resuming their path. A salute is five seconds long, so each exchange of salutes takes a full ten seconds (Commander Lambda's salute is a bit, er, involved). You think that by removing the salute requirement, you could save several collective hours of employee time per day. But first, you need to show her how bad the problem really is.

Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function solution(s) which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(">----<")
Output:
    2

Input:
solution.solution("<<>><")
Output:
    4

-- Java cases --
Input:
Solution.solution("<<>><")
Output:
    4

Input:
Solution.solution(">----<")
Output:
    2

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

"""

"""
foobar:~/en-route-salute vedron007$ verify solution.py
Verifying solution...
All test cases passed. Use submit solution.py to submit your solution
foobar:~/en-route-salute vedron007$ submit solution.py
Are you sure you want to submit your solution?
[Y]es or [N]o: Y
Submitting solution...
Awesome! Commander Lambda was so impressed by your efforts that she's made you her personal assistant. You'll be helping her directly with her work, which means you'll have access to all of her files-including the ones on the LAMBCHOP doomsday device. This is the chance you've been waiting for. Can you use your new access to finally topple Commander Lambda's evil empire?
Submission: SUCCESSFUL. Completed in: 29 mins, 13 secs.

Level 2 complete
You are now on level 3
Challenges left to complete level: 3

Level 1: 100% [==========================================]
Level 2: 100% [==========================================]
Level 3:   0% [..........................................]
Level 4:   0% [..........................................]
Level 5:   0% [..........................................]

To invite a friend to try a challenge, send the link below. This is a single-use code, so choose wisely.
"""
