write_text = "Bitch I'm stylish\n"
append_text = "Black top big t-shirt Billie Eilish\n"

# this creates a new song.txt file and writes content from write_text in it
with open("06. Writing File\\song.txt","w") as file:
    file.write(write_text)

# this appends content form append_text in the already created song.txt
with open("06. Writing File\\song.txt","a") as file:
    file.write(append_text)