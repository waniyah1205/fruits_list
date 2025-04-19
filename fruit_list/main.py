def main():
    # Create a list called `fruit_list` that contains the following fruits:
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    print("Initial length of the list:", len(fruit_list))

    # Add 'mango' at the end of the list.
    fruit_list.append('mango')

    # Print the updated list.
    print("Updated list after adding mango:")
    for fruit in fruit_list:
        print("-", fruit)

    # BONUS: Sort the list alphabetically
    fruit_list.sort()
    print("\nSorted list (alphabetically):")
    print(fruit_list)

    # BONUS: Insert 'kiwi' at the 2nd position (index 1)
    fruit_list.insert(1, 'kiwi')
    print("\nList after inserting 'kiwi' at index 1:")
    print(fruit_list)

    # BONUS: Remove 'banana' from the list
    if 'banana' in fruit_list:
        fruit_list.remove('banana')
        print("\nList after removing 'banana':")
        print(fruit_list)
    else:
        print("\nBanana not found in the list.")

    # BONUS: Reverse the list
    fruit_list.reverse()
    print("\nReversed list:")
    print(fruit_list)

    # BONUS: Find the index of 'orange'
    if 'orange' in fruit_list:
        orange_index = fruit_list.index('orange')
        print("\nIndex of 'orange':", orange_index)
    else:
        print("\nOrange is not in the list.")

if __name__ == '__main__':
    main()
