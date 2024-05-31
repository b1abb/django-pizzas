from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_instance = form.save()
            return redirect('feedback_thank_you', feedback_id=feedback_instance.id)
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedbackForm.html', {'form': form})


def feedback_thank_you(request, feedback_id):
    feedback_instance = Feedback.objects.get(id=feedback_id)
    context = {
        'name': feedback_instance.name,
        'email': feedback_instance.email,
        'theme': feedback_instance.get_theme_display(),
        'message': feedback_instance.message,
        'created_at': feedback_instance.created_at,
    }
    return render(request, 'feedback/feedbackEnd.html', context)


def goodLinks(request):
    return render(request, 'feedback/goodLinks.html')
