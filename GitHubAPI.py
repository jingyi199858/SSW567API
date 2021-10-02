import json
import requests

userid = "jingyi199858"

repolist = []
commitslist = []
resultlist = []

# response0 = requests.get("https://api.github.com/users/"+ userid +"/repos")
# result1 = response0.json()
# print(result1)
# for i in result1:
#     repolist.append(i["name"])
#
# print(repolist)
#
# for i in range(len(repolist)):
#     print(repolist[i])
#     response1 = requests.get("https://api.github.com/repos/"+ userid + "/" + repolist[i] +"/commits")
#     print(response1)
#     result2 = response1.json()
#     print("Repo Name: " + repolist[i] + " Commits number:" + str(len(result2)))
#
# print(commitslist)

#This is the function that displays all the repo an user has and all the commits
#that a repo has.
def githubAPI(userid):
    if userid is None:
        print("There is no input, please enter github id")
    if type(userid) != str:
        print("The input is not string")
    response0 = requests.get("https://api.github.com/users/" + userid + "/repos")
    if(response0 != 200):
        result1 = response0.json()
        #print(result1)
        for i in result1:
            repolist.append(i["name"])
        for i in range(len(repolist)):
            #print(repolist[i])
            response1 = requests.get("https://api.github.com/repos/" + userid + "/" + repolist[i] + "/commits")
            if response1 != 200:
                #print(response1)
                result2 = response1.json()
                #print("Repo Name: " + repolist[i] + " Commits number:" + str(len(result2)))
                resultlist.append("Repo Name: " + repolist[i] + " Commits Number:" + str(len(result2)))
            else:
                print("Fail to retrieve information, please check status!")
    else:
        print("Fail to retrieve information, please check status!")
    return resultlist



