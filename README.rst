py.spec
=======

`RSpec <http://rspec.info/>`_ has really awesome BDD syntax for managing
context.  Wouldn't it be nice if we had something like it for Python?  Perhaps
something that leveraged the awesomeness of `py.test <http://pytest.org/>`_?

.. image:: https://github.com/jasonkeene/py.spec/raw/master/aliens.gif
.. image:: https://github.com/jasonkeene/py.spec/raw/master/now.gif

Add these lines to your pytest.ini::

    [pytest]
    python_classes=Test Describe Context
    python_functions=test it

Then write your tests like this::

    class DescribeWidget:
        @pytest.fixture
        def widget(self):
            return Widget(3, 4)

        def it_adds(self, widget):
            assert widget.add() == 7

        class ContextWithExplosives:
            @pytest.fixture
            def widget(self, widget):
                widget.explode = True
                return widget

            def it_explodes(self, widget):
                with pytest.raises(Exception):
                    widget.add()

            class ContextWithExplodingDinosaurs:
                @pytest.fixture
                def widget(self, widget):
                    widget.jurassic = True
                    return widget

                def it_rawrs(self, widget):
                    with pytest.raises(Exception) as e:
                        widget.add()
                    assert e.value.message == "RAWR!" * 1000

.. image:: https://github.com/jasonkeene/py.spec/raw/master/ohyes.gif

Thanks to `@theY4Kman <https://github.com/theY4Kman>`_ for showing me how
nested fixtures work!
