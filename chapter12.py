# Read than write new info File and close
readable_file= open('text.txt','r');
print(readable_file.read())

writeable_file=open('text.txt','w')
writeable_file.write("I wrote this new text22")
if writeable_file.readable():
    print(writeable_file.read())
else:
    print("After writing you forgot to close")

writeable_file.close()