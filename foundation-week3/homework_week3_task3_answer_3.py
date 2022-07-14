song = "You could never know what it's like\n" \
       "Your blood like winter freezes just like ice\n" \
       "And there's a cold lonely light that shines from you\n" \
       "You'll wind up like the wreck you hide behind that mask you use\n\n" \
       "And did you think this fool could never win?\n" \
       "Well look at me, I'm coming back again\n" \
       "I got a taste of love in a simple way\n" \
       "And if you need to know while I'm still standing, you just fade away\n\n" \
       "Don't you know I'm still standing better than I ever did\n" \
       "Looking like a true survivor, feeling like a little kid\n" \
       "I'm still standing after all this time\n" \
       "Picking up the pieces of my life without you on my mind\n\n" \
       "I'm still standing (Yeah, yeah, yeah)\n" \
       "I'm still standing (Yeah, yeah, yeah)"

with open('./song.txt', 'w') as song_file:
    song_file.write(song)

# READ ONLY LINES CONTAINING "STILL" - METHOD #1 - List Comprehension

with open('./song.txt', 'r') as song_file:
    keyword = 'still'
    matching_lines = [line for line in open('./song.txt').readlines() if keyword in line]
    print(matching_lines)

# # READ ONLY LINES CONTAINING "STILL" - METHOD #2 - For Loop with If Condition
#
# matching_lines = []
# with open('./song.txt', 'r') as song_file:
#     for line in song_file:
#         if 'still' in line:
#             matching_lines.append(line)
# print(matching_lines)
