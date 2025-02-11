test = {
  'name': 'test_ses05_solution_selection_sort_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> selection_sort([1, 13, -23, 2.7, -3, 5, 7.5])
          [-23, -3, 1, 2.7, 5, 7.5, 13]
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ses05 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
