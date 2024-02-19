#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Name : Saaketh Potluri,Student Number : 100876538


# In[12]:


import time
import random

class Products:
    electronics = []
    
    def __init__(self, ID, Name, Price, Category):
        # Initializing product attributes
        self.ID = ID
        self.Name = Name
        self.Price = Price
        self.Category = Category

    def load_data():
        # Load product data from file and store data
        with open("product_data.txt", "r") as file:
            for line in file:
                ID, Name, Price, Category = line.strip().split(',')
                Products.electronics.append(Products(ID, Name, Price, Category))
        
        # Print read data as an array
        for product in Products.electronics:
            print(f"[ '{product.ID}', '{product.Name}', '{product.Price}', '{product.Category}' ]")
    

    def add_product(ID, Name, Price, Category):
        # Method for adding new products
        Products.electronics.append(Products(ID, Name, Price, Category))
        print("Product added Successfully")
    

    def update_product(ID, Name=None, Price=None, Category=None):
        # Method for updating products
        found = False 
        # Updating existing product details
        for product in Products.electronics:
            if product.ID == ID:  
                if Name:
                    product.Name = Name  
                if Price:
                    product.Price = Price  
                if Category:
                    product.Category = Category  
                print(f"Product {ID} updated successfully.")
                found = True  
                break  
        
        if not found:
            print(f"Product with ID {ID} not found.")
    

    def delete_product(ID):
        # Method for deleting products
        for i, product in enumerate(Products.electronics):
            if product.ID == ID:
                Products.electronics.pop(i)
                print(f"Product {ID} deleted successfully.")
                return
        print(f"Product with ID {ID} not found.")
    

    def search_product(search_term):
        # Method for searching products
        found = False
        for product in Products.electronics:
            if search_term.lower() in product.ID.lower() or search_term.lower() in product.Name.lower():
                found = True
                print(f"[ '{product.ID}', '{product.Name}', '{product.Price}', '{product.Category}' ]")
                break
        if not found:
            print("No products found.")
    
    
    def bubble_sort():
        # Bubble sort implementation to sort product data by price
        n = len(Products.electronics)
        for i in range(n):
            for j in range(0, n-i-1):
                if float(Products.electronics[j].Price) > float(Products.electronics[j+1].Price):
                    Products.electronics[j], Products.electronics[j+1] = Products.electronics[j+1], Products.electronics[j]
    
    
    def analyze_sorting_complexity():
        # Analyzing sorting complexity under different conditions
        start_time = time.perf_counter()
        Products.bubble_sort()
        sorted_time = time.perf_counter() - start_time
        print(f"Time taken to sort already sorted data: {sorted_time:.6f} seconds")
        
        random.shuffle(Products.electronics)
        
        start_shuffle_sort_time = time.perf_counter()
        Products.bubble_sort()
        shuffled_sort_time = time.perf_counter() - start_shuffle_sort_time
        print(f"Time taken to sort shuffled data: {shuffled_sort_time:.6f} seconds")
        
        Products.electronics.reverse()
        start_reverse_sort_time = time.perf_counter()
        Products.bubble_sort()
        reverse_sort_time = time.perf_counter() - start_reverse_sort_time
        print(f"Time taken to sort reverse ordered data: {reverse_sort_time:.6f} seconds")



while True:
    print("\nChoose the following options:\n 1. Display List\n 2. Add New Product\n 3. Update Product\n 4. Delete Product\n 5. Search Product\n 6. Analyze Sorting Complexity\n 7. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        Products.load_data()     
    elif choice == '2':
        ID = input("Enter Product ID: ")
        Name = input("Enter Product Name: ")
        Price = input("Enter Product Price: ")
        Category = input("Enter Product Category: ")
        Products.add_product(ID, Name, Price, Category)     
    elif choice == '3':
        ID = input("Enter Product ID to update: ")
        Name = input("Enter new Product Name (leave blank if no change): ")
        Price = input("Enter new Product Price (leave blank if no change): ")
        Category = input("Enter new Product Category (leave blank if no change): ")
        Products.update_product(ID, Name if Name != '' else None, Price if Price != '' else None, Category if Category != '' else None)
    elif choice == '4':
        ID = input("Enter Product ID to delete: ")
        Products.delete_product(ID)
    elif choice == '5':  
        search_term = input("Enter search term (ID or Name): ")
        Products.search_product(search_term)
    elif choice == '6':
        Products.analyze_sorting_complexity()
    elif choice == '7':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

