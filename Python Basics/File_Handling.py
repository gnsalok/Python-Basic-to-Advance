
print(''' Working with the Files
-----------------------------------------------------''')


#writing inside the file

#text='This is a sample text\nNew Line'
#saveFile=open('F:\\SampleText.txt','w')

#saveFile.write(text)
#print('Writing inside the file successfully')

#saveFile.close()


#Append the item

textAppend='My name is John and whats about you//\nNew Line'
AppendFile=open('F:\\SampleText.txt','a')
AppendFile.write(textAppend);
print("Appending inside the file completed!!")
AppendFile.close();

