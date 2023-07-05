from collections import defaultdict

def solution(genres, plays):
    answer = []
    # 노래 수록 기준
    # 장르, 노래, 낮은 고유번호 순
    song_dict = defaultdict(list)
    genre_playtime = defaultdict(int)
    for i in range(len(genres)):
        genre_playtime[genres[i]] += plays[i]
        song_dict[genres[i]].append((plays[i], i))
    
    sorted_playtime = sorted(genre_playtime.items(), key=lambda x: -x[1] )
    for key, _ in sorted_playtime:
        sorted_songs = sorted(song_dict[key], key=lambda x: (-x[0], x[1]))
        L = 2 if len(sorted_songs) >= 2 else 1
        answer += [sorted_songs[i][1] for i in range(L)]

    
    return answer