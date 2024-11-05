# Bingo card name
bingo_name = "Bingo"

# do we have a freespace
free_space_enabled = True

# Free Space Text
free_space_text = "Free Space"

# Output file name, no extension, automatically sticks a number on the end
# WILL REPLACE EXISTING FILES
output_file_name = "bingo"

# Grid Size: 3x3, 5x5 or 7x7
grid_size = "5x5"

# Link to background image, url goes in the single quotes
background_image_link = "background-image: url('')"
# css for if background repeats
background_repeat="background-repeat: repeat;"

# height and width of squares
width=100

# clicked square colour
clickedColour = "yellow"
# any css accepted colour i.e.
# "white", "black"
# "rgb(255,255,255)"
# "#ffffff"

# text colour
textColour = "white"

# link to audio file (with extension) for when a space is clicked
audioClicked = ""

# link to audio file (with extension) for when a its a BINGO!
audioComplete = ""

# type of file for BOTH of the above
# can be "wav", "mp3", "ogg" or any other allowed html values for audio tags
audioType = ""

# Text that appears on the card, 25 needed for 5x5, 49 for 7x7
# Use "<br>" for new line
# Use "<s>" and "</s>" to strikethrough text
# Use "<strong>" and "</strong>" to bold text
# Use "<em>" and "</em>" to make text italic
# Use "<sup>" and "</sup>" to make text superscript
# Use "<sub>" and "</sub>" to make text subscript
# ANY HTML allowed, Inline styling supported.
bingo_card = [
    "Card 1 text",
    "Card 2 text",
    "Card 3 text",
    "And so on text",
]



# Don't touch
from bingo import bingo
bingo(
    bingo_card,
    bingo_name,
    free_space_text,
    background_image_link,
    grid_size,
    output_file_name,
    width,
    clickedColour,
    audioClicked,
    audioComplete,
    audioType,
    background_repeat,
    textColour,
    free_space_enabled
)
