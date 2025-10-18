#Simulate a page loading check using a while loop.
#If page_loaded becomes True within 5 seconds, print success; else timeout.
#Hint: Use a counter (like wait_time) and break condition.
wait_time = 1
while wait_time <= 5:
    is_page_loaded = str(input("Is the page loaded? Y/N: ")).strip().upper()
    if is_page_loaded == 'Y':
        print(f"Page loaded too fast within {wait_time} seconds")
        break
    wait_time += 1
else:
    print("Page loaded too slow")