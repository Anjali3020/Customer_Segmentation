import pandas as pd

# Read customer data
df = pd.read_csv("Customer.csv")

# Function for segmentation
def segment_customer(amount):
    if amount >= 20000:
        return "Premium"
    elif amount >= 15000:
        return "Gold"
    elif amount >= 8000:
        return "Silver"
    else:
        return "Regular"
    
# Add segment column
df["CustomerSegment"] = df["PurchaseAmount"].apply(segment_customer)
print("========== CUSTOMER SEGMENTATION REPORT ==========\n")
print(df)

# Count customers in each segment
print("\n========== SEGMENT SUMMARY ==========\n")
print(df["CustomerSegment"].value_counts())

# Calculate average purchase amount
print("\n========== AVERAGE PURCHASE ==========\n")
print("Average Purchase Amount:", df["PurchaseAmount"].mean())

# Save result to new CSV file
df.to_csv("segmented_customers.csv", index=False)
print("\nSegmented customer data saved to segmented_customers.csv")