# Automated Swipe2Care Donations

NOTE: this is currently a work in progress (including the README). The form filling is fully automatic with the exception of two-factor authentication, and I hope to find a workaround for that in the near future.

## Motivation

Northeastern University's Dining Service provider, commonly known as NUDining, runs a program called [Swipe2Care](https://www.nudining.com/public/intentionally-reducing-waste), described as follows: 

> "Swipe2Care is a combined initiative from Student Government Association, Dining Services, and Student Affairs to provide a platform for students to donate their meal swipes to other students. The program is designed to allow students to seamlessly contribute meals from their meal plan while providing a confidential and efficient method for students–who may be having difficulty–to request their next meal."

While it's not publicly known how many students take advantage of this program, NUDining made it clear in a recent email to the entire Boston-based student body that there is currently a high demand for donated meal swipes. 

At the end of every week, hundreds –if not thousands– of unused, **already paid for** meal swipes expire, generating pure profit for NUDining. This can be attributed to the fact that NUDining places the responsibility of swipe donation on the student, meaning that few people consistently remember to donate their unused swipes. The obvious solution would be to automatically donate these unused meals to the Swipe2Care meal bank, which NUDining has not done. In fact, when I was looking through the website's HTML, I found that the meal donation website already includes functionality for automatic meal donations, but it's intentionally disabled. 

Fun fact: when u/uncountablyInfinit [posted](https://www.reddit.com/r/NEU/comments/10iw7kx/fun_fact_the_swipe2care_page_has_code_for/) my finding on the r/NEU subreddit, that functionality was quickly removed from public view. You can see the before and after for yourself in the `meal_donation_form` directory.

## Solution

As neat as automation is, this program's primary focus isn't to save time. It takes no more than a minute to submit a meal swipe donation. The purpose is more about sending a message to NUDining, the Student Government Association, and Student Affairs, who are eager to claim responsibility for what has the *potential* to be a beneficial program. 




