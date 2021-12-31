# 프로그래머스 해시 3단계 베스트 앨범

def solution(genres, plays):
    answer = []
    playsRank = {}
    genresRank = {}
    genresFrequency = {}
    genre = ''
    Rank = []
    
    for i in range(len(plays)):
        playsRank[i] = plays[i]
        
    for i in range(len(genres)):
        if genres[i] not in genresRank:
            genresRank[genres[i]] = plays[i]
        else:
            genresRank[genres[i]] = genresRank.get(genres[i]) + plays[i]
            
        if genres[i] not in genresFrequency:
            genresFrequency[genres[i]] = 1
        else:
            genresFrequency[genres[i]] = 2
    plays.sort(reverse=True)
    genresList = list(genresRank.keys())
    
    for i in range(len(genresList)):
        if genresFrequency.get(genresList[i]) == 1:
            Rank.append(genresRank.get(genresList[i]))
        elif genresFrequency.get(genresList[i]) == 2:
            Rank.append(genresRank.get(genresList[i]))
            Rank.append(genresRank.get(genresList[i]))
    Rank.sort()
    
    while Rank:
        temp = 0
        genresTemp = Rank.pop()
        
        for i in range(len(genresList)):
            if genresRank.get(genresList[i]) == genresTemp:
                genre = genresList[i]
                
        for i in range(len(plays)):
            for j in range(len(genres)):
                if plays[i] == playsRank.get(j) and genres[j] == genre:
                    playNumber = j
                    playsRank[j] = 0
                    answer.append(playNumber)
                    temp = 1
                    break
            if temp == 1:
                del plays[i]
                break
            
    print(playsRank)    
    print(answer)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop", "kpop"]
plays = [500, 600, 150, 800, 2500, 2100]

solution(genres, plays)

# [4, 1, 3, 0]