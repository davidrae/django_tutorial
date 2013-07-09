from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Paginator(object_list, per_page, orphans=0, allow_empty_first_page=True)


def listing(request):
    foo_list = Contacts.objects.all()
    paginator = Paginator(foo_list, 3) # Show 3 contacts per page

    page = request.GET.get('page')
    try:
        foo = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        foo = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        foo = paginator.page(paginator.num_pages)

    return render_to_response('foo/foo_list.html', {"foo": foo})