## Blind Auction

Click "Open Preview" above to see this file rendered with the markdown.

# Instructions

The objective of this program is to simulate a blind auction process. The program collects names and bid amounts from participants. Each participant is prompted to enter their name followed by their bid amount. 

```
Welcome to the secret auction program. 
What is your name?: Angela
```
```
What's your bid?: $123
```
```
Are there any other bidders? Type 'yes' or 'no'.
yes

```
If additional bidders wish to participate, the interface (e.g., the screen or console) should be cleared for the next person to enter their bid confidentially. Once all bids are collected, and no further bidders are left, the program announces the name of the highest bidder along with their bid amount.

```
The winner is Elon with a bid of $55000000000
```

To accomplish this, employ Python's dictionaries for storing bidder information and loops for iterating through the bidding process until all bids are collected.

# Note on Console Clearing

When not using Replit and opting for other IDEs (like VSCode, PyCharm, etc.), the `clear()` function for clearing the console output might not work as expected. This function is readily available in Replit through the "replit" module, simplifying the process without requiring additional setup.

For those using different environments, adapting the clear screen functionality might involve writing a custom `clear()` function or configuring your IDE to mimic this behavior. Detailed guidance on handling such scenarios, including module importation and custom function creation, will be discussed further on Day 15.

For quick solutions or additional context, consider referring to this discussion:
[Udemy Q&A Answer](https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/16084076)

# Solution Preview

Access a completed version of the blind auction project for reference or inspiration through the following link: 
[Blind Auction - Completed Project on Replit](https://replit.com/@YousufKh/blind-auctionbidderprogram#main.py)

This revised README maintains the original content while enhancing its relevance and clarity, providing additional context where necessary, and offering guidance for a broader range of development environments.