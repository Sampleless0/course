# answer key
ans = ["c","d","b","a","b","d","a","c","d","c"]
response = []

# input ans until all questions are answered
while len(response) < len(ans):
    studentAns = input("what is your answer? --> ")
    response.append(studentAns)
    
# print both answer key and student inputs
print(ans)
print(response)
