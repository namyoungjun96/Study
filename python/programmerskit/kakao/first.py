# 2022 카카오테크 인턴 1번문제

def solution(survey, choices):
    answer = ''
    characterList = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    surveyTemp = {}
    surveyTemp = makeSurvey(characterList)
    surveyTemp = countSurvey(survey, choices, surveyTemp)
    answer = selectCharacter(characterList, surveyTemp)
    return answer

def makeSurvey(characterList):
    surveyTemp = {}

    for i in range(len(characterList)):
        surveyTemp[characterList[i][0]] = 0
        surveyTemp[characterList[i][1]] = 0

    return surveyTemp

def countSurvey(survey, choices, surveyTemp):
    for i in range(len(survey)):
        if choices[i] > 4:
            surveyTemp[survey[i][1]] += (choices[i] - 4)
        elif choices[i] < 4:
            if choices[i] == 1:
                choices[i] = 3
            elif choices[i] == 3:
                choices[i] = 1
            surveyTemp[survey[i][0]] += choices[i]

    return surveyTemp

def selectCharacter(characterList, surveyTemp):
    character = ""
    for i in range(len(characterList)):
        if surveyTemp[characterList[i][0]] >= surveyTemp[characterList[i][1]]:
            character += characterList[i][0]
        else:
            character += characterList[i][1]
    return character

def testSample():
    assert solution(["AN", "CF", "MJ", "RT", "NA"]) == "TCMA"
    assert solution(["TR", "RT", "TR"]) == "RCJA"