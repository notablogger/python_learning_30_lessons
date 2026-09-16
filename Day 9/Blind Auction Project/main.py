# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art

print(art.logo)

bid_dic={}

cont="y"
while cont=="y":
    name=input("what is your name? ")
    bid_dic[name]=int(input(f"what is your bid {name}? "))
    cont=input("is there any other bidder (y/n)? ")
    print("\n"*10)

highest_bidder=""
highest_bid=0
for name in bid_dic:
    if bid_dic[name]>highest_bid:
        highest_bid=bid_dic[name]
        highest_bidder=name

print(f"Higest bid was placed by {highest_bidder} with value {bid_dic[highest_bidder]}")