"""
Reading through text files to extract information is a common computing task.
You should write a program that reads through a file that contains email addresses.
Your program should find the sender addresses of the emails and write all the sender addresses to another file.
An example file with emails has been added to the exercise.
The program should allow the user to enter the names of both files, both the program to read from and the one to write to.
An algorithm for doing this is as follows:

a. Ask the user for the name of the file with the emails and the file to be sent to the sender
b. Open the file with emails for reading
c. Open a new file for writing
d. Review the file with emails line by line
i. Use the strip() string method to remove spaces from the beginning and end of the string
ii. If the first line is "From:" then it is the address of the sender
iii. The email address is the string surrounded by "<" and ">"
iv. Append the email address to the output file
c) Handle all exceptions that may occur during file operations in task b)
"""


def find_email_addresses(in_file, out_file):
    try:
        input = open(in_file, 'r')
        output = open(out_file, 'w')
        for line in input:
            line = line.strip()
            if line.find("From:") == 0:
                email_address = line[line.find("<") + 1: line.find(">")]
                output.write(email_address + "\n")
        print('File processes successfully')
    except IOError as err:
        print("Error while processing file: ", err)
    finally:
        input.close()
        output.close()



if __name__ == '__main__':
    find_email_addresses(input('Which file do you want to read from?\n'), input('Where should the output be saved?\n'))
