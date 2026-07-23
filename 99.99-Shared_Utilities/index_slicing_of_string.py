def heading(title):
    print(f"\n{'=' * 40}\n{title}:-\n{'-' * 40}")

def note(message):
    print(f"(Note:- {message}.)\n{'-' * 40}")


text = "AnimeshSanghi"

# -----------------------------------------------------------------------------------------------------
# Without using step
# -----------------------------------------------------------------------------------------------------
heading("Basic Slicing")
print(text[0:7])      # Output: Animesh (characters from index 0 to 6)
print(text[7:])       # Output: Sanghi (from index 7 to end)
print(text[:7])       # Output: Animesh (from start to index 6)

heading("Negative Slicing")
print(text[-6:-1])    # Output: Sangh (starts at 'S', stops before the last character 'i')
print(text[:-1])      # Output: AnimeshSangh (everything except the last character)

heading("Slicing by Mixing Positive and Negative Indices")
print(text[2:-2])     # Output: imeshSang (Starts at index 2, stops 2 characters before the end)
print(text[-10:8])    # Output: meshS (Starts at 10th character from the end, stops at index 7)


# -----------------------------------------------------------------------------------------------------
# Using step
# -----------------------------------------------------------------------------------------------------
heading("Basic Slicing with basic Step")
print(text[0:10:2])   # Output: Aieha (Every 2nd character from index 0 to 9)
print(text[::3])      # Output: Amhni (Every 3rd character from the entire string)

heading("Negative Slicing with positive Step")
print(text[-9:-1:2])  # Output: ehag (Every 2nd character from index -9 up to -2)

heading("Positive Slicing with Negative Step")
note("To step backward, the starting index must be greater than the stopping index")
print(text[::-1])     # Output: ihgnaShseminA (Reverses the string completely!)
print(text[::-2])     # Output: igaheiA (Every 2nd character, going backwards through the whole string)
print(text[12:0:-1])  # Output: ihgnaShsemin (Reverses the string, excluding the first character at index 0)

heading("Negative Slicing with Negative Step")
print(text[-1:-9:-1]) # Output: ihgnaShs (Steps backward from the end down to index -8)


# -----------------------------------------------------------------------------------------------------
# Handling errors
# -----------------------------------------------------------------------------------------------------
heading("Out of Bounds Slicing")
note("Unlike direct indexing (text[20]), slicing handles out-of-bounds indices gracefully")
print(text[10:100])   # Output: ghi (Starts at index 10 and just grabs everything until the actual end)
print(text[-50:5])    # Output: Anime (Treats -50 as the very beginning of the string)

heading("Empty Slices")
note("If your step direction contradicts your start and stop indices, Python simply returns an empty string")
print(text[5:2])      # Output: "" (Starts at 5, wants to go to 2, but step is implicitly +1. Impossible!)
print(text[2:5:-1])   # Output: "" (Starts at 2, wants to go to 5, but step is -1. Impossible!)
print(repr(text[5:2]))# Using repr() just to visually show the empty string output: ''