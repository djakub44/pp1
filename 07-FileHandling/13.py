movie_titles = [None]*5

for i in range(5):
    movie_titles[i] = "film nr " + str(i+1)

file = open('movies.txt','w')

for i in range(len(movie_titles)):
    file.write(movie_titles[i]+'\n')

file.close()

file = open('movies.txt','r')
file_content = file.read()
print(file_content, end = "")
file.close()
