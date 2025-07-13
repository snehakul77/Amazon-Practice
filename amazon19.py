#Write a function to transform a string

#Remove special characters and lowercase all letters:

def normalize_string(s):
    return ''.join(c.lower() for c in s if c.isalnum())

#print(normalize_string("SnEha$!!"))

#Function to validate it

def test_normalize_string():
    input_string = "SnEha$!!"
    output_string = normalize_string(input_string)
    expected_output_string = "sneha"
    assert output_string == expected_output_string, f"Expected: {expected_output_string}, got: {output_string}"
    print("Test passed")

test_normalize_string()