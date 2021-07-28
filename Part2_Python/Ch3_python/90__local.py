

'''
locals
: 로컬에 선언된 모든 변수를 조회할 수 있는 강력한 명령
: -> 디버깅에 많은 도움
'''


import pprint


nums = [2, 7, 11, 15]
num_ragnge = range(1, 4)


pprint.pprint(locals())

# {'__annotations__': {},
#  '__builtins__': <module 'builtins' (built-in)>,
#  '__cached__': None,
#  '__doc__': '\nlocals\n: 로컬에 선언된 모든 변수를 조회할 수 있는 강력한 명령\n: -> 디버깅에 많은 도움\n',
#  '__file__': 'C:/Users/chaeyun/PycharmProjects/python_algorithm_interview/Part2_Python/Ch3_python/90__local.py',
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001E30B9D0910>,
#  '__name__': '__main__',
#  '__package__': None,
#  '__spec__': None,
#  'num_ragnge': range(1, 4),
#  'nums': [2, 7, 11, 15],
#  'pprint': <module 'pprint' from 'C:\\Users\\chaeyun\\AppData\\Local\\Programs\\Python\\Python38\\lib\\pprint.py'>}
