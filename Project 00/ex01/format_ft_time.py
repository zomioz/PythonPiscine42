import time as time

timestamp = time.time()

#here f"{} is from "Format String Syntax", f"" is formating the string from timestamp, and :, place a comma after 1000, and :e write in scientific notation
#see https://www.w3schools.com/python/ref_string_format.asp
print("Seconds since January 1, 1970:", f"{timestamp:,}", "or", f"{timestamp:e}", "in scientific notation")

#convert timestamp to classic date format with month name DD YYYY using strftime() and localtime(), %b for short month
date_formatted = time.strftime("%b %d %Y", time.localtime(timestamp))
print(date_formatted)

