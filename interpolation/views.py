from django.shortcuts import render


def interpolation(request):
    x1 = request.GET.get('x1')
    x2 = request.GET.get('x2')
    fx1 = request.GET.get('fx1')
    fx2 = request.GET.get('fx2')
    x = request.GET.get('x')
    title = 'interpolation'
    if x:
        try:
            x1, x2, fx1, fx2, x = map(float, [x1, x2, fx1, fx2, x])
            result = fx1 + (x - x1) * ((fx2 - fx1) / (x2 - x1))
        except ValueError:
            result = 'Please don\'t put str objects'
        except ZeroDivisionError:
            result = 'ZeroDivisionError'

        context = {
            'result': result,
            'x1': x1,
            'x2': x2,
            'fx1': fx1,
            'fx2': fx2,
            'x': x,
            'title': title
        }
        return render(request, "interpolation/index.html", context)
    else:
        return render(request, "interpolation/index.html", {'title': title})

