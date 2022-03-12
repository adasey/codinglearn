t = "aaaaaa" \
    + "bbbbbb"

print(t)

# not in

if 'a' in t:
    print("True")

if 'c' not in t:
    print("True")

is_ok = False

if not is_ok:
    print("False")

# False, 0, 0.0, '', [], (), {}, set{}

is_empty = '' 

if is_empty:
    print("ok")
else:
    print("no")

#None = Null

is_None = None

if is_None is None:
    print("None")

print(1 == True)
print(1 is True)