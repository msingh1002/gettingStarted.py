def welcome_assignment_answers(question):
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "cb0a815837c664e59ccfa806a84b72baf79c9810674a3332596038d1e74935cb"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = "5"
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = "3"
    else:
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return(answer)

if __name__ == "__main__":
    #I am using this space to make sure the code works
    debug_question = "Is it possible to decode a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question))