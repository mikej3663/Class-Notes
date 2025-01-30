## Important Notes and Information from the Textbook
 
Michael Jamesley


Three key takeaways from chapter 2:

1. Automate everything that can be automated
        - It is important to not *raw code* everything, make sure the code works for different data sets
2. ABCD = Always Be Checking your Data
        - When coding, constantly **use print statements** to check if your data makes sense
3. Store cleaned data in tables with unique and representative names
        - Data should be cleaned under a name that makes sense for the data


Here's an example of a table:
    random_table = [[23, 87, 56, 12, 45],[78, 34, 92, 11, 67],[19, 43, 81, 72, 99],[53, 27, 88, 60, 42],[76, 38, 90, 13, 29]]

Here's an example of a list: 
    yearly_profit = [10500, 12000, 9800, 13400, 15750, 11000, 14200, 9900, 12500, 13600]

In this chapter, we looked at "for loops". Here is an example of a for loop that counts the years the yearly profit was greater than 10,500
        count_greater_than_10500 = 0
        
        for profit in yearly_profit:
            if profit > 10,500:
                count_greater_than_10500 = count_greater_than_10500 + 1
            else:
                continue

        print(count_greater_than_10500)

Success!
![Happy Dance]https://vmscrub.com/wp-content/uploads/2017/05/happy-dance-animated-gif-image-1-2.gif


Key links:
        - [The main website](https://ledatascifi.github.io)
        - [Upcoming tasks and schedule](https://ledatascifi.github.io/ledatascifi-2025/content/about/schedule.html)
        - [Lecture slides](https://donbowen.github.io/slides/)
        - [Announcements, discussions, and help](https://github.com/LeDataSciFi/ledatascifi-2025/discussions)
        - [Tips](https://ledatascifi.github.io/ledatascifi-2025/content/about/tips.html)
        - [Help](https://ledatascifi.github.io/ledatascifi-2025/content/about/help.html)
        - [The LDSF org (repos)](https://github.com/orgs/LeDataSciFi)
