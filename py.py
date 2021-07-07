count = 0;  
num = 0;   
#Opens a file in read mode  
file = open("py.py", "r")  
      
#Gets each line till end of file is reached  
for line in file: 

    #Splits each line into words  
    words = line.split(" ");  
    num =line.split("line");
    #Counts each word  
    count = count + len(words);  
    count = num + len(num);
print("Number of number present in given file: " + str(count));      
print("Number of words present in given file: " + str(count));  
file.close();  