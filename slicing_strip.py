text = "X-DSPAM-Confidence:    0.8475"
index = text.find(' ')
# print(index)
text = (text[index:]).strip()
print(float(text))