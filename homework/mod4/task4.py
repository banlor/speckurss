def make_palindrome(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1

    odd_count = 0
    odd_char = ""
    for ch in freq:
        if freq[ch] % 2 != 0:
            odd_count = odd_count + 1
            odd_char = ch

    if odd_count > 1:
        print("Нельзя составить палиндром")
        return

    left = ""
    for ch in freq:
        left = left + ch * (freq[ch] // 2)

    if odd_char != "":
        result = left + odd_char + left[::-1]
    else:
        result = left + left[::-1]

    print(result)

s = input()
make_palindrome(s)
