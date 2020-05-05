# while loop are used to check the condition and will run until the condition becomes false

it = 4
while it>1:
    print(it)
    it = it-1
print("while loop execution is done")

print("*********** while..if *********************")
# Stop 3 from printing
it = 4
while it>1:
    if it != 3:
        print(it)
    it = it-1
print("while loop execution is done")

print("*********** break *********************")
# Stop 3 from printing
it = 10
while it>1:
    if it == 3:
        break
    print(it)
    it = it-1
print("while loop execution is done")

print("*********** continue *********************")
# continue is used to skip current iteration and move to the next iteration
it = 10
while it>1:
    if it == 9:
        it = it-1
        continue
    if it == 3:
        break
    print(it)
    it = it-1
print("while loop execution is done")