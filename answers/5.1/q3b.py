# answer key
ans = ["c","d","b","a","b","d","a","c","d","c"]
response = []
correct = 0
wrong = 0

# input ans until all questions are answered
while len(response) < len(ans):
    studentAns = input("what is your answer? --> ")
    response.append(studentAns)

# print both answer key and student inputs
print(f'your answer : answer key')
# for loop for all items inside list of response
for qn in range(len(response)):
    print(f"{response[qn]:^10}  :  {ans[qn]:^10}")
    
    # check if ans is correct
    if response[qn] == ans[qn]:
        correct += 1
    else:
        wrong += 1

# print result
print(f"correct answers: {correct}")
print(f"wrong answers: {wrong}")
