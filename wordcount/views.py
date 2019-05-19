from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')  #3번째 인자, 딕셔너리형 자료형을 받을 수 있다.


def about(request) :
    return render(request, 'about.html')

def result(request) :
    text=request.GET['fulltext']
    words=text.split()  # 이거자체가 리스트!
    word_dictionary={}

    for word in words :
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else :
            #add to dictionary
            word_dictionary[word]=1
    
    return render(request, 'result.html', {'full':text,'total': len(words), 'dictionary' : word_dictionary.items()}) 
   