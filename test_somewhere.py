import pytest

from somewhere import Widget


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
