from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Notice

def notice_list(request):
    # Get the search query from the request
    query = request.GET.get('q', '')
    
    # Filter notices based on the search query
    notices = Notice.objects.all()
    if query:
        notices = notices.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    
    # Paginate the notices (5 notices per page)
    paginator = Paginator(notices, 5)  # Show 5 notices per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'notices/notice_list.html', {
        'page_obj': page_obj,
        'query': query,
    })

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, id=pk)
    return render(request, 'notices/notice_detail.html', {'notice': notice})