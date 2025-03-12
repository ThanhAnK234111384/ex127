import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('../data/SampleData2.csv')

# (1) Print all data
def print_all_data():
    print(df)

# (2) Print all data but sort by Price ascending
def print_sorted_by_price():
    print(df.sort_values(by='Price', ascending=True))

# (3) Enter Symbol to search, if found, reduce Price by 1/2
def reduce_price_by_half():
    symbol = input("Enter Symbol to search: ")
    df.loc[df['Symbol'] == symbol, 'Price'] /= 2
    print(df)

# (4) Add USD column
df['USD'] = df['Price'] / 23
print(df)

# (5) Enter new data at the end
def add_new_data():
    try:
        symbol = input("Enter Symbol: ").strip()
        price = float(input("Enter Price: "))
        pe = float(input("Enter PE: "))
        group = input("Enter Group: ").strip()
        usd = price / 23
        new_row = pd.DataFrame({'Symbol': [symbol], 'Price': [price], 'PE': [pe], 'USD': [usd], 'Group': [group]})
        global df
        df = pd.concat([df, new_row], ignore_index=True)
        print(df)
    except ValueError:
        print("Invalid input! Please enter numeric values for Price and PE.")

def group_statistics():
    grouped = df.groupby('Group').agg({'Price': ['mean', 'sum', 'count']})
    return grouped

def delete_by_symbol():
    symbol = input("Enter Symbol to delete: ").strip()
    global df
    if symbol in df['Symbol'].values:
        df = df[df['Symbol'] != symbol]
        print(df)
    else:
        print("Symbol not found!")

# Test các chức năng
delete_by_symbol()