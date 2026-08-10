




class Tab:

    _titles = []
    _tab_labels = []
    _active = ''
    _index = 0
    _started = False



    @classmethod
    def define(cls,tabs, default_active=None):
        cls._titles = []
        cls._tab_labels = []
        cls._index = 0
        cls._started=False
        i=1
        for tab_name,tab_label in tabs.items():
            if isinstance(tab_label, int):
                cls._titles.append(tab_name)
                cls._tab_labels.append(str(i))
            elif not tab_name:
                cls._titles.append(tab_label)
                cls._tab_labels.append(str(i))
            else:
                cls._titles.append(tab_label)
                cls._tab_labels.append(tab_name)
            i += 1
        if default_active and default_active in cls._tab_labels:
            cls._active = default_active
        else:
            cls._active = cls._tab_labels[0] if cls._tab_labels else ''
        html = '<ul class="nav nav-tabs">'
        for i, title in enumerate(cls._titles):
            tab_key = cls._tab_labels[i]
            active_class = 'active' if tab_key == cls._active else ''
            html += f'<li class="nav-item"><a class="nav-link {active_class}" data-bs-toggle="tab" href="#tab-{tab_key}">{title}</a></li>'
        html += '</ul><div class="tab-content mt-4">'
        cls._started = True
        return html




    @classmethod
    def add(cls):
        if not cls._started:return ''
        html = ''
        if cls._index > 0:
            html += '</div>'
        tab_key = cls._tab_labels[cls._index] if cls._index < len(cls._tab_labels) else str(cls._index + 1)
        active_class = 'active' if tab_key == cls._active else ''
        html += f'<div class="tab-pane {active_class}" id="tab-{tab_key}">'
        cls._index += 1
        return html



    @classmethod
    def close(cls):
        if not cls._started:return ''
        cls._started=False
        return '</div></div>'
