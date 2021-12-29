# 프로그래머스 해시 3단계 주식가격
# 푸는중

def solution(genres, plays):
    answer = []
    album = {}
    genresList = list(set(genres))
    playList = sorted(plays)
    
    for i in range(len(genres)):
        album[plays[i]] = genres[i]
        
    while genresList:
        count = 0
        genresCompare = genresList.pop()
        for i in playList:
            if count == 2:
                break
            elif album.get(i) == genresCompare:
                answer
                count += 1
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)

a = (1, 2, 3, 4, 1, 2, 3, 4)
b = list(set(a))
print(a, b)

# [4, 1, 3, 0]