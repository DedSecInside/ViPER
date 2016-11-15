#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Clint Test Suite."""

import os
import unittest


class ClintTestCase(unittest.TestCase):
    """Clint test cases."""

    def setUp(self):
        import clint


    def tearDown(self):
        pass

class ColoredStringTestCase(unittest.TestCase):
    
    def setUp(self):
        from clint.textui.colored import ColoredString
    
    def tearDown(self):
        pass
    
    def test_split(self):
        from clint.textui.colored import ColoredString
        new_str = ColoredString('red', "hello world")
        output = new_str.split()
        assert output[0].s == "hello"
    
    def test_find(self):
        from clint.textui.colored import ColoredString
        new_str = ColoredString('blue', "hello world")
        output = new_str.find('h')
        self.assertEqual(output, 0)
        
    def test_replace(self):
        from clint.textui.colored import ColoredString
        new_str = ColoredString('green', "hello world")
        output = new_str.replace("world", "universe")
        assert output.s == "hello universe"

    def test_py2_bytes_not_mangled(self):
        from clint.textui.colored import ColoredString
        # On python 2 make sure the same bytes come out as went in
        new_str = ColoredString('RED', '\xe4')
        assert '\xe4' in str(new_str)
        from clint.textui import puts
        puts(new_str)

    def test_clint_force_color_env_var(self):
        from clint.textui.colored import ColoredString
        os.environ['CLINT_FORCE_COLOR'] = "1"
        new_str = ColoredString('RED', 'hello world')
        assert new_str.always_color == True


class TextuiFormatterTestCase(unittest.TestCase):

    def test_max_width(self):

        def _test_n_rows_width(ins, rows, n_rows, max_width):
            ins.assertEqual(len(rows), n_rows)
            for row in rows:
                ins.assertLessEqual(len(row), max_width)

        from clint.textui.formatters import max_width
        from clint.textui import colored
        # normal text
        text = ' '.join(['XXX'] * 3)
        rows = max_width(text, 6).split('\n')
        _test_n_rows_width(self, rows, 3, 6)
        rows = max_width(text, 7).split('\n')
        _test_n_rows_width(self, rows, 2, 7)
        # colored text
        c_text = colored.yellow(text)
        rows = max_width(c_text, 6).split('\n')
        _test_n_rows_width(self, rows, 3, 6)
        rows = max_width(c_text, 7).split('\n')
        _test_n_rows_width(self, rows, 2, 7)


if __name__ == '__main__':
    unittest.main()
