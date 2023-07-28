from django.shortcuts import render, HttpResponseRedirect, redirect
from . import util
from django.http import Http404
import markdown2
import random

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        raise Http404("Page not found")
    else:
        html_content = markdown2.markdown(content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })


def search(request):
    query = request.GET.get('q', '')
    entries = util.list_entries()

    if query in entries:
        return redirect('entry', title=query)

    matching_entries = [entry for entry in entries if query.lower() in entry.lower()]

    return render(request, 'encyclopedia/search_re.html', {
        'query': query,
        'entries': matching_entries
    })


def new_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        entries = util.list_entries()
        if title.lower() in entries:
            return render(request, 'encyclopedia/new_page.html', {
                'error': 'An entry with that title already exists.',
            })

        util.save_entry(title, content)
        return redirect('entry', title=title)

    return render(request, 'encyclopedia/new_page.html')

def edit(request, title):
    content = util.get_entry(title)
    if content is None:
        raise Http404("Page not found")

    return render(request, 'encyclopedia/edit.html', {
        'title': title,
        'content': content
    })


def save_edit(request, title):
    if request.method == 'POST':
        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect('entry', title=title)
    else:
        raise Http404("Invalid request method")


def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('entry', title=random_entry)


def index(request):
        entries = util.list_entries()
        context = {
            'entries': entries
        }
        return render(request, 'encyclopedia/index.html', context)


