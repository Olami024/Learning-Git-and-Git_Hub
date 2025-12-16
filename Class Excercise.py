#Write code using find() and string slicing to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475"

# Find the colon
pos = text.find(":")

# Extract the number part using slicing
number_part = text[pos + 1:].strip()

# Convert to float
last_number = float(number_part)

# Print ONLY the final result
print(last_number)
