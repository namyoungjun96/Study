# 프로그래머스 해시 3단계 베스트 앨범
# 푸는중

def solution(genres, plays):
    answer = []
    playsRank = {}
    genresRank = {}
    
    for i in range(len(plays)):
        playsRank[i] = plays[i]
        
    for i in range(len(genres)):
        if genres[i] not in genresRank:
            genresRank[genres[i]] = plays[i]
        else:
            genresRank[genres[i]] = genresRank.get(genres[i]) + plays[i]
            
    print(playsRank, genresRank)
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)

# [4, 1, 3, 0]