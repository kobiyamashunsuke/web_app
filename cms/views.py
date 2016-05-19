from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from cms.models import Book, Impression , python_Book , python_Impression
from cms.forms import BookForm, ImpressionForm
from django.db.models import Q


def home(request):
    """書籍の一覧"""
    if request.GET.get('your_name'):
        d = {'your_name': request.GET.get('your_name')}
        books = Book.objects.filter(Q(func_name__contains=request.GET.get('your_name'))| Q(program_name__contains=request.GET.get('your_name'))|Q(tag__contains=request.GET.get('your_name'))|Q(author__contains=request.GET.get('your_name')))
    else:
        books = Book.objects.all().order_by('id')
    return render(request, 'cms/home.html', {'books': books})

def book_list(request):
    """書籍の一覧"""
    if request.GET.get('your_name'):
        d = {'your_name': request.GET.get('your_name')}
        books = Book.objects.filter(Q(func_name__icontains=request.GET.get('your_name'))| Q(program_name__icontains=request.GET.get('your_name'))|Q(tag__icontains=request.GET.get('your_name'))|Q(author__icontains=request.GET.get('your_name')))
    else:
        books = Book.objects.all().order_by('id')
    return render(request, 'cms/book_list.html', {'books': books})

def book_edit(request, book_id=None):
    """書籍の編集"""
    if book_id:  # book_id が指定されている (修正時)
        book = get_object_or_404(Book, pk=book_id)
    else:  # book_id が指定されていない (追加時)
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:  # GET の時
        form = BookForm(instance=book)  # book インスタンスからフォームを作成

    return render(request, 'cms/book_edit.html', dict(form=form, book_id=book_id))

def book_del(request, book_id):
    """書籍の削除"""
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('cms:book_list')

class ImpressionList(ListView):
    """感想の一覧"""
    context_object_name='impressions'
    template_name='cms/impression_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['book_id'])  # 親の書籍を読む
        impressions = book.impressions.all().order_by('id')   # 書籍の子供の、感想を読む
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, book=book)
        return self.render_to_response(context)

def impression_del(request, book_id, impression_id):
    """感想の削除"""
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression_list', book_id=book_id)

def impression_edit(request, book_id, impression_id=None):
    """感想の編集"""
    book = get_object_or_404(Book, pk=book_id)  # 親の書籍を読む
    if impression_id:   # impression_id が指定されている (修正時)
        impression = get_object_or_404(Impression, pk=impression_id)
    else:               # impression_id が指定されていない (追加時)
        impression = Impression()

    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            impression = form.save(commit=False)
            impression.book = book  # この感想の、親の書籍をセット
            impression.save()
            return redirect('cms:impression_list', book_id=book_id)
    else:    # GET の時
        form = ImpressionForm(instance=impression)  # impression インスタンスからフォームを作成

    return render(request,
                  'cms/impression_edit.html',
                  dict(form=form, book_id=book_id, impression_id=impression_id))


def python_book_list(request):
    """書籍の一覧"""
    if request.GET.get('your_name'):
        d = {'your_name': request.GET.get('your_name')}
        python_books = python_Book.objects.filter(Q(func_name__icontains=request.GET.get('your_name'))| Q(program_name__icontains=request.GET.get('your_name'))|Q(tag__icontains=request.GET.get('your_name'))|Q(author__icontains=request.GET.get('your_name')))
    else:
        python_books = python_Book.objects.all().order_by('id')
    return render(request, 'cms/python_list.html', {'python_books': python_books})

def python_book_edit(request, python_book_id=None):
    """書籍の編集"""
    if python_book_id:  # book_id が指定されている (修正時)
        python_book = get_object_or_404(python_Book, pk=python_book_id)
    else:  # book_id が指定されていない (追加時)
        python_book = python_Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=python_book)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            python_book = form.save(commit=False)
            python_book.save()
            return redirect('cms:python_book_list')
    else:  # GET の時
        form = BookForm(instance=python_book)  # book インスタンスからフォームを作成

    return render(request, 'cms/python_book_edit.html', dict(form=form, python_book_id=python_book_id))

def python_book_del(request, python_book_id):
    """書籍の削除"""
    python_book = get_object_or_404(python_Book, pk=python_book_id)
    python_book.delete()
    return redirect('cms:python_book_list')

class python_ImpressionList(ListView):
    """感想の一覧"""
    context_object_name='python_impressions'
    template_name='cms/python_impression_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        python_book = get_object_or_404(python_Book, pk=kwargs['python_book_id'])  # 親の書籍を読む
        python_impressions = python_book.impressions.all().order_by('id')   # 書籍の子供の、感想を読む
        self.object_list = python_impressions

        context = self.get_context_data(object_list=self.object_list, python_book=python_book)
        return self.render_to_response(context)

def python_impression_edit(request, python_book_id, python_impression_id=None):
    """感想の編集"""
    python_book = get_object_or_404(python_Book, pk=python_book_id)  # 親の書籍を読む
    if python_impression_id:   # impression_id が指定されている (修正時)
        python_impression = get_object_or_404(python_Impression, pk=python_impression_id)
    else:               # impression_id が指定されていない (追加時)
        python_impression = python_Impression()

    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=python_impression)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            python_impression = form.save(commit=False)
            python_impression.book = python_book  # この感想の、親の書籍をセット
            python_impression.save()
            return redirect('cms:python_impression_list', python_book_id=python_book_id)
    else:    # GET の時
        form = ImpressionForm(instance=python_impression)  # impression インスタンスからフォームを作成

    return render(request,
                  'cms/python_impression_edit.html',
                  dict(form=form, python_book_id=python_book_id, python_impression_id=python_impression_id))

def python_impression_del(request, python_book_id, python_impression_id):
    """感想の削除"""
    python_impression = get_object_or_404(python_Impression, pk=python_impression_id)
    python_impression.delete()
    return redirect('cms:python_impression_list', python_book_id=python_book_id)





