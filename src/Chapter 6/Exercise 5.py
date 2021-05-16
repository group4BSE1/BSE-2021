string = 'X-DSPAM-Confidence: 0.8475'
#       Find_the colon_char
colon_position = string.find(':')
number = string[colon_position + 1:]
#       Conversion to floating_point_no.
floating_no = float(number)
print(floating_no)
