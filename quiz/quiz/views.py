from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuizForm

def quiz_view(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            # Return a response with JavaScript code to display a pop-up message
            response = HttpResponse('<script>alert("Thank you! Your answers will be sent to your mail."); window.location.href = "/";</script>')
            return response
    else:
        form = QuizForm()
    return render(request, 'quiz/quiz.html', {'form': form})

def success_view(request):
    return render(request, 'quiz/success.html')


