import pandas as pd

file = "articles_data.csv"
df = pd.read_csv(file)
# สร้างคอลัมน์ใหม่ "Digit1" และ "Digit2" โดยแยกตัวเลขในคอลัมน์ "Number"
df["Digit1"] = df["Number"].astype(str).str[0]  # เลขแรก
df["Digit2"] = df["Number"].astype(str).str[1]  # เลขที่สอง
print(df[["Number", "Digit1", "Digit2"]])

output_file = "articles_data_with_digits.csv"
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"Data with digits has been written to {output_file}")