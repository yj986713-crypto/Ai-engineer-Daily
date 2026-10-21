import pandas as pd

df = pd.DataFrame({
    'Product': ['Laptop', 'Phone', 'Tablet'],
    'Price': [1200, 800, 500],
    'Date': ['2024-01-01', '24-01-15', '24-03-28']
})

# Convert Date column
df['Date'] = pd.to_datetime(
    df['Date'],
    format='mixed',
    errors='coerce'
)

print(df)
print(df.info())
