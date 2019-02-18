from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .scripts.sudoku import SudokuGrid, SudokuSolver
# Create your views here.


def site_index(request):
    return render(request, 'coding/coding_index.html')


def sudoku(request):
    # solution = {'sudoku': 'test'}
    # try:
    #     nums = request.POST['nums']
    #     sg = SudokuSolver(SudokuGrid(nums))
    #     sg.solve_puzzle()
    #     sg.count = '{:,}'.format(sg.count)
    #     vals = ''
    #     for key, value in sg.grid.puzzle_values.items():
    #         vals += value
    #     solution['sudoku'] = vals
    #     solution['full_grid'] = sg
    # except BaseException as be:
    #     pass
    # return render(request, 'coding/coding_sudoku.html', {'sudoku': solution})
    return render(request, 'coding/coding_sudoku.html')


def ajax_sudoku(request):
    data = {'sudoku': ''}
    try:
        nums = request.POST.get('nums')
        csrf = request.POST.get('csrfmiddlewaretoken')
        sg = SudokuSolver(SudokuGrid(nums))
        sg.solve_puzzle()
        sg.count = '{:,}'.format(sg.count)
        vals = ''
        for key, value in sg.grid.puzzle_values.items():
            vals += value
        data['sudoku'] = vals
        data['nums'] = vals
        data['csrfmiddlewaretoken'] = csrf
        data['iterations'] = sg.count
        data['possible'] = sg.possible
        resp = JsonResponse(data)
    except BaseException as be:
        print('nope', str(be))
        pass
    return resp

