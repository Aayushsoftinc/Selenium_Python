try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("Some how I reached this block because there is failure in try block")


try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
# Python error message
except Exception as e:
    print(e)

# finally keyword

finally:
    print("cleaning up resources")