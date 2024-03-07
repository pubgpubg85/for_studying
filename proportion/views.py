from django.shortcuts import render


def proportion(request):
    l1 = request.GET.get('l1')
    l2 = request.GET.get('l2')
    r1 = request.GET.get('r1')
    r2 = request.GET.get('r2')
    result = 'please put only one \"x\" into one of following inputs'
    al = [l1, r1, l2, r2]
    title = 'Proportion'
    if 'x' not in al:
        result = 'please put \"x\" into one of following inputs'
    elif al.count('x') != 1:
        result = 'we need only one x'
    else:
        for i in range(len(al)):
            if al[i] == 'x' and al.index('x') in [0, 3]:
                try:
                    result = (float(al[i - 2]) * float(al[i - 1])) / float(al[i - 3])
                except IndexError:
                    result = (float(al[i + 2]) * float(al[i + 1])) / float(al[i + 3])
            elif al[i] == 'x' and al.index('x') == 1:
                result = (float(al[i - 1]) * float(al[i + 2])) / float(al[i + 1])
            elif al[i] == 'x' and al.index('x') == 2:
                result = (float(al[i + 1]) * float(al[i - 2])) / float(al[i - 1])
    context = {'result': result, 'title': title}
    return render(request, 'proportion/index.html', context)
