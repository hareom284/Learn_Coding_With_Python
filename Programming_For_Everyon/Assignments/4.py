text = "X-DSPAM-Confidence:    0.8475"
start = text.find('0')
end   = text[start:]
end = float(end)
print(end)